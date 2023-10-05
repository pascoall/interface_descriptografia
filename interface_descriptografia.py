from tkinter import*
from cryptography.fernet import Fernet

    

#Função para descriptografar
def descript():
    mensagem = "ola"
    #Gera uma chave de criptografia  
    key = Fernet.generate_key() 
                        
    #Instancia a classe Fernet com a chave de criptografia 
    fernet = Fernet(key) 
    #Criptografa a string com a instância Fernet 
    encMensagem = fernet.encrypt(mensagem.encode()) 
    
    descMensagem = fernet.decrypt(encMensagem).decode() 

    #Mostra a mensagem descriptografada   
    print("Mensagem descriptografada: ", descMensagem)

#Variavel que da inicio a criação da janela
janela = Tk()



#Especificaçõs da janela
janela.geometry("300x700")
janela.title("Descriptografia")
janela.config(bg="lightblue")

#orientacao = Label(janela, text="Digite o texto criptografado")
#orientacao.grid(column=3,row=3)

#Especificações da primeira barra
Entrada1 = Entry(janela,)
#Local onde a barra vai aparecer
Entrada1.place(relx=.1, rely=0.05,relheight=.025,relwidth=.8)

#Especificações da segunda barra
Entrada2 = Entry(janela,)
#Local onde a barra vai aparecer
Entrada2.place(relx=.1, rely=0.17,relheight=.025,relwidth=.8)

#Criando o botão e suas caracteristicas
botao = Button(janela, text="Descriptografar",foreground="white",bg="green",command = descript)
#Local onde o botão vai aparecer
botao.place(relx=0.1, rely=0.10)


#Variavel que permite que a janela fique aberta
janela.mainloop()
