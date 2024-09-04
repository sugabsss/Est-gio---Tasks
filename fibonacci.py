
class Sequencia:
    def __init__(self):
        self.fibonnaci = []
        self.numero = 0

    def criando_fibonacci(self, limite):
        a, b = 0, 1
        self.fibonnaci.append(a)
        while b <= limite:
            self.fibonnaci.append(b)
            a, b = b, a + b

    def numero_informado(self):
        while True:
            try:
                self.numero = int(input("Informe um número: "))
                if self.numero < 0:
                    print("Por favor, informe um número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, informe um número válido.")
        
        self.criando_fibonacci(self.numero)

        if self.numero in self.fibonnaci:
            print(f"» » » ({self.numero}) Pertence à sequência de Fibonacci « « «")
        else:
            print(f"» » » {self.numero} Não pertence à sequência de Fibonacci.« « «")
        
        print(f"Sequência de Fibonacci até o número ({self.numero}): {self.fibonnaci}")

sequencia = Sequencia()
sequencia.numero_informado()
