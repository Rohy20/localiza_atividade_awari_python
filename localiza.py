class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valorDiario, observacao):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valorDiario = valorDiario
        self.observacao = observacao

class Esportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valorDiario, observacao, tmp100km):
        super().__init__(placa, ano, cor, modelo, quilometragem, valorDiario, observacao)
        self.tmp100km = tmp100km
        self.melhorias = []

    def addMelhoria(self, melhoria):
        self.melhorias.append(melhoria)

class Utilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valorDiario, observacao, qtPassageiro, tmBagageiro, kmLitro):
        super().__init__(placa, ano, cor, modelo, quilometragem, valorDiario, observacao)
        self.qtPassageiro = qtPassageiro
        self.tmBagageiro = tmBagageiro
        self.kmLitro = kmLitro

class Reserva:
    def __init__(self, cliente, codigo, status, dtInicio, dtFim, carro):
        self.cliente = cliente
        self.codigo = codigo
        self.status = status
        self.dtInicio = dtInicio
        self.dtFim = dtFim
        self.carro = carro

    def definirStatusInativa(self):
        self.status = "Inativa"

    def getStatus(self):
        return self.status

    def getCliente(self):
        return self.cliente

class Pessoa:
    # TODO: CONSTRUIR PESSOA
    pass

class Funcionario(Pessoa):
    # TODO: CONSTRUIR FUNCIONARIO
    pass

class Cliente(Pessoa):
    # TODO: CONSTRUIR CLIENTE
    def __init__(self, email):
        self.email = email

    def getCPF(self):
        return self.getCPF

class Promocao:
    # TODO: CONSTRUIR PROMOÇÃO
    def enviarEmail(self, email):
        print(f'E-mail enviado para {email}')

class Localiza:
    def __init__(self, promocao):
        self.carros = []
        self.clientes = []
        self.funcionarios = []
        self.reservas = []
        self.promocao = promocao

    def enviarPromoca(self):
        for cliente in self.clientes:
            self.promocao.enviarEmail(cliente.email)

    def solicitarRervar(self, cliente):
        if self.verificarCliente(cliente):
            print("Solicitação da reserva aprovada!")
        else:
            print("Solicitação da reserva reprovada!")

    def verificarCliente(self, cliente):
        for reserva in self.reservas:
            if reserva.getStatus() == 'Ativa' and reserva.getCliente().getCPF() == cliente.getCPF():
                return False
        return True

    def verificarCarrosDisponiveis(self):
        # TODO: IMPLEMENTAR
        pass
