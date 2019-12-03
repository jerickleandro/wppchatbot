import wppbot
import time
import re
bot = wppbot.wppbot('Robot')
import os.path
from gui import *
import bd as core

app = None

def saudacao(primeiraVez):
    global nome
    if(primeiraVez==True):
        resposta = 'Olá, digite seu nome:'
        print(resposta)
        bot.responde(resposta)
        texto = escuta_resposta(resposta)
        print(texto)
    while(True):
        if(primeiraVez==True):
            nome = texto
            print(nome)
            arquivo = '{}.txt'.format(nome)
            print(arquivo)
            caminho = os.getcwd()
            print(caminho)
            verifica = caminho+'/'+arquivo
            print(verifica)
            check = os.path.exists(verifica)
            print(check)
            if check:
                resposta = 'Bom te ver de volta {}, digite o numero referente a opção desejada:'.format(nome)

            else:
                cria = open (arquivo, 'a')
                cria.write('novo')
                cria.close()
                resposta = '{}, digite o numero referente a opção desejada:'.format(nome)
            
        else:
            resposta = 'Digite o numero referente a opção desejada:'
        bot.responde(resposta)
        
        resposta = '(1) - Novo pedido\n(2) - Alteração de pedido\n(3) - Mais opções'             
        bot.responde(resposta)
        op = escuta_resposta('(3) - Mais opções')
        
        if(op == '1'):
            return novo_pedido()
        elif(op == '2'):
            return alteracao_pedido()
        elif (op == '3'):
            return mais_opcoes()
        else:
            print('Essa opção não existe')
            saudacao(False)


def novo_pedido():
    """Realiza todo o tratamento de um novo pedido"""

    global tamanho

    # Tratamento de decisoes no pedido
    while(True):
        resposta = 'Qual o tamanho da sua pizza?\n(1).  PEQUENA\n(2).  MÉDIA\n(3).  GRANDE'
        bot.responde(resposta)
        option = escuta_resposta('(3).  GRANDE')
        if option.isnumeric():
            option = int(option)
            if option == 1:
                return um_sabor(option)

            elif option == 2:
                resposta = 'Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores'
                bot.responde(resposta)
                opt_sabor = escuta_resposta('(2) 2 Sabores')
                if opt_sabor == 1:
                    return um_sabor(option)
                else:
                    return dois_sabores(option)

            elif option == 3:
                resposta = 'Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores\n(3) 3 Sabores'
                bot.responde(resposta)
                opt_sabor = escuta_resposta('(3) 3 Sabores')
                
                if option == 1:
                    return um_sabor(option)
                elif option == 2:
                    return dois_sabores(option)
                elif option == 3:
                    return tres_sabores()
        elif option.isalpha():
            option = option.upper()
            if option == 'PEQUENA':
                return um_sabor(option)

            elif option == 'MEDIA':
                resposta = 'Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores'
                bot.responde(resposta)
                opt_sabor = escuta_resposta('(2) 2 Sabores')
                if opt_sabor == 1:
                    return um_sabor(option)
                else:
                    return dois_sabores(option)

            elif option == 'GRANDE':
                resposta = 'Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores\n(3) 3 Sabores'
                bot.responde(resposta)
                opt_sabor = escuta_resposta('(3) 3 Sabores')
                
                if option == 1:
                    return um_sabor(option)
                elif option == 2:
                    return dois_sabores(option)
                elif option == 3:
                    return tres_sabores()


def alteracao_pedido():
    global tamanho
    global sabores
    print('O que você deseja alterar?\nDigite o numero referente a opção desejada')

    print('(1) - Alterar tamanho')
    print('(2) - Alterar sabores')
    print('(3) - Alterar extras')
    op = input()
    if(op == '1'):
        return alterar_tamanho()
    elif(op == '2'):
        return alterar_sabores(tamanho)
    elif(op == '3'):
        return alterar_extras()
    else:
        print('Essa opção não existe')
        alteracao_pedido()


def alterar_tamanho():
    global tamanho
    print('Para qual tamanho deseja alterar? Digite a opção desejada:')
    print('1 - Pequena\n2 - Média\n3 - Grande')
    op = input()
    if(op == '1'):
        tamanho = 'Pequena'
        return
    elif(op == '2'):
        tamanho = 'Media'
        return
    elif(op == '3'):
        tamanho = 'Grande'
        return
    else:
        print('Essa opção não existe')
        alterar_tamanho()


def alterar_sabores(tamanho):
    global menu
    global sabores
    if tamanho == 'Pequena':
        show_cardapio()
        print('Escolha o numero referente a novo sabor:')
        while(True):
            sabor = input()
            escolha = int(sabor)
            if escolha in menu:
                sabores[0] = sabor
                return
            else:
                print(
                    'Essa opção não está dentro das opções do menu. Escolha novamente:')
    elif tamanho == 'Media':
        if len(sabores) == 1:
            show_cardapio()
            print('Escolha o numero referente a novo sabor:')
            while(True):
                sabor = input()
                escolha = int(sabor)
                if escolha in menu:
                    sabores[0] = sabor
                    return
                else:
                    print(
                        'Essa opção não está dentro das opções do menu. Escolha novamente:')
        elif len(sabores) == 2:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois = int(sabores[1])
            print('(1) - {} '.format(menu[saborum]))
            print('(2) - {} '.format(menu[sabordois]))
            print('(3) - Os dois sabores')
            op = input()
            if(op == '1'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                i = 0
                while(i < 2):
                    show_cardapio()
                    print('Escolha seu {}º novo sabor'.format(i+1))

                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i += 1
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            else:
                print('Opção invalida')
                alterar_sabores(tamanho)
    elif tamanho == 'Grande':
        if len(sabores) == 1:
            print('Escolha o numero referente a novo sabor:')
            show_cardapio()
            while(True):
                sabor = input()
                escolha = int(sabor)
                if escolha in menu:
                    sabores.pop(0)
                    sabores.insert(0, sabor)
                    return
                else:
                    print(
                        'Essa opção não está dentro das opções do menu. Escolha novamente:')

        elif len(sabores) == 2:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois = int(sabores[1])
            print('(1) - {} '.format(menu[saborum]))
            print('(2) - {} '.format(menu[sabordois]))
            print('(3) - OS DOIS SABORES')
            op = input()
            if(op == '1'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                i = 0
                while(i < 2):
                    show_cardapio()
                    print('Escolha seu {}º novo sabor'.format(i+1))

                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i += 1

                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')

            else:
                print('Opção invalida')
                alterar_sabores(tamanho)
        elif len(sabores) == 3:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois = int(sabores[1])
            sabortres = int(sabores[2])
            print('(1) - {} '.format(menu[saborum]))
            print('(2) - {} '.format(menu[sabordois]))
            print('(3) - {} '.format(menu[sabortres]))
            print('(4) - OS TRÊS SABORES')
            op = input()
            if(op == '1'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[2] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '4'):
                i = 0
                while(i < 3):
                    show_cardapio()
                    print('Escolha seu {}º novo sabor'.format(i+1))

                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i += 1
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')

            else:
                print('Opção invalida')
                alterar_sabores(tamanho)


def mais_opcoes():
    resposta = 'Mais Opções'
    bot.responde(resposta)
    print('\n')
    while(True):
        bot.responde('digite o numero referente a opção desejada:')
        
        bot.responde('1 - Falar com Atendente Humana')
        bot.responde('2 - Voltar para as opções')
        op = int(escuta_resposta('2 - Voltar para as opções'))
        if(op == 1):
            bot.responde('Aguarde, a atendente humana entrará já falará com você.')
            return saudacao(False)
        elif(op == 2):
            return saudacao(False)
        else:
            bot.responde('Essa opção não é válida')
            return mais_opcoes()


def alterar_extras():
    return


def show_cardapio():

    time.sleep(5)
    bot.show_cardapio()
    time.sleep(5)



def um_sabor(option):
    """Escolha do sabor para apenas um sabor"""

    global tamanho

    if option == 1 or option == 'PEQUENA':
        tamanho = 'Pequena'
    elif option == 2 or option == 'MEDIA':
        tamanho = 'Media'
    elif option == 3 or option == 'GRANDE':
        tamanho = 'Grande'
    show_cardapio()
    while (True):
        bot.responde('Insira o numero referente ao sabor desejado:')
        sabor_0 = escuta_resposta('Insira o numero referente ao sabor desejado:')
        if sabor_0.isnumeric():
            escolha = int(sabor_0)
            if escolha in menu:
                sabores.append(sabor_0)
                break
        else:
            bot.responde('Ops! Digite apenas o número referente ao sabor:')
    return more_options()


def dois_sabores(option):
    """Escolha do sabor para duas opcoes"""

    global tamanho
    global sabores
    if option == 2:
        tamanho = 'Media'
    elif option == 3:
        tamanho = 'Grande'
    show_cardapio()
    flag = True
    while (flag):
        
        bot.responde('Insira o numero referente ao primeiro sabor desejado:')
        sabor_1 = escuta_resposta('Insira o numero referente ao primeiro sabor desejado:')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_1.isnumeric():
            escolha = int(sabor_1)
            if escolha in menu:
                sabores.append(sabor_1)    
            bot.responde('Insira o numero referente ao segundo sabor desejado:')
            sabor_2 = escuta_resposta('Insira o numero referente ao segundo sabor desejado:')
            # Validando se o valor do sabor_2 eh um numero para poder adicionar ao pedido
            if sabor_2.isnumeric():
                escolha = int(sabor_2)
                if escolha in menu:
                    sabores.append(sabor_2)
                    flag = False
            else:
                bot.responde('Ops! Digite apenas o número referente ao sabor:')
        else:
            bot.responde('Ops! Digite apenas o número referente ao sabor:')
        # Condicao de parada do loop
        # if len(sabores) == 2:
        #     more_options()
        #     return sabores
    return more_options()


def tres_sabores():
    """Escolha dos sabores para tres opcoes"""

    global tamanho
    tamanho = 'Grande'
    global sabores
    show_cardapio()
    flag = True
    while (flag):
        bot.responde('Insira o numero referente ao primeiro sabor desejado:')
        sabor_1 = escuta_resposta('Insira o numero referente ao primeiro sabor desejado:')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_1.isnumeric():
            escolha = int(sabor_1)
            if escolha in menu:
                sabores.append(sabor_1)
                
        

        bot.responde('Insira o numero referente ao segundo sabor desejado:')
        sabor_2 = escuta_resposta('Insira o numero referente ao segundo sabor desejado:')
            # Validando se o valor do sabor_2 eh um numero para poder adicionar ao pedido
        if sabor_2.isnumeric():
            escolha = int(sabor_2)
            if escolha in menu:
                sabores.append(sabor_2)
                
        else:
            bot.responde('Ops! Digite apenas o número referente ao sabor:')
        bot.responde('Insira o numero referente ao terceiro sabor desejado:')
        sabor_3 = escuta_resposta('Insira o numero referente ao terceiro sabor desejado:')
        
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_3.isnumeric():
            escolha = int(sabor_3)
            if escolha in menu:
                sabores.append(sabor_3)
                flag = False
                
        else:
            bot.responde('Ops! Digite apenas o número referente ao sabor:')
    return more_options()


def more_options():
    global borders
    global refrigerante
    global borda
    global refri
    
    bot.responde('Deseja adicionar borda?\n(1) SIM\n(2) NÃO')
    opt_border = int(escuta_resposta('(2) NÃO'))
    if opt_border == 1:
        bot.responde('Escolha o recheio da borda:')
        for i in range(len(borders)):
            resposta = '({}) - {}'.format(i,borders[i])
            bot.responde(resposta)
        b = int(escuta_resposta(resposta))
        if b >= 0 and b < len(borders):
            borda = borders[b]
        else:
            bot.responde('Essa opção de borda não existe')
    
    bot.responde('Deseja adicionar alguma bebida ao seu pedido?\n(1) SIM\n(2) NÃO')
    more_add = int(escuta_resposta('(2) NÃO'))
    if(more_add == 1):
        bot.responde('Escolha o seu refrigerante:')
        for i in range(len(refrigerante)):
            resposta = '({}) - {}'.format(i,refrigerante[i])
            bot.responde(resposta)
        r = int(escuta_resposta(resposta))
        if r >= 0 and r < len(borders): 
            refri = refrigerante[r]
        else:
            bot.responde('Essa opção de borda não existe')
    return total_pedido()


def total_pedido():
    global tamanho
    global sabores
    global borders
    global borda
    global refrigerante
    global refri
    global menu
    bot.responde('Por favor, confirme seu pedido:')
    bot.responde('Pizza tamanho: {}'.format(tamanho))
    bot.responde('Sabores:')
    for i in sabores:
        j = int(i)
        bot.responde('{} '.format(menu[j]))
    if(borda != ''):
        bot.responde('Borda:')
        bot.responde(borda)
    if(refri != ''):
        bot.responde('refri:')
        bot.responde(refri)
    bot.responde('Valor total: R$ {}'.format(
        valor_total(tamanho, sabores, borda, refri)))
    bot.responde('O seu pedido está correto?\n(1) SIM\n(2) NÃO')
    answer = int(escuta_resposta('(2) NÃO'))
    if answer == 1:
        
        return payment()
    else:
        return alteracao_pedido()


def valor_total(tamanho, sabores, borda, refri):
    vl_total = 0.0
    if(tamanho == 'Pequena'):
        vl_total += 15.00
    elif (tamanho == 'Media'):
        vl_total += 20.00
    elif (tamanho == 'Grande'):
        vl_total += 25.00
    if(borda != ''):
        vl_total += 1
    if(refri != ''):
        vl_total += 7.00
    return vl_total


def payment():

    resposta = 'Qual a forma de pagamento:\n(1) Dinheiro\n(2) Cartão'
    bot.responde(resposta)
    opt_payment = int(escuta_resposta('(2) Cartão'))
    if opt_payment == 1:
        
        resposta = 'Deseja troco?\n(1) SIM\n(2) NÃO'
        bot.responde(resposta)
        pay_back = int(escuta_resposta('(2) NÃO'))
        if pay_back == 1:
            resposta = 'Para quanto deseja o troco?'
            bot.responde(resposta)
            client_money = float(escuta_resposta('Para quanto deseja o troco?'))
            resposta = 'O troco será: R${}'.format(client_money - (valor_total(tamanho, sabores, borda, refri)))
            bot.responde(resposta)
            recebe_endereco()
    elif opt_payment == 2: 
        bot.responde('O motoboy levará a máquineta para o pagamento no ato da entrega!')
        recebe_endereco()
    else:
        bot.responde('Ops! Digite apenas o número referente ao pagamento')
        payment()
    
def recebe_endereco():
    global endereco
    resposta = 'Por ultimo, escreva seu endereço completo com numero, rua, complemento e ponto de localização.'
    bot.responde(resposta)
    endereco = escuta_resposta(resposta)
    finalizacao()

    
def finalizacao():
    global tamanho
    global sabores
    global borders
    global borda
    global refrigerante
    global refri
    global menu
    global endereco
    
    print('Entrou na finalização de pedido')
    if len(sabores)==1:
        sabor1 = sabores[0]
        sabor2 = None
        sabor3 = None
    elif len(sabores)==2:
        sabor1 = sabores[0]
        sabor2 = sabores[1]
        sabor3 = None
    else:
        sabor1 = sabores[0]
        sabor2 = sabores[1]
        sabor3 = sabores[2]

        core.insert(nome,tamanho,sabor1,sabor2,sabor3,refri,borda,endereco)
        view_command()
    resposta = 'Pedido concluido com sucesso! Nós agradecemos sua confiança.'
    bot.responde(resposta)
    app.run()

def escuta_resposta(resposta):
    while(True):
        texto = bot.escuta()
        #re.match(r'^#', resposta)
        if(texto != resposta):
            return texto


def view_command():
    rows = core.view()
    app.listPedidos.delete(0, END)
    for r in rows:
        app.listPedidos.insert(END, r)

def search_command():
    app.listPedidos.delete(0, END)
    rows = core.search(app.txtNome.get())
    for r in rows:
        app.listPedidos.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtTamanho.get(), app.txtSabor1.get(), app.txtSabor2.get(), app.txtSabor3.get(), app.txtRefri.get(), app.txtBorda.get(), app.txtEndereco.get())
    view_command()

def update_command():
    core.update(selected[0],app.txtNome.get(), app.txtTamanho.get(), app.txtSabor1.get(), app.txtSabor2.get(), app.txtSabor3.get(), app.txtRefri.get(), app.txtBorda.get(), app.txtEndereco.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listPedidos.curselection()[0]
    selected = app.listPedidos.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entTamanho.delete(0, END)
    app.entTamanho.insert(END, selected[2])
    app.entSabor1.delete(0, END)
    app.entSabor1.insert(END, selected[3])
    app.entSabor2.delete(0, END)
    app.entSabor2.insert(END, selected[4])
    app.entSabor3.delete(0, END)
    app.entSabor3.insert(END, selected[5])
    app.entRefri.delete(0, END)
    app.entRefri.insert(END, selected[6])
    app.entBorda.delete(0, END)
    app.entBorda.insert(END, selected[7])
    app.entEndereco.delete(0, END)
    app.entEndereco.insert(END, selected[8])
    return selected




menu = {
    1: "AMERICANA",
    2: "APRESUNTADA",
    3: "CROCANTE",
    4: "MILHO",
    5: "MUSSARELA",
    6: "TRADICIONAL",
    7: "ALHO E ÓLEO",
    8: "BACON",
    9: "CALABRESA",
    10: "ESCAROLA",
    11: "FRANGO",
    12: "FRANGO C/ CATUPIRY",
    13: "FRAN-MILHO",
    14: "MARGUERITA",
    15: "MEXICANA",
    16: "NAPOLITANA",
    17: "PAULISTA",
    18: "PORTUGUESA",
    19: "TOSCANA",
    20: "ALICHE"
}


tamanho = ''
sabores = []
borda = ''
refri = ''
borders = ['Catupiry', 'Cheddar', 'Calabresa', 'Queijo', 'Nutela']
refrigerante = ['Coca-cola', 'Fanta', 'Sprite', 'Kuat', 'Guaraná Antartica']
nome = ''
endereco = ''




bot.inicia()
app = Gui()
app.listPedidos.bind('<<ListboxSelect>>', getSelectedRow)

app.btnViewAll.configure(command=view_command)
app.btnBuscar.configure(command=search_command)
app.btnInserir.configure(command=insert_command)
app.btnUpdate.configure(command=update_command)
app.btnDel.configure(command=del_command)
app.btnClose.configure(command=app.window.destroy)



while(True):
    
    
    texto = str(bot.escuta())
    if(texto == 'Boa noite!'):
        saudacao(True) 
    
    # bot.verifica_converca()
    # # if(bot.verifica_converca()):
    # #     saudacao(True)
    # time.sleep(5)
# saudacao()
