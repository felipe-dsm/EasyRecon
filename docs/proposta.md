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
