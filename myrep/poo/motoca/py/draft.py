class pessoa
    def __init__(self, nome: str);
    self.nome = nome
    def

class moto
    def __init__(self):
        self.pessoa: pessoa | none = none
    
    def inserir(self, pessoa : pessoa):  -> bool:
        if self.pessoa != none:
            print("Já tem gente na moto")
            return true
        self.pessoa = pessoa
        return false

    def remover(self) -> pessoa | none:
        aux = self.pessoa
        self.pessoa = none
        return aux

moto = moto()
moto.inserir(pessoa("fulano"))
print(moto.pessoa)
fulano = moto.remover()

def main():
    moto = moto()

    while true:
        line = input()
        print("$")
main()