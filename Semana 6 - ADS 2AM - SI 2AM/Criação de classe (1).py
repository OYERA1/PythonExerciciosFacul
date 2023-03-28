class Professor:
    def __init__(self):
        self.nome = 'Claudio'
        self.drt = '123456'
        self.contratacao = '17/08/1990'
        self.status = 'Titular'
        self.disciplina = 'Matemática'
        self.cargaMaxima = 16


x = Professor()
print(x.nome)
print(x.disciplina)
x.nome = 'Juliana'
print(x.nome)
