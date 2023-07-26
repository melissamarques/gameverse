import mysql.connector as mysql
import datetime
from PyQt5.QtCore import QCoreApplication

class Banco:
    """
    Classe que representa o banco de dados do aplicativo.

    ...

    Attributes
    ----------
    conexao : mysql.connector.connection.MySQLConnection
        A conexão com o banco de dados.
    cursor : mysql.connector.cursor.MySQLCursor
        O cursor para executar comandos SQL no banco de dados.
    usuario_logado : None
        O usuário logado no momento. Inicialmente, nenhum usuário está logado.

    Methods
    -------
    __init__(self)
        Construtor da classe.

    cadastrar_usuario(self, username, email, senha, data_criacao)
        Cadastra um novo usuário no banco de dados.

    obter_nome_usuario_logado(self)
        Obtém o nome do usuário logado no momento.

    logar_usuario(self, username, senha)
        Realiza o login de um usuário no aplicativo.

    logar_administrador(self, username, senha)
        Realiza o login de um administrador no aplicativo.

    obter_jogos(self)
        Obtém a lista de jogos do banco de dados.

    abrir_tela_jogo(self, jogo_id)
        Abre a tela de um jogo específico.

    carregar_jogo(self, jogo_id)
        Carrega as informações de um jogo específico.

    salvar_review(self, usuario_id, jogo_id, data_criacao, texto_review)
        Salva uma review de um jogo feita por um usuário.

    get_id_usuario(self, username)
        Obtém o ID de um usuário a partir do nome de usuário.

    get_id_do_jogo(self, jogo)
        Obtém o ID de um jogo a partir do nome do jogo.

    obter_reviews(self, jogo_id)
        Obtém as reviews de um jogo específico.

    obter_ultimas_reviews_usuario(self, num_reviews)
        Obtém as últimas reviews feitas por um usuário.

    adicionar_jogo(self, nome, desenvolvedor, distribuidora, ano_lancamento, descricao)
        Adiciona um novo jogo ao banco de dados.

    carregar_jogos_adm(self)
        Carrega a lista de jogos para o administrador.

    botao_sair(self)
        Realiza o logout do usuário atual e fecha a conexão com o banco de dados.
    """

    def __init__(self) -> None:
        """
        Construtor da classe.
        
        Inicializa a conexão com o banco de dados, cria as tabelas necessárias
        caso elas não existam e configura a instância da classe TelaInicial.
        """

        self.conexao = mysql.connect(host='localhost', db='gameverse', user='root', passwd='202190m?34913')
        self.cursor = self.conexao.cursor()

        self.usuario_logado = None

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username TEXT,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    data_criacao DATE NOT NULL
                )''')

        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS jogos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    desenvolvedor TEXT NOT NULL,
                    distribuidora TEXT NOT NULL,
                    ano_lancamento TEXT NOT NULL,
                    descricao TEXT NOT NULL
                )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    jogo_id INT NOT NULL,
                    texto_review TEXT NOT NULL,
                    data_criacao DATE NOT NULL
                )''')

    def cadastrar_usuario(self, username, email, senha, data_criacao):
        """
        Cadastra um novo usuário no banco de dados.

        Essa função é responsável por realizar o cadastro de um novo usuário no banco de dados. 
        A função retorna True, indicando que o usuário foi cadastrado com sucesso. Caso contrário,
        se o resultado não for None, significa que já existe um usuário com o mesmo nome de usuário
        e o cadastro não pode ser realizado. Nesse caso, a função retorna False.

        Parameters
        ----------
        username : str
            O nome de usuário do novo usuário.
        email : str
            O email do novo usuário.
        senha : str
            A senha do novo usuário.
        data_criacao : str
            A data de criação do novo usuário.

        Returns
        -------
        bool
            True se o usuário foi cadastrado com sucesso, False caso contrário.
        """

        self.cursor.execute('SELECT * FROM usuarios WHERE username = %s', (username,))
        resultado = self.cursor.fetchone()
        if resultado is None:
            self.cursor.execute('INSERT INTO usuarios(username, email, senha, data_criacao) VALUES (%s, %s, %s, %s)',
                            (username, email, senha, data_criacao))
            self.conexao.commit()
            return True
        return False
    
    def obter_nome_usuario_logado(self):
        """
        Obtém o nome do usuário logado no momento.

        Essa função é responsável por obter o nome do usuário que está
        logado no momento. Ela verifica se há um usuário logado diferente de None. Se houver,
        a função executa uma consulta no banco de dados para obter o nome do usuário correspondente 
        ao ID do usuário logado.O resultado da consulta é armazenado na variável resultado.
        Se o resultado não for None, ou seja, se o usuário logado existe no banco de dados, a função
        retorna o nome do usuário (resultado[0]).
        Caso contrário, se o resultado for None, significa que nenhum usuário está logado ou o usuário
        logado não foi encontrado no banco de dados. Nesse caso, a função retorna None.

        Returns
        -------
        str or None
            O nome do usuário logado, ou None se nenhum usuário estiver logado.
        """

        if self.usuario_logado is not None:
            self.cursor.execute('SELECT username FROM usuarios WHERE id = %s', (self.usuario_logado,))
            resultado = self.cursor.fetchone()
            if resultado is not None:
                return resultado[0]
        return None

    def logar_usuario(self, username, senha):
        """
        Realiza o login de um usuário no aplicativo.

        Essa função é responsável por realizar o login de um usuário no 
        aplicativo. Ela recebe como parâmetros o username (nome de usuário) e senha 
        do usuário que deseja fazer o login. Em seguida, a função executa uma consulta
        no banco de dados para verificar se existe um registro de usuário com o nome de
        usuário e senha fornecidos. O resultado da consulta é armazenado na variável resultado.
        Se o resultado não for None, a função retorna True, indicando que o login foi bem-sucedido.
        Caso contrário, se o resultado for None, a função retorna False, indicando que o login não 
        foi bem-sucedido.

        Parameters
        ----------
        username : str
            O nome de usuário do usuário.
        senha : str
            A senha do usuário.

        Returnds
        -------
        bool
            True se o login foi bem-sucedido, False caso contrário.
        """

        self.usuario_logado = None
        self.cursor.execute('SELECT * FROM usuarios WHERE username = %s AND senha = %s', (username, senha))
        resultado = self.cursor.fetchone()
        if resultado is not None:
            self.obter_nome_usuario_logado()
            return True
        return False


    def logar_administrador(self, username, senha):
        """
        Realiza o login de um administrador no aplicativo.

        Essa função é responsável por realizar o login de um administrador
        no aplicativo. Ela recebe como parâmetros o username (nome de usuário) e senha do
        administrador que deseja fazer o login. A função verifica se o username é igual a 
        "admin" e a senha é igual a "admin123". Se forem iguais, significa que o login do 
        administrador foi bem-sucedido, e a função retorna True. Caso contrário, se o username
        ou a senha forem diferentes, significa que o login não foi bem-sucedido, e a função retorna False.

        Parameters
        ----------
        username : str
            O nome de usuário do administrador.
        senha : str
            A senha do administrador.

        Returns
        -------
        bool
            True se o login foi bem-sucedido, False caso contrário.
        """

        if username == 'admin' and senha == 'admin123':
            return True
        else:
            return False

    def obter_jogos(self):
        """
        Obtém a lista de jogos do banco de dados.

        Essa função é responsável por obter a lista de jogos do banco de dados.
        Ela executa uma consulta no banco de dados para selecionar os campos id, nome e 
        ano_lancamento da tabela jogos. O resultado da consulta é armazenado na variável jogos.
        A função retorna a lista de jogos obtida, no formato [(id, nome, ano_lancamento), ...].

        Returns
        -------
        list
            A lista de jogos no formato [(id, nome, ano_lancamento), ...].
        """

        self.cursor.execute("SELECT id, nome, ano_lancamento FROM jogos")
        jogos = self.cursor.fetchall()
        return jogos
    
    def abrir_tela_jogo(self, jogo_id):
        """
        Abre a tela de um jogo específico.

        Essa função é responsável por abrir a tela de um jogo específico.
        A função executa uma consulta no banco de dados para verificar se existe um registro 
        de jogo com o ID especificado. O resultado da consulta é armazenado na variável resultado.
        Se o resultado não for None, ou seja, se a consulta encontrou um registro de jogo correspondente
        ao ID informado, a função retorna o ID do jogo aberto (resultado[0]). Caso contrário, se o
        resultado for None, significa que o jogo com o ID especificado não existe, e a função retorna None.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo a ser aberto.

        Returns
        -------
        int or None
            O ID do jogo aberto, ou None se o jogo não existir.
        """
        self.cursor.execute("SELECT id FROM jogos WHERE id = %s", (jogo_id,))
        resultado = self.cursor.fetchone()
        if resultado is not None:
            return resultado[0]
        return None

    def carregar_jogo(self, jogo_id):
        """
        Carrega as informações de um jogo específico.

        Essa função é responsável por carregar as informações de um jogo específico.
        A função executa uma consulta no banco de dados para obter as informações do jogo com o
        ID especificado. O resultado da consulta é armazenado na variável jogo_data. Se jogo_data
        não for None e tiver comprimento maior que zero, significa que a consulta encontrou um jogo
        correspondente ao ID informado. Nesse caso, as informações do jogo são extraídas de jogo_data
        e armazenadas em um dicionário jogo com as chaves 'nome', 'desenvolvedor', 'distribuidora',
        'ano_lancamento' e 'descricao'. Esse dicionário é retornado pela função.
        Caso contrário, se jogo_data for None ou tiver comprimento igual a zero, significa que o jogo
        com o ID especificado não existe, e a função retorna None.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo a ser carregado.

        Returns
        -------
        dict or None
            Um dicionário contendo as informações do jogo, ou None se o jogo não existir.
            O dicionário tem a seguinte estrutura: {'nome': nome, 'desenvolvedor': desenvolvedor,
            'distribuidora': distribuidora, 'ano_lancamento': ano_lancamento, 'descricao': descricao}.
        """

        self.cursor.execute(
            "SELECT nome, desenvolvedor, distribuidora, ano_lancamento, descricao FROM jogos WHERE id = %s",
            (jogo_id,)
        )
        jogo_data = self.cursor.fetchone()
        
        if jogo_data and len(jogo_data) > 0:
            jogo = {
                'nome': jogo_data[0],
                'desenvolvedor': jogo_data[1],
                'distribuidora': jogo_data[2],
                'ano_lancamento': jogo_data[3],
                'descricao':jogo_data[4] 
                }
            return jogo
        else:
            return None
    
    def salvar_review(self, usuario_id, jogo_id, texto_review, data_criacao = None):
        """
        Salva uma review de um jogo feita por um usuário.

        Essa função é responsável por salvar uma review de um jogo feita por um usuário.
        Ela recebe como parâmetros o usuario_id, que é o ID do usuário que fez a review, o jogo_id, 
        que é o ID do jogo que recebeu a review, a data_criacao, que é a data de criação da review,
        e o texto_review, que é o texto da review. Em seguida, a função tenta executar uma inserção
        na tabela reviews do banco de dados, com os valores fornecidos. Se a inserção for bem-sucedida,
        ou seja, nenhum erro ocorrer, a transação é confirmada com self.conexao.commit() e a função retorna
        True, indicando que a review foi salva com sucesso. Caso ocorra algum erro durante a execução da
        inserção, uma exceção é capturada e uma mensagem de erro é exibida. A função retorna False, indicando
        que houve um erro ao salvar a review.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário que fez a review.
        jogo_id : int
            O ID do jogo que recebeu a review.
        data_criacao : str
            A data de criação da review.
        texto_review : str
            O texto da review.

        Returns
        -------
        bool
            True se a review foi salva com sucesso, False caso contrário.
        """

        data_criacao = datetime.datetime.now()
        try:
            self.cursor.execute('INSERT INTO reviews (usuario_id, jogo_id, data_criacao, texto_review) VALUES (%s, %s, %s, %s)', 
                                (usuario_id, jogo_id, data_criacao, texto_review))
            self.conexao.commit()
            return True
        except Exception as e:
            print("Erro ao salvar review:", e)
            return False

    def get_id_usuario(self, username):
        """
        Obtém o ID de um usuário a partir do nome de usuário.

        Essa função é responsável por obter o ID de um usuário a partir do seu nome de usuário.
        Ela recebe como parâmetro username, que é o nome de usuário do usuário. A função executa uma consulta 
        na tabela usuarios do banco de dados, filtrando pelo username fornecido. O resultado da consulta é obtido
        utilizando self.cursor.fetchone(), que retorna uma única linha da consulta. Se o resultado for diferente
        de None, significa que a consulta retornou uma linha com o ID do usuário. Nesse caso, a função retorna o
        ID do usuário encontrado (resultado[0]). Caso contrário, ou seja, se o resultado for None, significa que
        o usuário não foi encontrado no banco de dados e a função retorna None.

        Parameters
        ----------
        username : str
            O nome de usuário do usuário.

        Returns
        -------
        int or None
            O ID do usuário, ou None se o usuário não existir.
        """

        self.cursor.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return None
        
    def get_id_do_jogo(self, jogo):
        """
        Obtém o ID de um jogo a partir do nome do jogo.

        Essa fução é responsável por obter o ID de um jogo a partir do seu nome.
        A função executa uma consulta na tabela jogos do banco de dados, filtrando pelo nome do jogo fornecido. 
        Se o resultado for diferente de None, significa que a consulta retornou uma linha com o ID do jogo. 
        Nesse caso, a função retorna o ID do jogo encontrado (result[0]). Caso contrário, ou seja, se o resultado
        for None, significa que o jogo não foi encontrado no banco de dados e a função retorna None. Em caso de
        erro na execução da consulta, a função trata a exceção mysql.connector.Error exibindo uma mensagem de
        erro e retorna None.

        Parameters
        ----------
        jogo : str
            O nome do jogo.

        Returns
        -------
        int or None
            O ID do jogo, ou None se o jogo não existir.
        """

        try:
            self.cursor.execute("SELECT id FROM jogos WHERE nome = %s", (jogo,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except mysql.connector.Error as erro:
            print("Erro ao obter ID do jogo:", erro)
            return None

    def obter_reviews(self, jogo_id):
        """
        Obtém as reviews de um jogo específico.

        Essa função é responsável por obter as reviews de um jogo específico.
        Ela recebe como parâmetro o jogo_id, que é o ID do jogo do qual se deseja obter as reviews.
        A função executa uma consulta que combina as tabelas reviews e usuarios usando a cláusula JOIN,
        unindo-as com base no ID do usuário. A consulta seleciona as colunas texto_review, username e
        data_criacao da tabela reviews para o jogo específico identificado pelo jogo_id. Se a consulta
        for executada com sucesso, a função retorna a lista de reviews encontradas, no formato de uma
        lista de tuplas [(texto_review, username, data_criacao), ...]. Caso ocorra algum erro na execução
        da consulta, a função trata a exceção mysql.connector.Error, exibe uma mensagem de erro e retorna
        uma lista vazia.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo.

        Returns
        -------
        list
            A lista de reviews no formato [(texto_review, username, data_criacao), ...].
        """

        try:
            self.cursor.execute("""
                SELECT r.texto_review, u.username, r.data_criacao
                FROM reviews r
                JOIN usuarios u ON r.usuario_id = u.id
                WHERE r.jogo_id = %s
            """, (jogo_id,))
            reviews = self.cursor.fetchall()
            return reviews
        except mysql.Error as erro:
            print("Erro ao obter reviews:", erro)

    def obter_ultimas_reviews_usuario(self, usuario_id, num_reviews):
        """
        Obtém as últimas reviews feitas por um usuário.
        
        Essa função é responsável por obter as reviews de um jogo específico.
        A função executa uma consulta na tabela reviews e usuarios do banco de dados, utilizando um join 
        para relacionar as informações das reviews com os usuários correspondentes. A consulta é filtrada
        pelo jogo_id fornecido.
        Se houverem reviews para o jogo especificado, a função retorna a lista de reviews no formato
        [(texto_review, username, data_criacao), ...]. Caso ocorra algum erro na execução da consulta,
        a função trata a exceção mysql.connector.Error, exibe uma mensagem de erro e retorna uma lista vazia [].

        Parameters
        ----------
        num_reviews : int
            O número de reviews a serem retornadas.

        Returns
        -------
        list
            A lista das últimas reviews no formato [(texto_review, nome_jogo), ...].
        """

        try:
            self.cursor.execute("""
                SELECT r.texto_review, j.nome
                FROM reviews r
                JOIN jogos j ON r.jogo_id = j.id
                WHERE r.usuario_id = %s
                ORDER BY r.data_criacao DESC
                LIMIT %s
            """, (usuario_id, num_reviews))
            reviews = self.cursor.fetchall()
            return reviews
        except mysql.Error as err:
            print(f"Erro ao obter as últimas reviews do usuário: {err}")
            return None
        
    def adicionar_jogo(self, nome, desenvolvedor, distribuidora, ano_lancamento, descricao):
        """
        Adiciona um novo jogo ao banco de dados.

        A função adicionar_jogo é responsável por adicionar um novo jogo ao banco de dados.
        Ela recebe como parâmetros o nome, desenvolvedor, distribuidora, ano_lancamento e descricao do jogo.
        A função verifica se todos os campos são não vazios (nome, desenvolvedor, distribuidora, ano_lancamento
        e descricao) antes de executar a inserção no banco de dados. Caso algum campo esteja vazio, a função
        retorna False. Se todos os campos estiverem preenchidos, a função executa uma instrução INSERT na
        tabela jogos, inserindo os valores fornecidos como parâmetros. Em seguida, a função faz o commit da
        transação para efetivar a inserção. Se a inserção for realizada com sucesso, a função retorna True.
        Caso contrário, trata a exceção mysql.connector.Error, exibe uma mensagem de erro e retorna False.

        Parameters
        ----------
        nome : str
            O nome do jogo.
        desenvolvedor : str
            O desenvolvedor do jogo.
        distribuidora : str
            A distribuidora do jogo.
        ano_lancamento : str
            O ano de lançamento do jogo.
        descricao : str
            A descrição do jogo.

        Returns
        -------
        bool
            True se o jogo foi adicionado com sucesso, False caso contrário.
        """

        if nome and desenvolvedor and distribuidora and ano_lancamento and descricao:
            self.cursor.execute(
                "INSERT INTO jogos (nome, desenvolvedor, distribuidora, ano_lancamento, descricao) VALUES (%s, %s, %s, %s, %s)",
                (nome, desenvolvedor, distribuidora, ano_lancamento, descricao))
            self.conexao.commit()
            return True
        else:
            return False
        
    
    def carregar_jogos_adm(self):
        """
        Carrega a lista de jogos para o administrador.

        Essa função é responsável por adicionar um novo jogo ao banco de dados.
        Ela recebe como parâmetros o nome, desenvolvedor, distribuidora, ano_lancamento e descricao do jogo.
        A função verifica se todos os parâmetros possuem valores não vazios. Em seguida, executa uma consulta
        de inserção na tabela jogos, inserindo os valores fornecidos. Se a consulta for executada com sucesso,
        a função realiza o commit da transação e retorna True, indicando que o jogo foi adicionado com sucesso.
        Caso ocorra algum erro na execução da consulta, a função trata a exceção mysql.connector.Error, exibe
        uma mensagem de erro, desfaz a transação e retorna False. Se algum dos parâmetros estiver vazio, a função
        retorna False.

        Returns
        -------
        list
            A lista de jogos no formato [(id, nome, ano_lancamento), ...].
        """

        self.cursor.execute("SELECT id, nome, ano_lancamento FROM jogos")
        resultados = self.cursor.fetchall()

        return resultados
    
    def excluir_jogo(self, jogo_id):
        """
        Exclui um jogo do banco de dados.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo a ser excluído.

        Returns
        -------
        bool
            True se o jogo foi excluído com sucesso, False caso contrário.
        """
        try:
            sql = "DELETE FROM jogos WHERE id = " + str(jogo_id)
            self.cursor.execute(sql)
            self.conexao.commit()

            if self.cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Erro ao excluir o jogo do banco de dados: {e}")
            return False
        
    def pesquisar_jogos(self, filtro, pesquisa):
        """
        Pesquisa os jogos de acordo com os filtros selecionados.

        Parameters
        ----------
        filtro : str
            O filtro selecionado (ex: "Nome", "Desenvolvedora", "Distribuidora", "Ano de Lançamento").
        pesquisa : str
            O termo de pesquisa.

        Returns
        -------
        list
            A lista de jogos correspondente à pesquisa.
        """
        try:
            if filtro == "Todos":
                sql = "SELECT id, nome, ano_lancamento FROM jogos"
            else:
                filtro_column = ""
                if filtro == "Nome":
                    filtro_column = "nome"
                elif filtro == "Desenvolvedora":
                    filtro_column = "desenvolvedor"
                elif filtro == "Distribuidora":
                    filtro_column = "distribuidora"
                elif filtro == "Ano de Lançamento":
                    filtro_column = "ano_lancamento"
                
                sql = f"SELECT id, nome, ano_lancamento FROM jogos WHERE {filtro_column} LIKE '%{pesquisa}%'"

            self.cursor.execute(sql)
            jogos = self.cursor.fetchall()
            
            jogos_formatted = []
            for jogo in jogos:
                jogo_id = jogo[0]
                nome = jogo[1]
                ano_lancamento = jogo[2]
                jogos_formatted.append(f"{jogo_id} | {nome} ({ano_lancamento})")

            return jogos_formatted
        except Exception as e:
            print(f"Erro ao pesquisar jogos: {e}")
            return []

