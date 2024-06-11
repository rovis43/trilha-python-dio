import textwrap
import re

def menu(): 
    menu = """\n
    ======== Menu ========
    [1] Cria usuário
    [2] Nova Conta
    [3] Login conta
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [7] Listar contas
    [8] Sair
    => """
    return input(textwrap.dedent(menu))

#operações de conta
def create_user(USERS):
  cpf = input("[Passo 1/4]\nDigite seu CPF (somente números): ")
  if len(cpf) > 10 and cpf_verifier(cpf):
    nome_completo = input("[Passo 2/4]\nDigite seu nome completo: ")
    if re.match(r"[a-zA-Z]+ [a-zA-Z ]+", nome_completo) is not None:
        email = input("[Passo 3/4]\nDigite seu e-mail:")
        if re.match(r"[-\w\.]+@([-\w]+\.)+[-\w]{2,4}", email) is not None:
            endereco = input("[Passo 4/4]\nDigite seu endereco no seguinte formato: rua, numero, complemento (opcional) - bairro/cidade - estado - CEP: ")
            if endereco.count('-') >= 3:
                return USERS.append({cpf : {"nome" : nome_completo, "e-mail" : email, "endereço": endereco}})
                print("=== Usuario criado com sucesso ===")
            else:
                print("Digite um enderço com formato válido"); return create_user(USERS)
        else:
            print("Digite um e-mail válido"); return create_user(USERS)    
    else:
      print("Digite um nome e sobrenome válido"); return create_user(USERS)
  else:
    print("Formato de CPF invalido"); return create_user(USERS)

def cpf_verifier(CPF):
  cpf_as_l = [int(i) for i in CPF]
  
  verifier1 = sum([x * y  for x, y 
      in zip(range(10,1,-1), cpf_as_l)]) * 10 % 11
  verifier2 = sum([x * y  for x, y 
      in zip(range(11,1,-1), cpf_as_l)]) * 10 % 11
  
  if verifier1 == cpf_as_l[9] or (verifier1 == 10 and cpf_as_l[9] == 0):
      return verifier2 == cpf_as_l[10] or (verifier2 == 10 and cpf_as_l[10] == 0)
  else: 
    return False

def create_new_acc(BRANCH, ACC, ACCS, USERS):
    cpf = input("Digite o CPF do usuário (somente números): ")
    user = filter_user(cpf, USERS)

    if user:
        print("Nova conta criada")
        return ACCS.append({cpf : {"agencia" : BRANCH, "conta" : ACC}})
    
    print("Usuário não cadastrado.")

def list_acc(ACCS):
    for dict_cpf_conta in ACCS:
        cpf_conta = dict_cpf_conta.items()
        for cpf, conta_info in cpf_conta:
            print(f'CPF: {cpf}\t Ag:{conta_info["agencia"]} C/C:{conta_info["conta"]}')


def filter_user(CPF, USERS):
  user_filtrado = [user for user in USERS if CPF in user.keys()] 
  return user_filtrado[0] if user_filtrado else None
    

#operações bancárias
def login():
    print("\nEm desenvolvimento")
    return main()

def deposit(BALANCE, VALUE, STATEMENT, /):
            if VALUE > 0:
                BALANCE += VALUE
                STATEMENT += f"Depósito: R$ {VALUE:.2f}\n"
                print("\n=== Depósito realizado com sucesso! ===")
            else:
                print("Operação falhou! O valor informado é inválido.")

            return BALANCE, STATEMENT

def draft_money(*, BALANCE, VALUE, STATEMENT, DRAFT_VALUE_LIMIT, N_DRAFT, N_DRAFT_LIMIT):
    excedeu_saldo = VALUE > BALANCE
    excedeu_limite = VALUE > DRAFT_VALUE_LIMIT
    excedeu_saques = N_DRAFT >= N_DRAFT_LIMIT

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif VALUE > 0:
        BALANCE -= VALUE
        N_DRAFT += 1
        STATEMENT += f"Saque: R$ {VALUE:.2f}{'(':>15}{N_DRAFT}⁰ saque)\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return BALANCE, STATEMENT, N_DRAFT

def print_statement(BALANCE, /, *, STATEMENT, N_DRAFT, N_DRAFT_LIMIT):
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not STATEMENT else STATEMENT)
            print(f"\nSaldo: R$ {BALANCE:.2f}")
            print(f"Saque(s) restante(s): {N_DRAFT_LIMIT-N_DRAFT}")
            print("==========================================")

def main():
    branch = "001"
    statement = ""
    balance = 0
    n_draft = 0
    n_draft_limit = 3
    draft_value_limit = 500
    users = []
    accs = []

    #Demo
    users.extend([
        {"12345678900" : {"nome" : "Jose Calixto", "email" : "jose.calixto@aol.gov.br", "endereco" : "Rua X, 52 - Vila Leopoldo - Sao Paulo/SP - 00421-845"}},
        {"52687421445" : {"nome" : "Amanda Braga", "email" : "amanda.braga@aol.gov.br", "endereco" : "Rua Y, 84 - Vila Gerti - Santo Andre/PB - 52876-001"}},
        {"99999999999" : {"nome" : "Mar Mendes", "email" : "mar.mendes@aol.gov.br", "endereco" : "Rua Z, 53 - Apto 2 - Industrial - Betim/MG - 12345-678"}}
    ])

    accs.extend([
        {"12345678900" : {"agencia" : branch, "conta" : 1}},
        {"52687421445" : {"agencia" : branch, "conta" : 2}},
        {"99999999999" : {"agencia" : branch, "conta" : 3}}
    ])
    #End Demo

    while True:

        opcao = menu()

        if opcao == "1":
            create_user(users)

        elif opcao == "2":
            acc_n = len(accs) + 1
            create_new_acc(branch, acc_n, accs, users)

        elif opcao == "3":
            login()

        elif opcao == "4":
            value = float(input("Informe o valor do depósito: "))
            balance, statement = deposit(balance, value, statement)

        elif opcao == "5":
            value = float(input("Informe o valor do saque: "))
            balance, statement, n_draft = draft_money(
                BALANCE=balance,
                VALUE=value,
                STATEMENT=statement,
                DRAFT_VALUE_LIMIT=draft_value_limit,
                N_DRAFT=n_draft,
                N_DRAFT_LIMIT=n_draft_limit
                )

        elif opcao == "6":
            print_statement(
                balance,
                STATEMENT=statement,
                N_DRAFT=n_draft,
                N_DRAFT_LIMIT=n_draft_limit
            )

        elif opcao == "7":
            list_acc(accs)

        elif opcao == "8":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
 
main()