class bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha = 1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha
    
    def buzinar(self):
        print("Plim! Plim!")
    
    def parar(self):
        print("Parando bicicleta.")
        print("Bicicleta parada.")
    
    def correr(self):
        print("Pedalando com vigor.")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"
    
    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha")
        _self = self
        return self.marcha(nro_marcha)
        def _trocar_marcha():
            if nro_marcha > _self.marcha:
                print("Marcha trocada.")
            else:
                print("Não foi possível trocar de marcha.")


b1 = bicicleta("vermelha", "caloi", 2022, 600)

# b1.buzinar()
# b1.parar()
# b1.correr()

print(b1)
print(b1.marcha)
bicicleta.trocar_marcha(b1, 2)
print(b1.marcha)