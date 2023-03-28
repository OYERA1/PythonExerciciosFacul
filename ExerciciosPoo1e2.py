# ----------------- Livro -----------------

class Livro:
    def __init__(self, nome, autor, num_paginas):
        self.nome = nome
        self.autor = autor
        self.num_paginas = num_paginas


livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
livro2 = Livro("Morro dos Ventos Uivantes", "Emily Brontë", 368)


# --------------- Triângulo ---------------

class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        perimetro = self.lado_a + self.lado_b + self.lado_c
        return print(perimetro)


t1 = Triangulo(
    int(input('Primeiro lado: ')),
    int(input('Segundo lado: ')),
    int(input('Terceiro lado: '))
)

t1.calcular_perimetro()

# --------------- Televisão ---------------


class Televisao:
    def __init__(self, canal=None, volume=0):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, newCanal):
        self.canal = newCanal


tv1 = Televisao()


tv1.alterar_canal(6)

tv1.aumentar_volume()
tv1.aumentar_volume()
tv1.aumentar_volume()
tv1.aumentar_volume()
tv1.diminuir_volume()

print(
    f'A Televisão está sintonizada no canal: {tv1.canal}. E está no volume: {tv1.volume}'
)

# --------------- Funcionario -------------


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, percentual):
        percentual = self.salario * (percentual/100)
        self.salario += percentual


f1 = Funcionario(
    input('Digite seu nome: '),
    int(input('Digite seu salário: '))
)

porcentagem = int(
    input('Porcentagem de aumento de salário à ser adicionada: '))

f1.aumentarSalario(porcentagem)

print(f'{f1.nome}, seu salário com o aumento de {porcentagem} será de: {f1.salario}')


# -------------------- Carro --------------


class Carro:
    def __init__(self):
        self.lts = 0

    def adicionarCombustivel(self, litros):
        self.lts += litros

    def obterCombustivel(self):
        return self.lts

    def andar(self, distancia):
        
        self.lts = distancia / 20


car1 = Carro()

car1.adicionarCombustivel(20)
car1.andar(80)
print(f'Litros de combustível no tanque: {car1.obterCombustivel()}')


# --------------------- Exercicios da segunda aula --------------------------------

# ---------------- Carro ------------------

class Carro2:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    
    def exibir_dados(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nPlaca{self.placa}')


def main():

    c1 = Carro2('Volkswagen', 'Kombi', 'SAO-1930')
    c2 = Carro2('Ford', 'Mustang', 'SPO-1992')

    c1.exibir_dados()
    c2.exibir_dados()




# -------------- Functionario -------------

class Funcionario:
    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.salario_mensal = sobrenome
        self.salario_mensal = salario_mensal
        if self.salario_mensal < 0:
            self.salario_mensal = 0
    
    def aumentar_salario(self):
        self.salario_mensal += self.salario_mensal * 0.10


    def salario_anual(self):
        return self.salario_mensal * 12

def main():
    f1 = Funcionario('Luan', 'Oyera', 2000)
    f2 = Funcionario('Jorge', 'Souza', 5000)
    
    f1.aumentar_salario()
    f2.aumentar_salario()
    
    print(f1.salario_anual())
    print(f2.salario_anual())



main()

# --------- Conta Bancaria ----------------

class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor, senha):
        if self.senha == senha:
            self.saldo += valor
        else:
            print('senha incorreta')


    def sacar(self, valor, senha):
        if self.senha == senha:
            self.saldo -= valor
            # if self.saldo >= valor:
            #     self.saldo -= valor
            # else:
            #     print('saldo insuficiente')
        else:
            print('senha incorreta')


def main1():
    c1 = ContaBancaria(123, 'Luan', 1234)

    c1.depositar(41, 1234)

    c1.sacar(42, 1234)
    print(c1.saldo)

main1()

# ------------- Aluno ---------------------

class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas=[]
        
    def inserir_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas) / (len(self.notas))

        return media        
    
def main2():
    a1 = Aluno('2203300', 'luan', 'SI')

    a1.inserir_nota(10)
    a1.inserir_nota(5)
    a1.inserir_nota(3)
    a1.inserir_nota(4)

    print(a1.calcular_media())


main2()