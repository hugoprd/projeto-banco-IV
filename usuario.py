class Usuario:
    tem_conta = False;

    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf;
        self.nome = nome;
        self.data_nascimento = data_nascimento;
        self.endereco = endereco;

    def setTem_Conta(tc):
        self._tem_conta = tc;