#INTERFACE GRAFICA (NAO RODA NO CODESPACE, APENAS LOCAL)

from tkinter import messagebox, Tk, Label, Entry, Button

def show_nome():
    lbl_resultado.config(text =  lbl_resultado.cget('text') + txt_nome.get() + '\n')
    messagebox.showinfo(
        title='Seja bem vindo!',
        message=f'Olá {txt_nome.get()}!'
    )

janela = Tk()
janela.title('Janela')
janela.config(padx=10, pady=50, background='turquoise')

lbl_nome = Label(text='Nome:', background='turquoise')
lbl_nome.grid(row=0,column=0)
lbl_resultado = Label(text='', background='turquoise')
lbl_resultado.grid(row=5, column=0, columnspan=3, sticky='W')


txt_nome = Entry(width=40)
txt_nome.grid(row=0,column=1,columnspan=2,sticky='W')
txt_nome.focus()
btn_ok =Button(text='OK', width=20, command=show_nome)
btn_ok.grid(row=3,column=0,columnspan=3, pady=10)

janela.mainloop()