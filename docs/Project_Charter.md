# Project Charter

Problema: informações climáticas dispersas dificultam o planejamento ambiental de organizações. A solução centraliza indicadores de temperatura, umidade, precipitação e vento. Pilar ESG: ambiental. ODS 13 (ação climática, especialmente conscientização e capacidade de adaptação) e ODS 11 (planejamento de cidades sustentáveis). O painel não mede diretamente emissões nem comprova impacto ambiental.
Público: gestores ambientais, ONGs, empresas, pesquisadores e estudantes. Stakeholders: autora Alicia Scripelliti (desenvolvimento), professor (avaliação) e usuários potenciais (validação futura).
Escopo TP1: planejamento, amostra sintética, demo Streamlit e coleta opcional via API. Fora do escopo atual: alertas oficiais, previsão própria, scraping e LLMs em produção.
Metas: duas fontes integradas até o final do projeto; quatro indicadores; três gráficos; completude mínima de 95% (campos preenchidos / campos esperados); interface validada por três usuários em etapa futura. Critério TP1: abrir a demo, visualizar tabela e identificar fontes. Riscos: indisponibilidade da API, dados faltantes, interpretação incorreta e dependência de internet. Mitigação: timeout, amostra local identificada, validação e documentação de unidades.
## TP2
Escopo: filtros por cidade e origem, gráficos, scraping do ODS 13, frequência de palavras, cache de 15 minutos para API, upload CSV validado, exportação e estado de sessão. Stakeholders e metas do TP1 mantidos; aceitação: executar cada item do roteiro de testes, publicar repositório e documentar evidências. Riscos adicionais: alterações no HTML, permissões de coleta, arquivos inválidos e confusão entre fontes. Mitigação: verificar robots.txt e termos, identificar origem, validar CSV e tratar falhas. LLM e alertas oficiais permanecem fora do escopo.
## Atualização do projeto — TP3

### Projeto: EcoMonitor Brasil

**Responsável:** Alicia Scripelliti

### Problema de negócio

A dificuldade de centralizar, consultar e interpretar informações climáticas e ambientais pode prejudicar a tomada de decisões relacionadas à sustentabilidade.

### Objetivo geral

Desenvolver uma plataforma interativa de monitoramento ambiental, alinhada aos ODS 11 e 13 da Agenda 2030, facilitando o acesso aos indicadores climáticos e aos conteúdos sobre sustentabilidade.

### Público-alvo

Gestores, empresas, organizações não governamentais, estudantes e pesquisadores interessados em sustentabilidade ambiental.

### Evolução do projeto no TP3

- Implementação de múltiplas páginas utilizando Streamlit.
- Criação de um menu lateral de navegação.
- Desenvolvimento de uma API própria utilizando FastAPI.
- Implementação de endpoints GET e POST.
- Integração entre Streamlit e FastAPI.
- Documentação interativa da API por meio do Swagger.
- Preparação para futura utilização de modelos de linguagem (LLMs).

### Tecnologias utilizadas

- Python.
- Streamlit.
- FastAPI.
- Uvicorn.
- Pydantic.
- Pandas.
- Requests.
- Beautiful Soup.
- Open-Meteo.
- Git e GitHub.

### Decisões técnicas

Optou-se pela manutenção da coleta de dados por APIs e Beautiful Soup, considerando que as fontes utilizadas não exigem interação dinâmica com elementos JavaScript. Dessa forma, a utilização do Selenium não é necessária nesta etapa.

### Resultados alcançados

Os testes de integração demonstraram que a aplicação consegue estabelecer comunicação com a FastAPI, consultar registros climáticos e enviar novos dados por meio da interface Streamlit.

### Próximas etapas

Integrar modelos de linguagem para geração automática de relatórios, resumos de conteúdos ambientais e desenvolvimento de um assistente inteligente de perguntas e respostas.
# EcoMonitor Brasil — TP5

## 1. Objetivo do projeto

O EcoMonitor Brasil tem como objetivo facilitar o acesso e a interpretação de informações ambientais, utilizando ciência de dados e inteligência artificial para apoiar decisões relacionadas à sustentabilidade, ESG e Agenda 2030.

## 2. Atualização do Project Charter

O projeto evoluiu para uma aplicação integrada que reúne coleta, processamento, visualização e análise automatizada de informações ambientais.

O público-alvo inclui estudantes, pesquisadores e profissionais interessados em sustentabilidade.

A solução busca reduzir o esforço necessário para interpretar grandes volumes de informações textuais.

## 3. Atualização do Data Summary Report

O projeto utiliza dados climáticos e conteúdos relacionados à Agenda 2030, trabalhando com APIs, web scraping e arquivos CSV.

Os dados são organizados no diretório data/, processados e apresentados por meio de tabelas, indicadores e gráficos interativos.

Os registros fictícios utilizados nos testes da API não representam observações climáticas reais.

## 4. Ciclo de ciência de dados

- Entendimento do problema de negócio.
- Coleta de dados via APIs e web scraping.
- Limpeza e organização dos dados.
- Análise exploratória.
- Processamento textual com inteligência artificial.
- Visualização e apresentação dos resultados.

## 5. Escolha da solução com LLM

Foi selecionada a opção 2: Automação de Sumarização de Textos com LLMs.

O modelo escolhido foi o Google FLAN-T5 Small, disponibilizado pela Hugging Face, devido ao seu custo computacional relativamente reduzido e à possibilidade de execução local sem contratação de serviços de IA online.

## 6. Engenharia de prompts

A engenharia de prompts orienta o modelo de linguagem na tarefa de sumarização dos conteúdos ambientais.

Exemplo de prompt para sumarização:

“Summarize the following text, highlighting its main environmental and sustainability information.”

O objetivo é produzir textos mais curtos, preservando as informações relevantes do conteúdo original.

## 7. Arquitetura da solução

A aplicação utiliza as seguintes tecnologias:

- Python.
- Streamlit.
- Pandas.
- FastAPI.
- Beautiful Soup.
- Hugging Face Transformers.
- PyTorch.
- FLAN-T5 Small.
- Git e GitHub.

## 8. Dashboard final

O dashboard permite selecionar bases de dados, visualizar registros, acompanhar indicadores de processamento e gerar resumos automáticos.

Os resultados da inteligência artificial são apresentados em tabelas e gráficos comparativos.

## 9. Testes e resultados

O teste realizado com a base agenda2030.csv demonstrou o processamento de cinco textos relacionados aos Objetivos de Desenvolvimento Sustentável.

A aplicação apresentou os textos originais, os resumos gerados e um gráfico comparativo.

O teste confirmou o funcionamento da sumarização integrada ao dashboard, mas não constitui uma avaliação quantitativa da precisão do modelo.

## 10. Alinhamento com ESG e ODS

O projeto está relacionado principalmente aos seguintes objetivos:

- ODS 11 — Cidades e comunidades sustentáveis.
- ODS 12 — Consumo e produção responsáveis.
- ODS 13 — Ação contra a mudança global do clima.

A solução contribui para a organização e disseminação de informações ambientais, apoiando práticas de sustentabilidade e governança informacional.

## 11. Limitações

O modelo pode gerar respostas em inglês, omitir informações relevantes ou produzir interpretações imprecisas.

Os resultados devem ser revisados por pessoas antes de serem utilizados em decisões.

O desempenho depende dos recursos computacionais disponíveis.

## 12. Conclusão

O EcoMonitor Brasil demonstra a integração entre ciência de dados, sustentabilidade e inteligência artificial local.

A solução reúne coleta, processamento, análise e apresentação de informações em uma aplicação interativa, facilitando a compreensão de conteúdos ambientais e apoiando decisões relacionadas aos ODS e ESG.

## 13. Referências

- https://huggingface.co/google/flan-t5-small
- https://huggingface.co/docs/transformers/
- https://fastapi.tiangolo.com/
- https://streamlit.io/
- https://pytorch.org/
- https://brasil.un.org/pt-br/sdgs