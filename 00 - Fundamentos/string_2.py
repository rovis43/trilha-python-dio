nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": nome, "idade": 28, "profissao": profissao, "linguagem": linguagem}
print("7Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**dados))

print("1Nome: %s Idade: %f" % (nome, idade))

print("2Nome: {} Idade: {}".format(nome, idade))

print("3Nome: {1} Idade: {0}".format(idade, nome))
print("4Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("5Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("6Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

print(f"8Nome: {nome} Idade: {idade}")
print(f"9Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"10Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
