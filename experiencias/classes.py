class Pessoa:
    def __init__(self,nome,sexo,cpf,ativo):
        self.nome=nome
        self.sexo=sexo
        self.cpf=cpf
        self.ativo=ativo

    def eliminar(self):
        self.ativo=False
        print("A pessoa foi eliminda com sucesso")

if __name__=="__main__":
    pessoa1=Pessoa("diego","M","123456",True)
    print(pessoa1.nome)
    print(pessoa1.sexo)
    print(pessoa1.cpf)
    print(pessoa1.ativo)
    pessoa1.eliminar()
    print(pessoa1.ativo)
