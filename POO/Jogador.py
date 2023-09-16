from Tabela import Tabela
from random import randint
class Jogador:
    __nome=''
    __trueTable= Tabela() #Nesta tabela
    __tabelaMostrada= Tabela()
    
    __navioSimbolo='N'
    __ErroSimbolo='X'
    __AcertoSimbolo='F'
    
    def __init__(self,nome:str,naviosQuantidade:int):
        self.__nome=nome
        
        
    @nome.setter
    def nome(self,nome:str):
        self.nome=nome
        
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    
    def montarTabelaVerdadeira(self, naviosQuantidade:int, randomize:bool = True, posicoes: list[list[int]] = None):
    
        if randomize:
            # Lógica para gerar aleatoriamente as posições dos navios
            self.__trueTable = Tabela(10, 10)  # Assumindo um tabuleiro de 10x10
            for navio in range(naviosQuantidade):
                while True:
                    col = randint(1, 10)
                    row = randint(1, 10)
                    if self.__trueTable.obterSimbolo(col, row) != 'N':
                        self.__trueTable.inserirSimbolo(col, row, 'N')
                        break
            
        else:
            self.__trueTable = Tabela(10, 10)  # Assumindo um tabuleiro de 10x10
            for posicao in posicoes:
                col, row = posicao
                self.__trueTable.inserirSimbolo(col, row, 'N')
                
    def montarTabelaMostrada(self):
        self.__tabelaMostrada = Tabela(10, 10)  # Assumindo um tabuleiro de 10x10
        
        
    def marcarJogada(self, col:int, row:int)->bool:
        '''Se tiver acertado a posição de um navio, retorna True, e False caso contrário.
        Também altera a  tabelaMostrada
        '''
        simbolo = self.__ErroSimbolo
        Acertounavio= self.__trueTable.obterSimbolo(col, row) == 'N'        
        if Acertounavio:
            simbolo = self.__AcertoSimbolo

        self.__tabelaMostrada.inserirSimbolo(col, row,simbolo)
        
        return Acertounavio