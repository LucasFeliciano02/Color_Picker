from tkinter import *
import tkinter.messagebox


# cores
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#004338"


# Janela
janela = Tk()
janela.title('Color Picker')
janela.geometry('530x205')
janela.configure(bg=cor1)
janela.iconbitmap('color_picker.ico')  # icon do app


# ------ Funções -------

def escala(valor):
    r = scale_red.get()
    g = scale_green.get()
    b = scale_blue.get()
    
    rgb = f'{r}, {g}, {b}'
    
    hexadecimal = "#%02x%02x%02x" % (r, g, b)  
    
    tela['bg'] = hexadecimal  # Altera a cor do fundo da tela
    
    # Altera a entry
    entry_cor.delete(0, END)
    entry_cor.insert(0, hexadecimal)
    
    
# função clicar

def onClick():  
    tkinter.messagebox.showinfo('Sucesso', 'A cor foi copiada!')
    
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(entry_cor.get())
    clip.destroy()


# Criando a tela e frames

tela = Label(janela, bg=cor0, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0, column=1, padx=5)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)


# Configurando o frame_Direita com as opções 'RGB'

label_red = Label(frame_direita, text='Red', width=7, bg=cor1, fg='red', anchor='nw', font=('Time New Roman', 12, 'bold'))
label_red.grid(row=0, column=0)

scale_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='red', orient=HORIZONTAL)
scale_red.grid(row=0, column=1)


label_green = Label(frame_direita, text='Green', width=7, bg=cor1, fg='green', anchor='nw', font=('Time New Roman', 12, 'bold'))
label_green.grid(row=1, column=0)

scale_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
scale_green.grid(row=1, column=1)


label_blue = Label(frame_direita, text='blue', width=7, bg=cor1, fg='blue', anchor='nw', font=('Time New Roman', 12, 'bold'))
label_blue.grid(row=2, column=0)

scale_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
scale_blue.grid(row=2, column=1)


# -------- Configurando o frame_Baixo ----------

label_rgb = Label(frame_baixo, text='CÓDIGO HEX:', bg=cor1, font=('Ivy', 10, 'bold'))
label_rgb.grid(row=0, column=0, padx=5)


# Entrys

entry_cor = Entry(frame_baixo, width=12, font=('Ivy', 10, 'bold'), justify=CENTER)
entry_cor.grid(row=0, column=1, padx=5)


# Botao Copiar

botao_copiar = Button(frame_baixo, command=onClick, text='Copiar a cor', bg=cor1, font=('Ivy', 8, 'bold'), relief=RAISED, overrelief=RIDGE)
botao_copiar.grid(row=0, column=2, padx=5)


# App nome

label_app_nome = Label(frame_baixo, text='Seletor de Cores', bg=cor1, font=('Ivy', 15, 'bold'))
label_app_nome.grid(row=0, column=3, padx=40)


janela.mainloop()
