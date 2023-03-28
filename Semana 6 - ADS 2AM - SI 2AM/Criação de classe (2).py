class Professor:
    def __init__(self, a, b, c, d='Substituto', e=None, f=4):
        if type(a) != str:
            print('Tipo do nome errado!')
            exit()
        self.nome = a
        self.drt = b
        self.contratacao = c
        self.status = d
        self.disciplina = e
        self.cargaMaxima = f
