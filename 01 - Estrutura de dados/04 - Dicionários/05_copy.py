contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()

print(contatos)  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia)

contatos["guilherme@gmail.com"]["nome"] = "Ju"
print(contatos)  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia)

copia["guilherme@gmail.com"]["nome"] = "Gui"
print(contatos)  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia)

print(contatos)  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia)  # {"nome": "Gui"}


# copia["guilherme@gmail.com"]["nome"] = "Gu"
# print(copia["guilherme@gmail.com"])
# print(contatos["guilherme@gmail.com"])