class Professor:
    def __init__(self, nome, drt, contratacao, status, disciplina, cargaMax):
        self.nome = nome
        self.drt = drt
        self.contratacao = contratacao
        self.status = status
        self.disciplina = disciplina
        self.cargaMaxima = cargaMax

    def setDisciplina(self, disciplina):
        self.disciplina = disciplina

    def setCargaMaxima(self, cargaMax):
        self.cargaMaxima = cargaMax

def exibe(p):
    print(f'Nome........: {p.nome}')
    print(f'DRT.........: {p.drt}')
    print(f'Contratação.: {p.contratacao}')
    print(f'Status......: {p.status}')
    print(f'Disciplina..: {p.disciplina}')
    print(f'Carga máxima: {p.cargaMaxima}')
    print()
