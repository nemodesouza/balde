class Balde:
    def __init__ (self, capacidade):
        self.__capacidade = capacidade
        self.__quantidade = 0
    
    def fique_cheio(self):
        self.__quantidade = self.__capacidade
    
    def fique_vazio(self):
        self.__quantidade = 0

    def esta_cheio(self):
        self.__quantidade == self.__capacidade
    
    def esta_vazio(self):
        self.__quantidade == 0

    def retorne_capacidade(self):
        return self.__capacidade
    
    def retorne_quantidade(self):
        return self.__quantidade
    
    def derrame_em(self, outro_balde):
        quantidade_restante = outro_balde.__capacidade - outro_balde.__quantidade
        
        if quantidade_restante > self.__quantidade:
            outro_balde.__quantidade = outro_balde.__quantidade + self.__quantidade
            self.__quantidade = 0
        else:
            outro_balde.__quantidade = outro_balde.__capacidade
            self.__quantidade = self.__quantidade - quantidade_restante

    def receba_de(self, outro_balde):
        outro_balde.derrame_em(self)

