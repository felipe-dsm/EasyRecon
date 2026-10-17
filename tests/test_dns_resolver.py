import socket
import dns_resolver

def test_dns_direto_retorna_enderecos_ipv4(monkeypatch):
    def resposta_falsa(host_nome):
        return host_nome, [], ["192.0.2.10", "192.0.2.20"]

    monkeypatch.setattr(
        dns_resolver.socket,
        "gethostbyname_ex",
        resposta_falsa,
    )

    resultado = dns_resolver.dns_direto("exemplo.com")

    assert resultado == (
        "Lista de endereços IPv4 associados ao nome do domínio:\n"
        "- 192.0.2.10\n"
        "- 192.0.2.20"
    )

def test_dns_direto_trata_dominio_nao_encontrado(monkeypatch):
    def simular_erro(host_nome):
        raise socket.gaierror("Falha simulada")

    monkeypatch.setattr(
        dns_resolver.socket,
        "gethostbyname_ex",
        simular_erro,
    )

    resultado = dns_resolver.dns_direto("dominio-inexistente.test")

    assert resultado == "Não foi possível encontrar o endereço IPv4 desse host."


def test_dns_reverso_retorna_nome_do_host(monkeypatch):
    def resposta_falsa(ip):
        return "exemplo.com", [], [ip]

    monkeypatch.setattr(
        dns_resolver.socket,
        "gethostbyaddr",
        resposta_falsa,
    )

    resultado = dns_resolver.dns_reverso("192.0.2.10")

    assert resultado == "O nome do domínio do host é:\nexemplo.com."


def test_dns_reverso_trata_host_nao_encontrado(monkeypatch):
    def simular_erro(ip):
        raise socket.herror("Falha simulada")

    monkeypatch.setattr(
        dns_resolver.socket,
        "gethostbyaddr",
        simular_erro,
    )

    resultado = dns_resolver.dns_reverso("192.0.2.10")

    assert resultado == "Não foi possível encontrar o nome do domínio desse host."
