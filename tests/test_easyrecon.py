import easyrecon

def test_executar_dns_usa_resolucao_direta_para_dominio(
    monkeypatch,
    capsys,
):
    def simular_ipv4_invalido(host):
        raise OSError

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "exemplo.com",
    )
    monkeypatch.setattr(
        easyrecon.socket,
        "inet_aton",
        simular_ipv4_invalido,
    )
    monkeypatch.setattr(
        easyrecon,
        "dns_direto",
        lambda host: "resultado da resolução direta",
    )

    easyrecon.executar_dns()

    saida = capsys.readouterr().out

    assert "resultado da resolução direta" in saida


def test_executar_dns_usa_resolucao_reversa_para_ipv4(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "192.0.2.10",
    )
    monkeypatch.setattr(
        easyrecon.socket,
        "inet_aton",
        lambda host: b"",
    )
    monkeypatch.setattr(
        easyrecon,
        "dns_reverso",
        lambda host: "resultado da resolução reversa",
    )

    easyrecon.executar_dns()

    saida = capsys.readouterr().out

    assert "resultado da resolução reversa" in saida


def test_main_avisa_sobre_opcao_invalida_e_permite_sair(
    monkeypatch,
    capsys,
):
    respostas = iter(["9", "0"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: next(respostas),
    )

    easyrecon.main()

    saida = capsys.readouterr().out

    assert "Escolha uma opção válida" in saida
    assert "Encerrando o programa" in saida
