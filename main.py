import textwrap
from datetime import datetime

# ==============================
# CLASSES DO SISTEMA
# ==============================

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Movimentacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo}: R$ {self.valor:.2f}"


class Conta:
    def __init__(self, agencia, numero, usuario, limite=500, limite_saques=3):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.movimentacoes = []

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return
        self.saldo += valor
        self.movimentacoes.append(Movimentacao("Depósito", valor))
        print("\n=== Depósito realizado com sucesso! ===")

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
        elif valor > self.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! Valor excede o limite da conta. @@@")
        elif self.numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques atingido. @@@")
        else:
            self.saldo -= valor
            self.numero_saques += 1
            self.movimentacoes.append(Movimentacao("Saque", valor))
            print("\n=== Saque realizado com sucesso! ===")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("\n@@@ Valor de transferência inválido. @@@")
        elif valor > self.saldo:
            print("\n@@@ Saldo insuficiente para transferência. @@@")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.movimentacoes.append(Movimentacao(f"Transferência p/ C/C {conta_destino.numero}", valor))
            conta_destino.movimentacoes.append(Movimentacao(f"Transferência recebida da C/C {self.numero}", valor))
            print("\n=== Transferência realizada com sucesso! ===")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            for mov in self.movimentacoes:
                print(mov)
        print(f"\nSaldo atual:\tR$ {self.saldo:.2f}")
        print("=========================================")


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    # ==============================
    # MÉTODOS DE USUÁRIO
    # ==============================
    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if self.buscar_usuario_por_cpf(cpf):
            print("\n@@@ Usuário já existe! @@@")
            return
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
        usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(usuario)
        print("\n=== Usuário criado com sucesso! ===")

    def buscar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    # ==============================
    # MÉTODOS DE CONTA
    # ==============================
    def criar_conta(self):
        if not self.usuarios:
            print("\n@@@ Nenhum usuário cadastrado! Crie um usuário primeiro. @@@")
            return
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.buscar_usuario_por_cpf(cpf)
        if not usuario:
            print("\n@@@ Usuário não encontrado! @@@")
            return
        numero_conta = len(self.contas) + 1
        conta = Conta("0001", numero_conta, usuario)
        self.contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")

    def listar_contas(self):
        if not self.contas:
            print("\n@@@ Nenhuma conta cadastrada! @@@")
            return
        for conta in self.contas:
            print("=" * 50)
            print(f"Agência:\t{conta.agencia}")
            print(f"C/C:\t\t{conta.numero}")
            print(f"Titular:\t{conta.usuario.nome}")
            print("=" * 50)

    def buscar_conta_por_numero(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

# ==============================
# FUNÇÃO MENU
# ==============================
def menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [t]\tTransferir
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================
def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            numero = int(input("Informe o número da conta: "))
            conta = banco.buscar_conta_por_numero(numero)
            if not conta:
                print("\n@@@ Conta não encontrada! @@@")
                continue
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "s":
            numero = int(input("Informe o número da conta: "))
            conta = banco.buscar_conta_por_numero(numero)
            if not conta:
                print("\n@@@ Conta não encontrada! @@@")
                continue
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        elif opcao == "t":
            numero_origem = int(input("Informe o número da sua conta: "))
            conta_origem = banco.buscar_conta_por_numero(numero_origem)
            if not conta_origem:
                print("\n@@@ Conta de origem não encontrada! @@@")
                continue
            numero_destino = int(input("Informe o número da conta destino: "))
            conta_destino = banco.buscar_conta_por_numero(numero_destino)
            if not conta_destino:
                print("\n@@@ Conta de destino não encontrada! @@@")
                continue
            valor = float(input("Informe o valor da transferência: "))
            conta_origem.transferir(valor, conta_destino)

        elif opcao == "e":
            numero = int(input("Informe o número da conta: "))
            conta = banco.buscar_conta_por_numero(numero)
            if not conta:
                print("\n@@@ Conta não encontrada! @@@")
                continue
            conta.exibir_extrato()

        elif opcao == "nu":
            banco.criar_usuario()

        elif opcao == "nc":
            banco.criar_conta()

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            print("\nSaindo do sistema... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
