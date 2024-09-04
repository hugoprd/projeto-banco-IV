import usuario;
import datetime;

class ClienteBanco(usuario.Usuario):
    saldo = 0;

    def __init__(self, cpf, nome, data_nascimento, endereco, numero_conta, saldo, extrato, transacoes):
        super().__init__(cpf, nome, data_nascimento, endereco);
        self.numero_conta = numero_conta;
        self.saldo = saldo;
        self.extrato = extrato;
        self.transacoes = transacoes;

    def log_transacao(func):
        def envelope(*args, **kwargs):
            resultado = func(*args, **kwargs);
            print(f"{datetime.now()}: {func.__name__.upper()}");
            return resultado;

    @log_transacao
    def depositar(self):
        print("\n[1]\tSelecionar Valor");
        print("\n[q]\tSair");

        while True:
            resposta_deposito = input("\n=> ");

            if resposta_deposito == 1:
                while True:
                    resposta_valor = float(input("\n=> "));

                    if resposta_valor <= 0:
                        print("\nNao eh possivel depositar R$ 0.00. Tente novamente.");
                    else:
                        self._saldo += resposta_deposito;
                        self._extrato += f"\nSaldo: {self._saldo}\nDeposito de R${resposta_deposito:.2f}.";
                        print(f"\nR${resposta_deposito:.2f} depositados na conta.");

                        break;
                
                break;
            elif resposta_deposito == "q" or resposta_deposito == "Q":
                break;
            else:
                print("\nResposta invalida. Tente novamente.");

    @log_transacao
    def sacar(self):
        print("\n[1]\tSelecionar Valor");
        print("\n[q]\tSair")

        while True:
            resposta_saque = input("\n=> ");
    
            if resposta_saque == 1:
                while True:
                    resposta_valor = float(input("\n=> "));

                    if resposta_valor > sal:
                        print("\nNao eh possivel sacar mais do que possue na conta. Tente novamente.");
                    elif resposta_valor <= 0:
                        print("\nNao eh possivel sacar R$ 0.00. Tente novamente.");
                    else:
                        self._saldo -= resposta_saque;
                        self._extrato += f"\nSaldo: {self._saldo}\nSaque de R${resposta_saque:.2f}.";
                        print(f"\nR${resposta_saque:.2f} sacados da conta.");
    
                        break;

                break;
            elif resposta_saque == "q" or resposta_saque == "Q":
                break;
            else:
                print("\nResposta invalida. Tente novamente.");

    @log_transacao
    def exibir_extrato(self):
        print("\n =============================================");
        print(self._extrato);

    def transacoes(self):
        return self._transacoes;

    #def adicionar_transacao(self, transacao):

    def gerar_relatorio(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao == None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao;