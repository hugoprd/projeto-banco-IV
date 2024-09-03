import clientebanco;

class LoginBanco(clientebanco.ClienteBanco):
    def __init__(self, agencia, saldo, extrato, numero_conta, cpf, nome, data_nascimento, endereco):
        super().__init__(numero_conta, cpf, nome, data_nascimento, endereco);
        self.agencia = agencia;
        self.saldo = saldo;
        self.extrato = extrato;

    def saque():


    def deposito():


    def extrato():