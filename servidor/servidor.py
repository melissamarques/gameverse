import socket, threading
from banco_de_dados import Banco
import datetime
import json

def tratar_mensagem(mensagem):
    """
    Processa a mensagem recebida e retorna uma resposta.

    A função tratar_mensagem processa a mensagem recebida do cliente e retorna uma resposta.
    Ao receber uma mensagem, a função a divide em elementos separados pelo caractere "-". Em seguida, 
    ela analisa o primeiro elemento da lista resultante para determinar qual ação realizar. No final,
    a função retorna a variável envia, que contém a resposta em formato de string a ser enviada de 
    volta ao cliente.
 
    Parameters
    ----------
    mensagem : str
        A mensagem recebida do cliente.

    Returns
    -------
    str
        A resposta em string para ser enviada de volta ao cliente.
    """

    l = mensagem.split("-")
    envia = ''
    if l[0] == '-1':
        banco.botao_sair()
        envia = "-1"
    elif l[0] == '-2':
        envia = "-2"
    elif l[0] == '0': 
        username = l[1]
        senha = l[2]
        if banco.logar_usuario(username, senha):
            banco.obter_nome_usuario_logado()
            envia = "1"
            print(f'{username} entrou no GameVerse!')
        else:
            envia = "0"
    elif l[0] == '1':  
        username = l[1]
        email = l[2]
        senha = l[3]
        data_criacao = datetime.date.today().strftime('%Y-%m-%d')
        if banco.cadastrar_usuario(username, email, senha, data_criacao):
            envia = '1'
            print(f'{username} agora faz parte do GameVerse.')
        else:
            envia = '0'
    elif l[0] == '2':
        jogo_id = str(l[1])
        nome_jogo = banco.abrir_tela_jogo(jogo_id)
        if nome_jogo is not None:
            envia = str(nome_jogo)
        else:
            envia = '0'
    elif l[0] == '3':
        usuario_id = int(l[1])
        jogo_id = int(l[2])
        texto_review = l[3]
        if banco.salvar_review(usuario_id, jogo_id, texto_review):
            envia = '1'
            print('review salva')
        else:
            envia = '0'
            print('erro ao salvar a review')
    elif l[0] == '4':
        jogos = banco.obter_jogos()
        envia = '\n'.join('{} | {} ({})'.format(j[0], j[1], j[2]) for j in jogos)
    elif l[0] == '5':
        jogo_id = str(l[1])
        reviews = banco.obter_reviews(jogo_id)
        if reviews:
            envia = '\n'.join(' | '.join(str(item) for item in review) for review in reviews)
        else:
            envia = ' '
    elif l[0] == '6':
        jogo_id = int(l[1])
        informacoes_jogo = banco.carregar_jogo(jogo_id)
        if informacoes_jogo:
            envia = json.dumps(informacoes_jogo)
        else:
            envia = ''
    elif l[0] == '7':
        usuario_id = int(l[1])
        num_reviews = int(l[2])
        ultimas_reviews = banco.obter_ultimas_reviews_usuario(usuario_id, num_reviews)
        if ultimas_reviews is not None:
            envia = '\n'.join(' | '.join(str(item) for item in review) for review in ultimas_reviews) 
    elif l[0] == '8':
        username = l[1]
        if banco.obter_nome_usuario_logado() == username:
            envia = '1'
            usuario_id = banco.get_id_usuario(username)
            print(f"Usuário {username} logado. ID do usuário: {usuario_id}")
        else:
            envia = '0'
    elif l[0] == '9':
        username = l[1]
        print('Recebido pedido de ID do usuário para:', username)
        usuario_id = banco.get_id_usuario(username)
        if usuario_id is not None:
            envia = str(usuario_id)
        else:
            envia = '0'
    elif l[0] == '10':
        username = l[1]
        senha = l[2]

        if banco.logar_administrador(username, senha):
            envia = "1"
            print(f'Administrador entrou no GameVerse!')
        else:
            envia = "0"
    elif l[0] == '11':
        nome = l[1]
        desenvolvedor = l[2]
        distribuidora = l[3]
        ano_lancamento = l[4]
        descricao = l[5]
        
        if banco.adicionar_jogo(nome, desenvolvedor, distribuidora, ano_lancamento, descricao):
            envia = '1'
            print(f"Jogo {nome} adicionado ao banco de dados.")
        else:
            envia = '0' 
            print("Falha ao adicionar o jogo ao banco de dados.")
    elif l[0] == '12':
        resultados = banco.carregar_jogos_adm()
        envia = '\n'.join(' {} | {} | ({})'.format(r[0], r[1], r[2]) for r in resultados)
        print(envia)
    elif l[0] == '13':
        jogo_id = int(l[1])
        if banco.excluir_jogo(jogo_id):
            envia = '1'
            print(f"Jogo {jogo_id} excluído do banco de dados.")
        else:
            envia = '0'
            print(f"Falha ao excluir o jogo {jogo_id} do banco de dados.")
    elif l[0] == "14":
        filtro = l[1]
        pesquisa = l[2]
        jogos = banco.pesquisar_jogos(filtro, pesquisa)
        if jogos:
            envia = "\n".join(jogos)
        else:
            envia = "Nenhum jogo encontrado!"
            print('Nenhum jogo encontrado')
    else:
        envia = "Comando inválido"
    return envia

class ClientThread(threading.Thread):
    """
    Classe que representa uma thread para lidar com a comunicação com um cliente.

    ...

    Attributes
    ----------
    connection : socket
        O objeto de conexão com o cliente.

    Methods
    -------
    __init__(self, connection)
        Construtor da classe. Inicializa o objeto de conexão com o cliente.
        
    run(self)
        Executa a thread do cliente.
    """
   
    def __init__(self, connection):
        """
        Parameters
        ----------
        connection : socket
            O objeto de conexão com o cliente.
        """

        super().__init__()
        self.con = connection
    
    def run(self):
        """
        Executa a thread do cliente.

        Este método é executado quando a thread do cliente é iniciada. Ele contém um loop infinito que recebe
        mensagens do cliente, processa essas mensagens utilizando a função `tratar_mensagem`, e envia a resposta
        de volta ao cliente.
        """

        while True:
            recebe = self.con.recv(1024)
            enviar = tratar_mensagem(recebe.decode())
            if enviar == "-1":
                self.con.send(enviar.encode())
                break
            else:
                self.con.send(enviar.encode())

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8087
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))
    banco = Banco()

    while True:
        server_socket.listen(10)
        print("esperando cliente...")
        con, cliente = server_socket.accept()
        print("cliente aceito...")
        sinc = threading.Lock()
        newThread = ClientThread(con)
        newThread.start()
