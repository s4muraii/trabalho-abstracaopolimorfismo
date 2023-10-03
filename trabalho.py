# Para iniciar o trabalho, explicarei como funciona o Polimorfismo em Python.
# Polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas.
# Em Python, o Polimorfismo é implementado através de Herança.
# Herança é a capacidade de uma classe herdar atributos e métodos de outra classe.

# Para exemplificar, aqui vai um exemplo de uma classe chamada Animal, que possui um método chamado falar.

class Animal:
    def falar(self):
        print('Falando...')

# A classe Animal possui um método que imprime a mensagem "Falando...".
# Através do polimorfismo, vamos criar outra classe que também utilizara o método falar, mas com uma mensagem diferente.

class Cachorro(Animal):
    def falar(self):
        print('Au au!')

# A classe Cachorro herda os atributos e métodos da classe Animal, e utiliza o mesmo método Falar mas de forma diferente.
# Agora, vamos criar uma classe Gato que também herda os atributos e métodos da classe Animal, e utiliza o mesmo método Falar mas de forma diferente.

class Gato(Animal):
    def falar(self):
        print('Miau!')

# A classe Gato, assim como a classe Animal e a classe Cachorro, herda os atributos e métodos da classe Animal, e utiliza o mesmo método Falar mas polimorfizando sua funcionalidade.

# Vamos instanciar os objetos para testar.
animal = Animal()
cachorro = Cachorro()
gato = Gato()

# Agora, vamos chamar o método Falar de cada objeto.
animal.falar()
cachorro.falar()
gato.falar()

# O polimorfismo é utilziado para reaproveitar código, e também para criar classes que possuem o mesmo método, mas com funcionalidades diferentes.
# O polimorfismo é usado profissionalmente em casos como: um sistema de cadastro de funcionários, onde cada funcionário possui um salário diferente, mas todos possuem o mesmo método para calcular o salário.

# Para exemplificar, vamos criar uma classe Funcionario que possui um método para calcular o salário.

class Funcionario:
    def calcularSalario(self):
        print('Calculando salário...')
        print('Salário calculado!')

# Agora, vamos criar uma classe Gerente que herda os atributos e métodos da classe Funcionario, e utiliza o mesmo método calcularSalario mas de forma diferente.

class Gerente(Funcionario):
    def calcularSalario(self):
        print('Calculando salário...')
        print('Salário calculado!')
        print('Adicionando bônus...')
        print('Bônus adicionado!')
        print('Salário final calculado!')

# O gerente possui o mesmo método que o funcionário, mas devido ao seu cargo, ele possui um bônus no salário. Esse bônus altera o método, poliformizando seu uso.

# Vamos instanciar os objetos para testar.
funcionario = Funcionario()
gerente = Gerente()

# Agora, vamos chamar o método calcularSalario de cada objeto.

funcionario.calcularSalario()
gerente.calcularSalario()

#####################################################################################################################################################################

# Agora a Abstração.
# A abstração se resume na criação de classes abstratas, que não podem ser instanciadas e que servem como modelo para outras classes.

# Basicamente, a abstração tem como função moldar outras classes sem poder ser instanciada.
# O Python não oferece suporte para classes abstratas, mas podemos utilizar a biblioteca ABC para criar classes abstratas.

# Para exemplificar, vamos criar uma classe abstrata chamada Pessoa, que não pode ser instanciada.

from abc import * # Devemos iniciar a criação de classes abstratas importando a biblioteca ABC.

class Pessoa:
    @abstractmethod # Para criar uma classe abstrata, devemos utilizar o decorador @abstractmethod.

    def idade(self):
        pass

    def andar(self):
        pass

# A classe Pessoa não pode ser instanciada, e serve como modelo para outras classes.

class Criança(Pessoa):

    def idade(self):
        print('18 anos')

    def andar(self):
        print('Andando...')

# A classe Criança herda os atributos e métodos da classe Pessoa, e pode ser instanciada normalmente. Mas a classe Pessoa serve apenas para moldar a classe Criança.
# Corporativamente, a abstração é utilizada em exemplos como: um sistema veterinário, onde existem vários tipos de animais, mas todos possuem as mesmas características, como idade, peso, altura, etc. 

# Para exemplificar, vamos criar uma classe Animal que não pode ser instanciada.

from abc import * # Devemos iniciar a criação de classes abstratas importando a biblioteca ABC.

class Animal:
    @abstractmethod # Para criar uma classe abstrata, devemos utilizar o decorador @abstractmethod.

    def idade(self):
        pass

    def peso(self):
        pass

    def altura(self):
        pass

# A classe Animal não pode ser instanciada, e serve como modelo para outras classes.

class Cachorro(Animal):
    
        def idade(self):
            print('10 anos')
    
        def peso(self):
            print('10 kg')
    
        def altura(self):
            print('50 cm')

# A classe Cachorro herda os atributos e métodos da classe Animal, e pode ser instanciada normalmente. Mas a classe Animal serve apenas para moldar a classe Cachorro.

# Agora, vamos instanciar os objetos para testar.

cachorro = Cachorro()

# Agora, vamos chamar o método idade de cada objeto.

cachorro.idade()