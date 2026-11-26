# Data Summary Report

Open-Meteo — https://open-meteo.com/en/docs — API JSON de previsão meteorológica; temperatura (°C), umidade (%), precipitação (mm), vento (km/h), horário local. Uso: acompanhamento de condições meteorológicas previstas; não confundir previsão com observação. Consulta por latitude e longitude de São Paulo. Integração opcional no código; disponibilidade e condições de uso devem ser verificadas.
IBGE — https://servicodados.ibge.gov.br/api/docs/localidades — API JSON de localidades, códigos e nomes de municípios; uso futuro: seleção territorial e padronização de nomes. Não integrada no TP1.
Amostra local: data/raw/amostra.csv, três registros fictícios para testar a interface, sem valor científico. Campos: cidade, horario, temperatura, umidade, precipitacao, vento. Qualidade planejada: verificar nulos, duplicatas, tipos, umidade entre 0 e 100 e precipitação não negativa. Registrar origem e horário de coleta. Não coletar dados pessoais.
## TP2
ONU Brasil: https://brasil.un.org/pt-br/sdgs/13 — HTML público, extração de títulos e parágrafos com Beautiful Soup, condicionada a permissões e termos de uso. Saída data/raw/agenda2030.csv: texto, fonte, coletado_em (UTC). Uso: frequência de termos e nuvem de palavras; não representa notícias nem opinião pública. Coleta ainda não executada neste ambiente. Upload: CSV com as seis colunas da amostra, origem identificada como usuário, validação de tipos e limites, remoção de duplicatas exatas no upload. Dados importados ficam na sessão, não em armazenamento permanente. IBGE continua planejado, não integrado.
## Atualização do Data Summary Report — TP3

**Projeto:** EcoMonitor Brasil

**Responsável:** Alicia Scripelliti

### 1. Descrição dos dados

O projeto utiliza dados climáticos e conteúdos relacionados ao meio ambiente, à sustentabilidade e à Agenda 2030.

### 2. Fontes de dados

- Open-Meteo: obtenção de informações climáticas.
- Web scraping com Beautiful Soup: extração de conteúdos ambientais.
- Arquivos CSV: armazenamento e organização dos registros.
- FastAPI: consulta e inclusão de registros climáticos.

### 3. Estrutura dos dados climáticos

| Campo | Descrição |
|---|---|
| cidade | Localidade analisada |
| horario | Data e horário do registro |
| temperatura | Temperatura em graus Celsius |
| umidade | Umidade relativa do ar |
| precipitacao | Precipitação em milímetros |
| vento | Velocidade do vento em km/h |

### 4. Armazenamento e organização

Os arquivos de dados são organizados no diretório data/ do projeto, permitindo sua utilização nas análises e visualizações da aplicação Streamlit.

### 5. Integração com FastAPI

A API desenvolvida disponibiliza os seguintes endpoints:

| Método | Endpoint | Finalidade |
|---|---|---|
| GET | / | Verificar o funcionamento da API |
| GET | /dados | Consultar registros climáticos |
| POST | /dados | Adicionar novos registros |
| GET | /docs | Acessar a documentação Swagger |

### 6. Validação e testes

Foram realizados testes de comunicação entre Streamlit e FastAPI, obtendo os seguintes resultados:

- Conexão com a API realizada com sucesso.
- Consulta GET executada com retorno HTTP 200.
- Envio POST executado com retorno HTTP 201.
- Exibição dos registros na interface Streamlit.

Os registros fictícios utilizados nos testes devem ser identificados e separados dos dados reais antes das análises.

### 7. Decisão sobre Selenium

Nesta etapa, priorizou-se a utilização de APIs e Beautiful Soup, mantendo a simplicidade da arquitetura. O Selenium poderá ser incorporado futuramente caso novas fontes exijam interação com páginas dinâmicas.

### 8. Preparação para integração com LLMs

Os dados estruturados e os conteúdos ambientais poderão ser utilizados futuramente em aplicações de inteligência artificial, incluindo:

- Geração automática de relatórios ambientais.
- Resumos de conteúdos sobre sustentabilidade.
- Classificação de sentimentos em textos ambientais.
- Assistente inteligente de perguntas e respostas.
- Geração de insights a partir dos indicadores climáticos.

Os cálculos estatísticos deverão ser realizados com Python, utilizando os LLMs para interpretação e comunicação dos resultados.

### 9. Limitações

A qualidade das análises depende da disponibilidade, atualização e confiabilidade das fontes. Os dados deverão ser validados antes de serem utilizados por modelos de linguagem.

### 10. Conclusão

A evolução do EcoMonitor Brasil no TP3 amplia as possibilidades de interação com os dados por meio de múltiplas páginas e integração com FastAPI, preparando a aplicação para a futura incorporação de inteligência artificial.
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