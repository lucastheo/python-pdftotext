import PyPDF2
import os
import re
import random
import string
import time


class pdfFile:

    def __init__(self , caminho = None ):
        if caminho != None:
            self.atalizaPdf(caminho)
            self.arquivoTxtCaminho()
        self._info = None
        self.arquivoSaidaTxt = None
        self._arquivoTxtCaminho = None
        
        diretorioAtual = os.getcwd()
        os.system("cd " + diretorioAtual + " ; echo " " > pdftotext.log" )
    
    def close(self ):
        if self._info != None:
            os.system("cd /tmp rm " + self._info )
    
    def arquivoTxtCaminho(self):
        if self._arquivoTxtCaminho == None:
            self._arquivoTxtCaminho = self.getCaminhoAleatorio()
        
        return self._arquivoTxtCaminho
        
    def atalizaPdf( self , caminho ):
        self.caminhoPdf =  caminho

    def getText(self, atalizaPdf = None, cont = 0):
        
        if atalizaPdf != None:
            self.atalizaPdf(atalizaPdf)
        #print( atalizaPdf )
        caminhoSaida = self.arquivoTxtCaminho()
        diretorioAtual = os.getcwd()
        os.system('echo " " > ' + caminhoSaida  )
        os.system("cd " + diretorioAtual + " ; pdftotext "+ atalizaPdf + " " + caminhoSaida + " 2>> pdftotext.log" )
        
        time.sleep( 1 )

        try:
            arq = open(caminhoSaida, "r")
            text = arq.read()
            arq.close()
        except:
            if cont < 5:
                text = self.getText( atalizaPdf , cont + 1 )

        os.system("rm " + self.arquivoTxtCaminho() )

        return text
    
    def getCaminhoAleatorio(self):
        s = "/tmp/"
        for i in range(0,10):
            s += random.choice(string.ascii_letters)
        
        return s

    def getInfo(self, chave, atalizaPdf ):
        if atalizaPdf != None:
            self.atalizaPdf(atalizaPdf)

        if self._info == None:
            self._info = self.getCaminhoAleatorio()

        os.system("pdfinfo "+ atalizaPdf + " > " + self._info )

        arq = open(self._info, "r")
        text = arq.read()
        arq.close()
        
        #print("-----")
        for line in text.split("\n"):
            #print(line)    
            apo = line.split(":")
            
            if len( apo ) > 1:
                apo[0] = apo[0].strip(" ").lower()
                #print( apo[0] + "|||" + chave.lower() )
                #print(apo[0] == chave.lower())
                if apo[0] == chave.lower():
                    apo[1] = apo[1].strip(" ")
                    #print("bbb", apo[1])
                    return apo[1]
        #print("nada ")
        return "None"
