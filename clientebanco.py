import usuario;

class ClienteBanco(usuario.Usuario):
    def __init__(self, numero_conta, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento, endereco);
        self.numero_conta = numero_conta;