import json
import os
from datetime import datetime

login_salvo = None

def relatorio():
    print("\n--- RELATÓRIO ---")

    lancamentos = carregar()

    if len(lancamentos) == 0:
        print("[!] Nenhum lançamento registrado ainda.\n")
        return

    treceitas = 0
    tdespesas = 0
    categorias = {}

    for lancamento in lancamentos:
        valor = lancamento["valor"]
        categoria = lancamento["categoria"]

        if lancamento["tipo"] == "receita":
            treceitas += valor
        else:
            tdespesas += valor

        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += valor

    saldo = treceitas - tdespesas

    print(f"\nTotal de receitas:  R$ {treceitas:.2f}")
    print(f"Total de despesas:  R$ {tdespesas:.2f}")
    print(f"Saldo total:        R$ {saldo:.2f}")
    print("\n-- Por categoria --")
    for categoria, total in categorias.items():
        print(f"  {categoria}: R$ {total:.2f}")
    print()


def carregar():
    if os.path.exists("lancamentos.json"):
        with open("lancamentos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar(lancamentos):
  
    with open("lancamentos.json", "w", encoding="utf-8") as arquivo:
        json.dump(lancamentos, arquivo, indent=4, ensure_ascii=False)

def registrar_lancamento():
    print("\n--=-- REGISTRAR LANÇAMENTO --=--")

    while True:
        tipo = input("Tipo (receita/despesa): ").strip().lower()
        if tipo in ("receita", "despesa"):
            break
        print("[X] Tipo inválido! Digite 'receita' ou 'despesa'.")

    while True:
        try:
            valor = float(input("Valor (ex: 150.00): R$ "))
            if valor <= 0:
                print("[X] O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("[X] Valor inválido! Digite apenas números (ex: 150.00).")

    while True:
        categoria = input("Categoria (ex: alimentação, salário): ").strip()
        if categoria != "":
            break
        print("[X] A categoria não pode ser vazia.")

    while True:
        descricao = input("Descrição (ex: almoço no trabalho): ").strip()
        if descricao != "":
            break
        print("[X] A descrição não pode ser vazia.")

    lancamento = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao
    }
    lancamentos = carregar()
    lancamentos.append(lancamento)
    salvar(lancamentos)

    print(f"\n[✓] Lançamento registrado com sucesso!")
    print(f"    {tipo.upper()} | R$ {valor:.2f} | {categoria} | {descricao}\n")

def  extrato():

    print("Extrato")

    lancamentos = carregar()

    if len (lancamentos) == 0:
        print("[!] Nenhum lançamento registrado ainda.\n")
        return

    for lancamento in lancamentos:
        print(f"\nData:      {lancamento['data']}")
        print(f"Tipo:      {lancamento['tipo'].upper()}")
        print(f"Categoria: {lancamento['categoria']}")
        print(f"Descrição: {lancamento['descricao']}")
        print(f"Valor:     R$ {lancamento['valor']:.2f}")
        print("-" * 40)

def exportar_relatorio():
    print("\n--=-- EXPORTAR RELATÓRIO --=--")

    lancamentos = carregar()

    if len(lancamentos) == 0:
        print("[!] Nenhum lançamento para exportar.\n")
        return

    treceitas = 0
    tdespesas = 0
    categorias = {}

    for lancamento in lancamentos:
        valor = lancamento["valor"]
        categoria = lancamento["categoria"]

        if lancamento["tipo"] == "receita":
            treceitas += valor
        else:
            tdespesas += valor

        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += valor

    saldo = treceitas - tdespesas

    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=-=-= RELATÓRIO DE FINANÇAS =-=-=\n")
        arquivo.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        arquivo.write(f"Total de receitas:  R$ {treceitas:.2f}\n")
        arquivo.write(f"Total de despesas:  R$ {tdespesas:.2f}\n")
        arquivo.write(f"Saldo total:        R$ {saldo:.2f}\n")
        arquivo.write("\n-- Por categoria --\n")
        for categoria, total in categorias.items():
            arquivo.write(f"  {categoria}: R$ {total:.2f}\n")

    print("[✓] Relatório exportado com sucesso em relatorio.txt!\n")        

while True:
    print("=-=-=-=-=- Bem vindo ao seu gestor de gastos -=-=-=-=-=-=-=")
    print("\n                    Escolha uma opção\n")
    print("                  [1] Logar | [2] Cadastrar           ")
    print("                  [3] Sair\n")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    opcao1 = input("Digite sua escolha: ")

    if opcao1 == "1":
        if login_salvo is None:
            print("[!] Nenhum usuário cadastrado ainda! Escolha a opção [2] primeiro.")
        else:
            usuario_input = input("Digite o nome de usuário: ")
            if usuario_input == login_salvo:
                print("[✓] Usuário confirmado! Entrando no sistema...")
                break
            else:
                print("[X] Usuário inválido. Tente novamente.")
    elif opcao1 == "2":
        login_salvo = input("Cadastre seu nome de usuário: ")
        if login_salvo == "":
            print("[X] O nome não pode ser vazio!")
            login_salvo = None
        else:
            print(f"[✓] Usuário '{login_salvo}' cadastrado com sucesso!\n")
    elif opcao1 == "3":
        print("Saindo do sistema... Até logo!")
        exit()
    else:
        print("[X] Opção inválida! Escolha 1, 2 ou 3.")

while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-= Sua conta =-=-=-=-=-=-=-=-=-=-=-=-=")
    print("                       Escolha uma opção")
    print("")
    print("          [1] Registrar | [2] Extrato | [3] Relatório")
    print("                   [4] Exportar | [5] Sair    ")
    print("")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    opcao_menu = input("Digite sua escolha: ")

    if opcao_menu == "1":
        registrar_lancamento()
    elif opcao_menu == "2":
        extrato()
    elif opcao_menu == "3":
        relatorio()
    elif opcao_menu == "4":
        exportar_relatorio()
    elif opcao_menu == "5":
        print("\nSaindo da sua conta de finanças... Volte sempre!")
        break
    else:
        print("\n[X] Opção inválida! Escolha de 1 a 5.\n")