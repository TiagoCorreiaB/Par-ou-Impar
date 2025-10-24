import random

print("-" * 35)
print("        JOGO PAR OU IMPAR")
print("-" * 35)

resp_poui = ""
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resps = ["par", "impar"]
n_maq = 0
resp_maq = ""
contv = 0
contd = 0
resp_soun = ''


def verificacao_parimpar(numero):
    if numero % 2 == 0:
        resp = "P"
    else:
        resp = "I"
    return resp


while resp_soun != "encerrar":

    resp_poui = input("Digite, qual será sua escolha nessa rodada? [PAR/IMPAR]: ").lower()
    n = ""

    while resp_poui not in resps:
        print("ERRO!!![OPÇÃO INVÁLIDA]")
        resp_poui = input("Digite, qual será sua escolha nessa rodada? [PAR/IMPAR]: ").lower()

    while n not in num:
        n = int(input("Digite um valor entre 0 e 10: "))
        if n not in num:
            print("ERRO!!![OPÇÃO INVÁLIDA]")

    n_maq = random.randint(0, 10)
    print(f'O número escolhido pela máquina foi: {n_maq}')
    soma = n + n_maq
    print(f'A soma entre seu número e o número da máquina foi de: {soma}')
    print("-" * 40)

    if resp_poui == "par":
        resp_maq = "impar"
        respverificacao = verificacao_parimpar(soma)
        if (respverificacao == "P"):
            print("VITÓRIA!!!")
            contv += 1
        else:
            print("DERROTA!!!")
            contd += 1

    if resp_poui == "impar":
        resp_maq = "par"
        respverificacao = verificacao_parimpar(soma)
        if respverificacao == "I":
            print("VITÓRIA!!!")
            contv += 1
        else:
            print("DERROTA!!!")
            contd += 1

    verificacao_fim = True

    while verificacao_fim:
        resp_soun = input("Deseja jogar mais uma vez ou encerrar? [jogar/encerrar] ").lower()
        print("-" * 40)
        if resp_soun == "jogar" or resp_soun == "encerrar":
            break
        else:
            print("ERRO!!![OPÇÃO INVÁLIDA]")

    if resp_soun == "encerrar":
        break

print(f"A quantidade de vitórias é de: {contv}")
print(f"A quantidade de derrotas é de: {contd}")