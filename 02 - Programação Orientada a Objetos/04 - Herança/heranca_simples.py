class veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
    
    def ligar_motor(self):
        print("Ligando o motor.")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"
        

class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "No"}'
              ", estou carregado.")

moto1 = motocicleta("preta", "ABC-1234", 2)
# print(moto)
# moto.ligar_motor()

carro1 = carro("branco", "FYM6G41", 4)
# carro.ligar_motor()

caminhao1 = caminhao("roxo", "GYM-5489", 6, True)
# caminhao.ligar_motor()
caminhao1.esta_carregado()

print(moto1)
print(caminhao1)
print(carro1)

