import os
import time
import re
import urllib.request
from selenium import webdriver


class wppbot:
    #Pega o diretorio onde está salvo o arquivo wppbot.py
    dir_path = os.getcwd()
    
    #Inicia o bot
    def __init__(self, nome_bot):
        print('Iniciado')
        #salva o perfil para não precisar escanear 
        self.chrome = self.dir_path+'/chromedriver_linux64/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            r"user-data-dir="+self.dir_path+"/profile/wpp")
        self.driver = webdriver.Chrome(
            self.chrome, chrome_options=self.options)
    
    #Inicia o google chrome
    def inicia(self):
        #self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)
        
    def fecha(self):
        self.driver.close()
    #esculta as conversas
    def verifica_converca(self):
        try:
            inicia = self.driver.find_elements_by_class_name('_19RFN')
            texto = inicia[1].find_element_by_class_name('_19RFN').text
            print(texto)
            if (texto == 'Fala bot!'):
                self.primeira_converca = self.driver.find_element_by_class_name('_19RFN')
                self.primeira_converca.click()
                print('True')
                #return True
            
        except: 
            print('Nada Encontrado ou erro')
            self.verifica_converca()
    
    def escuta(self):
        try:
            
            post = self.driver.find_elements_by_class_name('FTBzM')
            ultimo = len(post) - 1
            texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
            return texto
        except:
            return self.escuta()
    
    
    def responde(self,resposta):
        try:
            response = str(resposta)
            self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3FeAD')
            self.caixa_de_mensagem.send_keys(response)
            #time.sleep(1)
            self.botao_enviar = self.driver.find_element_by_class_name('_3M-N-')
            self.botao_enviar.click()
        except:
            self.responde(resposta)

    def show_cardapio(self):
        try:
            self.botao_anexo = self.driver.find_element_by_css_selector("span[data-icon='clip']")
            self.botao_anexo.click()
            #self.driver.implicitly_wait(5)
            self.busca_anexo = self.driver.find_element_by_css_selector("input[type='file']")
            self.dir_path = self.dir_path+"/cardapio.jpeg"
            self.busca_anexo.send_keys(self.dir_path)
            #self.driver.implicitly_wait(5)
            #self.enviar_anexo = self.driver.find_element_by_css_selector("span[data-icon='send-light']")
            flag = True
            while flag:
                flag = False
                try:
                    self.enviar_anexo = self.driver.find_element_by_css_selector("span[data-icon='send-light']")
                    #self.enviar_anexo = self.driver.find_element_by_class_name('_1g8sv')
                    self.enviar_anexo.click()
                except:
                    flag = True
                    print('Erro')
            #self.driver.implicitly_wait(5)
        except:
            #_1g8sv
            self.show_cardapio()