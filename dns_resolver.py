import socket

def dns_reverso(ip):
	try:
		host_nome = socket.gethostbyaddr(ip)[0]
		return f"O nome do domínio do host é:\n{host_nome}."

	except socket.herror:
		return "Não foi possível encontrar o nome do domínio desse host."

def dns_direto(host_nome):
	try:
		lista_ip = socket.gethostbyname_ex(host_nome)[2]
		resultado = "Lista de endereços IPv4 associados ao nome do domínio:\n"

		for ip in lista_ip:
			resultado += f"- {ip}\n"

		return resultado.strip()

	except socket.gaierror:
		return "Não foi possível encontrar o endereço IPv4 desse host."
