# Proposta — EasyRecon

## 1. Visão do produto

**Para** estudantes, curiosos e entusiastas iniciantes em segurança ofensiva  
**Que** encontram dificuldade para escolher comandos e parâmetros ao realizar suas primeiras atividades de reconhecimento  
**O EasyRecon é** uma ferramenta de linha de comando para reconhecimento de redes e serviços  
**Que** permite executar tarefas comuns de reconhecimento por meio de uma experiência simplificada  
**Diferente de** ferramentas abrangentes e com maior curva de aprendizado, como o Nmap  
**Nosso produto** oferece comandos diretos, configurações padrão e mensagens em português.

### Hipótese de valor

Acreditamos que estudantes, curiosos e entusiastas iniciantes em segurança ofensiva conseguirão realizar suas primeiras tarefas práticas de reconhecimento com menor dependência de consultas externas, porque o EasyRecon oferece comandos simples, configurações padrão e mensagens em português.

## 2. Definição do MVP

| No MVP | Fora do MVP |
|---|---|
| CLI em Python com menu interativo em português | Interface gráfica ou aplicação web |
| Validação de IP, domínio e rede CIDR | Varredura distribuída ou em grande escala |
| Resolução DNS direta e reversa | Enumeração DNS avançada |
| Descoberta de hosts por ping sweep | Técnicas de evasão e furtividade |
| Varredura de portas TCP, com portas comuns por padrão e intervalo opcional | Varredura UDP |
| Coleta básica de banners | Detecção de sistema operacional |
| Fluxo integrado de reconhecimento | Detecção e exploração de vulnerabilidades |
| Resultados organizados no terminal | Histórico persistente e banco de dados |
| Tratamento de erros e timeouts | Sistema de plugins |

### Critério de sucesso do MVP

O MVP será considerado funcional quando um iniciante conseguir iniciar o EasyRecon, informar um alvo válido, escolher e executar as ferramentas de reconhecimento em um ambiente autorizado e compreender os resultados apresentados em português. Entradas inválidas, timeouts e ausência de resposta deverão gerar mensagens claras, sem encerrar o programa inesperadamente.

## 3. Backlog inicial

O backlog inicial do EasyRecon é mantido no [GitHub Project do projeto](https://github.com/users/felipe-dsm/projects/2).

O quadro contém seis histórias de usuário, todas priorizadas e estimadas. As histórias foram distribuídas entre as três sprints de desenvolvimento conforme suas dependências e o valor entregue ao usuário.

## 4. Stack tecnológica e justificativa

| Tecnologia | Uso e justificativa |
|---|---|
| Python 3 | Linguagem principal, escolhida pela legibilidade, rapidez de desenvolvimento e suporte a operações de rede. Também permite aproveitar os conhecimentos adquiridos durante o curso de segurança ofensiva |
| Interface de linha de comando | Mantém o escopo viável e aproxima o produto do ambiente de terminal utilizado em segurança ofensiva |
| Biblioteca padrão do Python | Será priorizada para validação de endereços, sockets e operações de rede, reduzindo dependências externas |
| pytest | Permitirá criar testes automatizados para validações, tratamento de erros e componentes de rede simulados |
| GitHub Actions | Será utilizado para executar testes e verificações automaticamente em pushes e pull requests |
| Docker | Permitirá executar e testar o EasyRecon em um ambiente reproduzível nas sprints posteriores |

## 5. Acordo de processo

### Cadência e cerimônias

As sprints seguem as datas do cronograma da disciplina.

| Cerimônia | Frequência | Duração | Objetivo |
|---|---|---:|---|
| Planejamento | Início de cada sprint | 30 min | Selecionar o objetivo e mover os itens comprometidos para o Sprint Backlog |
| Acompanhamento | Duas vezes por semana | 10 min | Atualizar o quadro, registrar impedimentos e verificar os limites de WIP |
| Revisão | Final de cada sprint | 20 min | Executar o incremento e conferir os critérios de aceitação |
| Retrospectiva | Após a revisão | 30 min | Registrar fatos, dificuldades e uma melhoria para a sprint seguinte |

O projeto não terá reunião diária, pois possui apenas um integrante. O acompanhamento será registrado diretamente no GitHub Project e nas issues.

### Definição de Pronto

Uma história poderá ser movida para `Pronto` quando:

- [ ] Todos os critérios de aceitação estiverem satisfeitos.
- [ ] Os testes automatizados relacionados passarem localmente.
- [ ] A alteração tiver sido integrada à `main` por meio de pull request.
- [ ] O pull request possuir descrição, checklist e autorrevisão.
- [ ] O pull request referenciar e fechar a issue correspondente.
- [ ] A documentação afetada estiver atualizada.
- [ ] O uso de inteligência artificial estiver registrado, quando aplicável.
- [ ] Após a introdução da integração contínua, o pipeline estiver verde.

### Papéis

Como o projeto possui apenas um integrante, os papéis serão acumulados:

| Papel | Responsabilidade |
|---|---|
| Product Owner | Priorizar o backlog e aceitar ou recusar os resultados |
| Facilitador | Manter o processo, o quadro e as cerimônias |
| Desenvolvedor | Implementar, testar e documentar o produto |
| Revisor | Realizar uma autorrevisão do diff usando o checklist do pull request |

### Ferramentas

| Finalidade | Ferramenta |
|---|---|
| Código e documentação | Repositório GitHub |
| Backlog e fluxo | GitHub Issues e GitHub Projects |
| Revisão e integração | GitHub Pull Requests |
| Decisões e impedimentos | Issues, comentários e documentos do repositório |
| Testes | pytest |
| Integração contínua | GitHub Actions, a partir da Sprint 2 |
| Ambiente reproduzível | Docker, a partir da Sprint 2 |

### Limites de WIP

| Coluna | Limite |
|---|---:|
| Backlog | Sem limite |
| Sprint Backlog | 3 |
| Em progresso | 1 |
| Em revisão | 1 |
| Pronto | Sem limite |

Quando um limite for atingido, nenhum novo item será iniciado até que o trabalho em andamento avance.
