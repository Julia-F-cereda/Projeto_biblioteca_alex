#importar
import ttkbootstrap as ttk
import sqlite3


class Tabela_gerenciar():
    def __init__(self):
        #criando a janela
        self.janela = ttk.Window(themename="vapor")

        self.label_titulo_inicial = ttk.Label(text="Biblioteca de Jogos de Vídeo")
        self.label_titulo_inicial.pack()
      
#############################################################################################################
        #caixas de texto para inserir informações
        #titulo
        self.label_titulo = ttk.Label(text="Titulo")
        self.label_titulo.pack()
        self.entry_titulo = ttk.Entry(width=90)
        self.entry_titulo.pack(pady=5)

        #plataforma
        self.label_plataforma = ttk.Label(text="Plataforma")
        self.label_plataforma.pack()
        self.entry_plataforma = ttk.Entry(width=90)
        self.entry_plataforma.pack(pady=10)

        #genero
        self.label_genero = ttk.Label(text="Genero")
        self.label_genero.pack()
        self.entry_genero = ttk.Entry(width=90)
        self.entry_genero.pack(pady=10)

        #status
        self.label_status = ttk.Label(text="Status")
        self.label_status.pack()
        self.entry_status = ttk.Entry(width=90)
        self.entry_status.pack(pady=10)

        self.frame_button = ttk.Frame(self.janela)
        self.frame_button.pack(pady=5)

##############################################################################################################
#criando os botoes de inserir, excluir e alterar(apenas o layout)
        #inserir
        self.button_inserir = ttk.Button(self.frame_button, text="Inserir")
        self.button_inserir.pack(side="left", padx=10, pady=10)

        #alterar
        self.button_alterar = ttk.Button(self.frame_button, text="Alterar")
        self.button_alterar.pack(side="left", padx=10, pady=10)

        #exluir
        self.button_excluir = ttk.Button(self.frame_button, text="Excluir")
        self.button_excluir.pack(side="left", padx=10, pady=10)


###############################################################################################################
        #criando a tabela
        treeview = ttk.Treeview(self.janela)
        treeview.pack()

        #definir as colunas
        treeview["columns"] = ("titulo", "plataforma", "genero", "status")
        #diz para mostrar as colunas, e nomeia elas
        treeview["show"] = "headings"
        treeview.heading("titulo", text="titulo")
        treeview.heading("plataforma", text="plataforma")
        treeview.heading("genero", text="genero")
        treeview.heading("status", text="status")
#############################################################################################################
#começando a inserir banco de dados
    conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
    cursor = conexao.cursor()

        
    #criar tabela
    sql_criar_tabela = """
                                CREATE TABLE IF NOT EXISTS biblioteca_jogos (
                                titulo integer primary key autoincrement, 
                                plataforma varchar(200),
                                genero varchar(200),
                                status integer default 0
                                
                                );
                                """
    #para executar a tabela
    cursor.execute(sql_criar_tabela)
    conexao.commit()


    #para fechar o cursor
    cursor.close()
    conexao.close()
##########################################################################################################
#criando adicionar tarefa

    conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
    cursor = conexao.cursor()

    sql_adicionar_tarefa = """
                        INSERT INTO biblioteca_jogos (titulo, plataforma, genero, status)
                                                VALUES (?, ?, ?, ?)
                                                );
                                                        """


    #para fechar o cursor
    cursor.close()
    conexao.close()




    

#rodado a janela 
    def run(self):
      self.janela.mainloop()

if __name__ == "__main__":
    app = Tabela_gerenciar()
    app.run()


