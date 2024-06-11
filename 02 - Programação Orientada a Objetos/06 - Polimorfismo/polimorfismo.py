class Passaro:
  def voar(self):
    print("Passaro voando")

class Pardal(Passaro):
  def voar(self):
    super().voar()

class Averstruz(Passaro):
  def voar(self):
    print("Avestruz nao pode voar")


class Aviao(Passaro):
  def voar(self):
    print("Aviao esta decolando...")

def plano_voo(obj):
  obj.voar()

plano_voo(Passaro())
plano_voo(Pardal())
plano_voo(Averstruz())
plano_voo(Aviao())
