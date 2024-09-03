import loginbanco;
import usuario;
import clientebanco;

lista_usuarios = [];
lista_contas = [];
agencia = "0001";

# ============================================== CADASTRO USUARIO ==============================================
#ver se a string nao possui apenas o mesmo numero
def verificarNumeros(cpf):
    for i in len(cpf):
        if cpf[i] != cpf[0]:
            return False;

    return True;

#ver se existe um cpf igual ao que esta tentando se cadastrar na lista de usuarios cadastrados
def cpfIgual(cpf):
    if len(lista_usuarios) == 0:
        return False;
    for i in len(lista_usuarios):
        if lista_usuarios[i].cpf == cpf:
            return True;

    return False;

#verificar a primeira parte do cpf
def verificarParte1(cpf1, verificador):
    num = 0;
    aux = 10;
    verN = 0;

    for i in 9:
        numero += int(cpf1[i])*aux;

        aux -= 1;

    resto = numero % 11;

    if resto == 1 or resto == 0:
        verN = 0;
    elif resto >= 2 and resto <= 10:
        verN = 11 - resto;

    return verN == verificador[0];

#verificar a segunda parte do cpf
def verificarParte2(cpf2, verificador):
    numero = 0;
    aux = 11;
    verN = 0;

    for i in 10:
        numero += int(cpf2[i])*aux;

        aux -= 1;

    resto = numero % 11;

    if resto == 1 or resto == 0:
        verN = 0;
    elif resto >=2 and resto <=10:
        verN = 11 - resto;

    return verN == verificador[1];

#validar cpf da tentativa de cadastro
def validarCpf(rCpf):
    if len(rCpf) == 11:
        if rCpf.isdigit():
            if verificarNumeros(rCpf) == False:
                if cpfIgual(rCpf == False):
                    parte1 = rCpf[1, 10];
                    parte2 = rCpf[1, 11];
                    verificadorCpf = rCpf[9, 12];

                    if verificarParte1(parte1, verificadorCpf) and verificarParte2(parte2, verificadorCpf):
                        return rCpf;

                    else:
                        print("CPF invalido. Tente novamente.");
                else:
                    print("CPF invalido. Tente novamente.");
            else:
                print("CPF invalido. Tente novamente.");
        else:
            print("CPF invalido. Tente novamente.");
    else:
        print("CPF invalido. Tente novamente.");

#validar nome da tentativa de cadastro
def validarNome(rNome):
    if not rNome.isdigit():
        return rNome;
    else:
        print("Nome invalido. Tente novamente.");

#validar data de nascimento da tentativa de cadastro
def validarDataNascimento(rData):
    if len(rData) == 8:
        dia = rData[1:2];
        mes = rData[3:4];
        ano = rData[5:8];

        data += "/".join(dia);
        data += "/".join(mes);
        data += "/".join(ano);

        return data;
    else:
        print("Data invalida. Tente novamente.");

def cadastroUsuario():
    print("===================================================");
    print("================ Seja bem-vindo(a) ================");
    print("Digite suas informacoes a seguir para se cadastrar:");

    while True:
        while True:
            respostaCpf = input("\nCPF: ");
            cpfFinal = validarCpf(respostaCpf);
        
            if cpfFinal == respostaCpf:
                break;

        while True:
            respostaNome = input("\nNome: ");
            nomeFinal = validarNome(respostaNome);

            if nomeFinal == respostaNome:
                break;

        while True:
            resposta_nascimento = input("\nData de nascimento (apenas numeros): ");
            nascimentoFinal = validarDataNascimento(resposta_nascimento);

            if nascimentoFinal == resposta_nascimento:
                break;

        logradouro = "Rua {0}, {1} - {2}/{3}";
        print("\nEndereco: ");
        while True:
            respostaRua = input("\nRua: ");

            if not respostaRua.isdigit():
                print("Nome de rua invalido. Tente novamente.");
            else:
                break;
        while True:
            respostaNumero = input("\nNumero: ");

            if not respostaNumero.isalpha():
                print("Numero de endereco invalido. Tente novamente.");
            else:
                break;
        while True:
            print("Sigla do seu estado:");
            respostaSigla = input("\nSigla: ");

            if len(respostaSigla) > 2 or respostaSigla.isdigit():
                print("Sigla invalida. Tente novamente.");
            else:
                break;
        enderecoFinal = logradouro.format(respostaRua, respostaNumero, respostaSigla);
        
        usuario = usuario.Usuario(cpfFinal, nomeFinal, nascimentoFinal, enderecoFinal);

        print("Usuario cadastrado com sucesso.");
        print(f"\nCPF: {usuario.cpf}");
        print(f"\nNome: {usuario.nome}");
        print(f"\nData de nascimento: {usuario.data_nascimento}");
        print(f"\nEndereco: {usuario.endereco}");

# ============================================== CADASTRAR CONTA BANCO ==============================================
#verificar se o cpf digitado é válido e se já está cadastrado
def validarCadastro(cpf):
    cpfAux = validarCpf(cpf);

    if cpfAux == cpf:
        if len(lista_contas) >= 1:
            if not cpf in lista_contas:
                print("\nCPF nao cadastrado no sistema. Tente novamente.");
                return False;
            else:
                return True;
        else:
            print("\nNao ha nenhum CPF cadastrado no sistema. Tente novamente.");
            return False;


def cadastroBanco(usuarioX):
    print("============================================================");
    print("===================== Seja bem-vindo(a) ====================");
    print("Digite suas informacoes a seguir para se cadastrar no banco:");

    while True:
        resposta_cadastro = input("\nDigite o seu CPF: ");

        if validarCadastro(resposta_cadastro):
            num = 0;

            for conta in lista_contas:
                num = conta.numero_conta + 1;
            
            break;

    banco = banco.Banco(usuarioX.cpf, usuarioX.nome, usuarioX.data_nascimento, usuarioX.endereco, num);

    print("\nCadastro concluido.");
    print(f"\nConta {banco.num} do CPF {banco.cpf}");
    print(f"\nAgencia: {agencia}. Numero da conta: {banco.num}. Usuario: {banco.cpf}");

# ============================================== ENTRAR NO USUARIO E NA CONTA ==============================================
def entrarUsuario():
    while True:
        resposta_entrar = input("\nDigite o seu CPF: ");
        respostaFinal = validarCpf(resposta_entrar);

        if respostaFinal == resposta_entrar:
            for conta in lista_contas:
                if conta.cpf == respostaFinal:
                    nomeAux = conta.nome;
                    break;

            print(f"Seja bem-vindo(a) {nomeAux}");

            for conta in lista_contas:
                if conta.numero_conta

def main():

main();