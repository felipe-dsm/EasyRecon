#!/usr/bin/python3

import os
import socket

from dns_resolver import dns_direto, dns_reverso


OPCOES_VALIDAS = {"0", "1"}


def resolver_alvo(host):
    try:
        socket.inet_aton(host)
    except OSError:
        return dns_direto(host)

    return dns_reverso(host)


def executar_dns():
    print("\n=== EasyRecon | Resolução DNS ===")

    host = input(
        "\nDigite o IPv4 do host ou seu nome de domínio: "
    )

    resultado = resolver_alvo(host)

    print(f"\n{resultado}")


def main():
    while True:
        print("\n=== EasyRecon ===")
        print("\n1. Resolução DNS")
        print("0. Sair")

        escolha = input(
            "\nDigite o número da opção desejada: "
        )

        if escolha not in OPCOES_VALIDAS:
            print("\nEscolha uma opção válida.\n")
            continue

        if escolha == "0":
            print("\nEncerrando o programa...\n")
            break

        if escolha == "1":
            os.system("clear")
            executar_dns()


if __name__ == "__main__":
    os.system("clear")
    main()
