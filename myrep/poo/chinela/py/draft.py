class chinela:
    def __init__(self):
        self.__tamanho = 0 

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor:int):
         if valor < 20 or valor > 50:
            print("Tamanho inválido! Digite um número entre 30 e 50.")

chinela = chinela()

while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    try:
        tamanho = int(input())
        chinela.setTamanho(tamanho)
    except ValueError:
        print("Por favor, digite apenas números inteiros.")


print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())
