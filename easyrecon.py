#!/usr/bin/python3

import os
import socket

from dns_resolver import dns_direto, dns_reverso

def executar_dns():
	print("=== EasyRecon | Resolução DNS ===")
	host = input("\nDigite o IPv4 do host ou seu nome de domínio: ").strip()
	print()

	try:
		socket.inet_aton(host)
		resultado = dns_reverso(host)

	except OSError:
		resultado = dns_direto(host)
	
	print(resultado)
	print()

def main():
	while True:
		print("=== EasyRecon ===")
		print("\n1. Resolução DNS")
		print("0. Sair")

		escolha = input("\nDigite o número da opção desejada: ")

		if (escolha not in ["0", "1"]):
			print("\nEscolha uma opção válida.\n")

		if (escolha == "0"):
			print("\nEncerrando o programa...\n")
			break

		if (escolha == "1"):
			print()
			executar_dns()

if __name__ == "__main__":
	os.system("clear")
	main()
