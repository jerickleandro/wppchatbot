from tkinter import *

class Gui():
    """Classe que define a interface gráfica da aplicação
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30


    #Criando a janela...
    window          = Tk()
    window.wm_title("Cadastro de pedidos")


    #Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtNome         = StringVar()
    txtTamanho      = StringVar()
    txtSabor1       = StringVar()
    txtSabor2       = StringVar()
    txtSabor3       = StringVar()
    txtRefri        = StringVar()
    txtBorda        = StringVar()
    txtEndereco     = StringVar()
    
    #Criando os objetos que estarão na janela...
    lblnome      = Label(window, text="Nome")
    lbltamanho   = Label(window, text="Tamanho")
    lblsabor1    = Label(window, text="Sabor1")
    lblsabor2    = Label(window, text="Sabor3")
    lblsabor3    = Label(window, text="Sabor2")
    lblrefri     = Label(window, text="Refri")
    lblborda     = Label(window, text="Borda")
    lblendereco  = Label(window, text="Endereco")
    
    
    entNome      = Entry(window, textvariable=txtNome, width=width_entry)
    entTamanho   = Entry(window, textvariable=txtTamanho, width=width_entry)
    entSabor1    = Entry(window, textvariable=txtSabor1, width=width_entry)
    entSabor2    = Entry(window, textvariable=txtSabor2, width=width_entry)
    entSabor3    = Entry(window, textvariable=txtSabor3, width=width_entry)
    entRefri     = Entry(window, textvariable=txtRefri, width=width_entry)
    entBorda     = Entry(window, textvariable=txtBorda, width=width_entry)
    entEndereco  = Entry(window, textvariable=txtEndereco, width=width_entry)
    
    listPedidos    = Listbox(window, width=100)
    scrollPedidos  = Scrollbar(window)
    btnViewAll     = Button(window, text="Ver todos")
    btnBuscar      = Button(window, text="Buscar")
    btnInserir     = Button(window, text="Inserir")
    btnUpdate      = Button(window, text="Atualizar Selecionados")
    btnDel         = Button(window, text="Deletar Selecionados")
    btnClose       = Button(window, text="Fechar")


    #Associando os objetos a grid da janela...
    lblnome.grid(row=0,column=0)
    lbltamanho.grid(row=1,column=0)
    lblsabor1.grid(row=2,column=0)
    lblsabor2.grid(row=3, column=0)
    lblsabor3.grid(row=4,column=0)
    lblrefri.grid(row=5,column=0)
    lblborda.grid(row=6,column=0)
    lblendereco.grid(row=7, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entTamanho.grid(row=1, column=1)
    entSabor1.grid(row=2, column=1)
    entSabor2.grid(row=3, column=1, padx=50, pady=50)
    entSabor3.grid(row=4, column=1)
    entRefri.grid(row=5, column=1)
    entBorda.grid(row=6, column=1)
    entEndereco.grid(row=7, column=1)
    listPedidos.grid(row=0, column=2, rowspan=10)
    scrollPedidos.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=8, column=0, columnspan=2)
    btnBuscar.grid(row=9, column=0, columnspan=2)
    btnInserir.grid(row=10, column=0, columnspan=2)
    btnUpdate.grid(row=11, column=0, columnspan=2)
    btnDel.grid(row=12, column=0, columnspan=2)
    btnClose.grid(row=13, column=0, columnspan=2)



    #Associando a Scrollbar com a Listbox...
    listPedidos.configure(yscrollcommand=scrollPedidos.set)
    scrollPedidos.configure(command=listPedidos.yview)


    #Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')




    def run(self):
        Gui.window.mainloop()