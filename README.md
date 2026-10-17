# EasyRecon

O **EasyRecon** é uma ferramenta de linha de comando que reúne, em um único programa, recursos de reconhecimento utilizados na área de cibersegurança.

O projeto busca oferecer a iniciantes e entusiastas uma experiência intuitiva, reduzindo a barreira de entrada encontrada em ferramentas tradicionais mais abrangentes, como o Nmap.

## Equipe

- **Felipe Dantas de Souza Macedo**
  - Matrícula: 20240011697
  - GitHub: [@felipe-dsm](https://github.com/felipe-dsm)

## Coorte

**Coorte B — online**

## Integração com outras disciplinas

Não se aplica.

## Funcionalidades planejadas

- Resolução DNS direta e reversa
- Descoberta de hosts por ping sweep
- Varredura de portas TCP
- Coleta básica de banners
- Fluxo integrado de reconhecimento

As funcionalidades serão desenvolvidas progressivamente durante as próximas sprints. O EasyRecon deve ser utilizado somente em redes e sistemas próprios ou devidamente autorizados.

## Funcionalidades disponíveis

Nesta versão, o EasyRecon oferece:

- Resolução DNS direta, convertendo um nome de domínio em endereços IPv4.
- Resolução DNS reversa, consultando o registro PTR associado a um endereço IPv4.
- Menu interativo em português.
- Tratamento de erros quando a consulta não retorna resultados.

## Requisitos

- Python 3
- Acesso à rede para realizar consultas DNS

O EasyRecon utiliza somente a biblioteca padrão do Python durante sua execução.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/felipe-dsm/EasyRecon.git
cd EasyRecon
```
## Documentação

- [Proposta do produto](docs/proposta.md)
- [Backlog e quadro do projeto](https://github.com/users/felipe-dsm/projects/2)
- [Registro do uso de inteligência artificial](docs/uso-de-ia.md)
- [Vídeo de apresentação da Sprint 0](https://youtu.be/aFlgH47uOUk)
