

class Conta:

    # construtor
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("O saldo é de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo +=valor

    def saca(self, valor):
        if (self.__limite_suficiente(valor)):
            self.__saldo -=valor
        else:
            print("O seu limite é insuficiente")

    def __limite_suficiente(self, valor):
        return valor <= (self.saldo + self.limite)

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos(codigo):
        bancos = {"BB":"001", "Caixa":"104", "Bradesco":"237", "Itaú":"341", "Santander":"033"}
        if codigo in bancos:
            return bancos[codigo]
        else:
            return "Banco inválido"


