#importar
import ttkbootstrap as ttk
import sqlite3
import tkinter.messagebox as message


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
        self.button_inserir = ttk.Button(self.frame_button,text="Inserir",command= self.adicionar)
        self.button_inserir.pack(side="left", padx=10, pady=10)

        #alterar
        self.button_alterar = ttk.Button(self.frame_button, text="Alterar")
        self.button_alterar.pack(side="left", padx=10, pady=10)

        #exluir
        self.button_excluir = ttk.Button(self.frame_button, text="Excluir")
        self.button_excluir.pack(side="left", padx=10, pady=10)

        #faz com que execute a tabela assim que iniciar o programa
        self.criando_tabela()


###############################################################################################################
        #criando a tabela
        self.treeview = ttk.Treeview(self.janela)
        self.treeview.pack()

        #definir as colunas
        self.treeview["columns"] = ("titulo", "plataforma", "genero", "status")
        #diz para mostrar as colunas, e nomeia elas
        self.treeview["show"] = "headings"
        self.treeview.heading("titulo", text="titulo")
        self.treeview.heading("plataforma", text="plataforma")
        self.treeview.heading("genero", text="genero")
        self.treeview.heading("status", text="status")

        self.atualizar()
#############################################################################################################
#começando a inserir banco de dados
    def criando_tabela(self):
        conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
        cursor = conexao.cursor()

            
        #criar tabela
        sql_criar_tabela = """
                                    CREATE TABLE IF NOT EXISTS biblioteca_jogos (
                                    titulo varchar(200) primary key, 
                                    plataforma varchar(200),
                                    genero varchar(200),
                                    status varcha(200) 
                                    
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
    def adicionar(self):
        try:
            conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
            cursor = conexao.cursor()
            
            #para pegar oq tem dentro da caixa de texto
            self.titulo = self.entry_titulo.get()
            self.plataforma = self.entry_plataforma.get()
            self.genero = self.entry_genero.get()
            self.status = self.entry_status.get()
            #limpando as caixas 
            self.entry_titulo.delete(0,ttk.END)
            self.entry_plataforma.delete(0,ttk.END)
            self.entry_genero.delete(0, ttk.END)
            self.entry_status.delete(0,ttk.END)
    
     #banoc de dados
            self.inserir = """
                                INSERT INTO biblioteca_jogos (titulo, plataforma, genero, status)
                                    VALUES (?, ?, ?, ?);
                                """
            cursor.execute(self.inserir, [self.titulo, self.plataforma, self.genero, self.status])
            
            conexao.commit()
            self.atualizar()
            message.showwarning(message="Informações inseridas com sucesso!")
        except:

            message.showerror(message="Erro ao inserir, favor preencher todos os dados")


        finally:
        #para fechar o cursor
            cursor.close()
            conexao.close()
#########################################################################################################
    def atualizar(self):
        conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
        cursor = conexao.cursor()
        # função self.treeview.get_children() 
        # é a única função nativa que retorna essa lista de iids que está na raiz.
        self.treeview.delete(*self.treeview.get_children())
            
           
        self.select = """
                        SELECT titulo, plataforma, genero, status 
                        FROM biblioteca_jogos
                    """
        cursor.execute(self.select)
        atualizando = cursor.fetchall()
        conexao.close()

        for linha in atualizando:
            self.treeview.insert("", "end", values= linha)
            
#########################################################################################################3#
#e
    def excluir(self):
        
        self.selecionado = self.titulo.selection()  # pega o índice do item selecionado
        if self.selecionado:
            indice = self.selecionado[0]
            texto = self.titulo.get(indice)

        conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
        cursor = conexao.cursor()
  
       






#rodado a janela 
    def run(self):
      self.janela.mainloop()

if __name__ == "__main__":
    app = Tabela_gerenciar()
    app.run()


