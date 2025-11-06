#importar
import tkinter as tk
import ttkbootstrap as ttk
import sqlite3
import tkinter.messagebox as message
#eles nao podem ter o mesmo nome, por isso o meu tava dando erro
#Constantes (END, LEFT, RIGHT) → tk
#Widgets → ttkbootstrap se quiser o estilo moderno


class Tabela_gerenciar():
    def __init__(self):
        
        #criando a janela
        self.janela = ttk.Window(themename="superhero")
    
        self.label_titulo_inicial = ttk.Label(text="Biblioteca de Jogos de Vídeo", 
                                              font=("Helvetica", 20, "bold"))
        self.label_titulo_inicial.pack()
        self.criando_tabela()

        #Criando o notebook(que é o gerenciador das janelas.)
        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")
        
        #Cria as abas que eu quero
        self.aba_jogos = ttk.Frame(self.notebook) #Aba jogos(que é a que esta feita)
        self.aba_estatisticas = ttk.Frame(self.notebook) #aba "Estatísticas"(do desafio bonus)
        
        #Aqui ele vai tonar as abas que eu criei cliaveis. para quando clicar em uma delas a opção mudar
        self.notebook.add(self.aba_jogos, text='Jogos')
        self.notebook.add(self.aba_estatisticas, text='Estatísticas')
        
        #Monta o layout da aba de esttisticas
        self.criar_aba_estatisticas(self.aba_estatisticas)
        
        #liga um "sensor" para mudar de aba.
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)
      
#############################################################################################################
        #caixas de texto para inserir informações
        #As informações que vão ficar dentro da aba de jogos tem que adicionar o self.aba_jogos
        #para que as informações dos jogos fiquem apenas na janela de jogos.
        #titulo
        self.label_titulo = ttk.Label(self.aba_jogos, text="Titulo")
        self.label_titulo.pack()
        self.entry_titulo = ttk.Entry(self.aba_jogos, width=90)
        self.entry_titulo.pack(pady=5)

        #plataforma
        self.label_plataforma = ttk.Label(self.aba_jogos, text="Plataforma")
        self.label_plataforma.pack()
        self.entry_plataforma = ttk.Entry(self.aba_jogos, width=90)
        self.entry_plataforma.pack(pady=10)

        #genero
        self.label_genero = ttk.Label(self.aba_jogos, text="Genero")
        self.label_genero.pack()
        self.entry_genero = ttk.Entry(self.aba_jogos, width=90)
        self.entry_genero.pack(pady=10)

        #status
        self.label_status = ttk.Label(self.aba_jogos,text="Status")
        self.label_status.pack()
        self.entry_status = ttk.Entry(self.aba_jogos,width=90)
        self.entry_status.pack(pady=10)

        self.frame_button = ttk.Frame(self.aba_jogos)
        self.frame_button.pack(pady=5)

##############################################################################################################
#criando os botoes de inserir, excluir e alterar(apenas o layout)
        #inserir
        self.button_inserir = ttk.Button(self.frame_button,text="Inserir",command= self.adicionar)
        self.button_inserir.pack(side="left", padx=10, pady=10)

        #alterar
        self.button_alterar = ttk.Button(self.frame_button, text="Alterar", command= self.alterar)
        self.button_alterar.pack(side="left", padx=10, pady=10)

        #exluir
        self.button_excluir = ttk.Button(self.frame_button, text="Excluir", command=self.excluir)
        self.button_excluir.pack(side="left", padx=10, pady=10)

        self.button_atualizar = ttk.Button(self.frame_button, text="Atualizar alterações", command= self.salvar_alteracao)
        self.button_atualizar.pack(side="left", padx=10, pady=10)
        #faz com que execute a tabela assim que iniciar o programa
       


###############################################################################################################
        #criando a tabela
        self.treeview = ttk.Treeview(self.aba_jogos)
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
########################################################################################################################################################
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
                                    status varchar(200) 
                                    
                                    );
                                    """
        #para executar a tabela
        cursor.execute(sql_criar_tabela)
        conexao.commit()


    #para fechar o cursor
        cursor.close()
        conexao.close()
########################################################################################################################################################
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
            self.entry_titulo.delete(0,tk.END)
            self.entry_plataforma.delete(0,tk.END)
            self.entry_genero.delete(0, tk.END)
            self.entry_status.delete(0,tk.END)
    
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
            if self.inserir == None:
                message.showerror(message="Erro ao inserir, favor preencher todos os dados")


        finally:
        #para fechar o cursor
            cursor.close()
            conexao.close()
########################################################################################################################################################
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
            
#######################################################################################################################################################
    def excluir(self):
        selecionado = self.treeview.selection()
        #selecionando qual vai ser a linha que vai ser excluida
        if selecionado:
            indice = selecionado[0]
            valores = self.treeview.item(indice, "values")
            self.titulo = valores[0] #o título é a primeira coluna

            #conectando sqlite
            conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
            cursor = conexao.cursor()

            # Exclui do banco de dados, estou excluindo pela primary key
            cursor.execute("DELETE FROM biblioteca_jogos WHERE titulo = ?", (self.titulo,))

            conexao.commit()
            cursor.close()
            conexao.close()

            # Exclui da Treeview 
            self.treeview.delete(indice)

        else:
            message.showerror(message="Selecione o item que quer excluir")
#######################################################################################################################################################
#def para alterar 
    def alterar(self):
        selec_alterar = self.treeview.selection()
        if selec_alterar:
            indice = selec_alterar[0]
            valores = self.treeview.item(indice, "values")

            # guarda o título original (chave primária)
            self.titulo_original = valores[0]

            # limpa os entrys antes de preencher
            self.entry_titulo.delete(0, tk.END)
            self.entry_plataforma.delete(0, tk.END)
            self.entry_genero.delete(0, tk.END)
            self.entry_status.delete(0, tk.END)

            # coloca os valores da linha selecionada nos entrys
            self.entry_titulo.insert(0, valores[0])
            self.entry_plataforma.insert(0, valores[1])
            self.entry_genero.insert(0, valores[2])
            self.entry_status.insert(0, valores[3])
        else:
            message.showerror("Erro", "Selecione um item para alterar.")

#######################################################################################################################################################
    def salvar_alteracao(self):
        try:
            #pondo as novas alterações
            novo_titulo = self.entry_titulo.get().strip()
            nova_plataforma = self.entry_plataforma.get().strip()
            novo_genero = self.entry_genero.get().strip()
            novo_status = self.entry_status.get().strip()

            

            conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
            cursor = conexao.cursor()
            #pondo as novas alterações
            cursor.execute("""
                UPDATE biblioteca_jogos
                SET titulo = ?, plataforma = ?, genero = ?, status = ?
                WHERE titulo = ?
            """, (novo_titulo, nova_plataforma, novo_genero, novo_status, self.titulo_original))

            conexao.commit()
            cursor.close()
            conexao.close()

            # Atualiza visualmente a tabela
            self.atualizar()

            message.showinfo("Sucesso", "Alterações salvas com sucesso!")

        except AttributeError:
            message.showerror("Erro", "Você precisa primeiro clicar em 'Alterar' para escolher o item a editar.")
#######################################################################################################################################################
#ESTATISTICAS
    def criar_aba_estatisticas(self):
        self.label_contagem = ttk.Label(self.aba_estatisticas, text="")
        self.label_contagem.pack()
   
######################################################################################################################################################
    def total(self):
        conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
        cursor = conexao.cursor()

        cursor.execute("SELECT COUNT(titulo) FROM biblioteca_jogos")
        qtd = cursor.fetchone()[0]
        return qtd  # só retorna o número
    
########################################################################################################################################################

    def total_jogados(self):
        conexao = sqlite3.connect("Biblioteca_jogos/bd_tabela_jogos.sqlite")
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(titulo) FROM biblioteca_jogos WHERE status='Jogado'")
        qtd = cursor.fetchone()[0]
        conexao.close()
        return qtd

######################################################################################################################################################
    def atualizar_jogados(self):
        total = self.total()
        jogados = self.total_jogados()

        # evita erro de divisão por zero
        if total > 0:
            porcentagem = (jogados / total) * 100
        else:
            porcentagem = 0
        self.label_contagem.config(text=f"Total de jogos: {total}\nPorcentagem: {total_jogados:.2f}%")


##############################################################################################################

############################################################################################################


    def on_tab_change(self, event):
        aba_selecionada = event.widget.tab('current')['text']

        if aba_selecionada == "Estatísticas":
            self.atualizar_estatisticas()

        elif aba_selecionada == "Jogos":
            self.atualizar()
    #################################################################################################################################################

#rodado a janela 
    def run(self):
      self.janela.mainloop()

if __name__ == "__main__":
    app = Tabela_gerenciar()
    app.run()


