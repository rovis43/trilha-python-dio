class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

#Familias
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_bico, voa, **kwargs):
        self.cor_bico = cor_bico
        self.voa = voa
        super().__init__(**kwargs)

#Especies
class Cachorro(Mamifero):
        pass

class Gato(Mamifero):
        pass

class Pato(Ave):
        pass

class FalarMixin_Ave():
     def falar(self):
          return "Quack!"

class Ornitorrinco(Mamifero, Ave, FalarMixin_Ave):
        def __init__(self, cor_pelo, cor_bico, nro_patas, voa):
        #      print(Ornitorrinco.__mro__)

             super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas, voa=voa)


gato = Gato(nro_patas=4, cor_pelo="preto")
# print(gato)
# orni = Ornitorrinco(nro_patas=4, cor_pelo="vermelho", voa=False, cor_bico="cinza")
orni = Ornitorrinco(nro_patas=4, cor_pelo="vermelho", cor_bico="cinza", voa=False)
print(orni)
print(orni.falar())
