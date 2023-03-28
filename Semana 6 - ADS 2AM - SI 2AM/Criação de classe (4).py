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
        if cargaMax <= 40:
            self.cargaMaxima = cargaMax
        else:
            print('Carga máxima ultrapassou o limite!')

    def exibe(self):
        print(f'Nome........: {self.nome}')
        print(f'DRT.........: {self.drt}')
        print(f'Contratação.: {self.contratacao}')
        print(f'Status......: {self.status}')
        print(f'Disciplina..: {self.disciplina}')
        print(f'Carga máxima: {self.cargaMaxima}')
        print()
