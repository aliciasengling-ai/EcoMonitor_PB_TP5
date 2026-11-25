# EcoMonitor Brasil — TP4

**Autora:** Alicia Scripelliti

## 1. Objetivo

Integrar um modelo de inteligência artificial executado localmente ao EcoMonitor Brasil, permitindo a geração automática de resumos de textos relacionados ao meio ambiente e à sustentabilidade.

## 2. Escolha do modelo

O modelo selecionado foi o Google FLAN-T5 Small, disponibilizado pela plataforma Hugging Face, com aproximadamente 80 milhões de parâmetros.

A escolha considerou os seguintes critérios:

- Desempenho adequado para tarefas básicas de resumo automático.
- Menor custo computacional em comparação com modelos de maior porte.
- Possibilidade de execução em CPU, sem necessidade obrigatória de GPU.
- Disponibilidade por meio da biblioteca Transformers.
- Ausência de custos por requisição a serviços externos de inteligência artificial.

O modelo foi executado com sucesso no ambiente de desenvolvimento local.

## 3. Integração local

Foram utilizadas as bibliotecas Transformers, PyTorch e SentencePiece para carregar e executar o modelo.

Após o download inicial, o carregamento foi configurado com o parâmetro `local_files_only=True`, permitindo a utilização dos arquivos armazenados localmente.

## 4. Integração com FastAPI

Foi implementado o endpoint POST `/processar_texto`, responsável por receber textos e retornar resumos automáticos.

A resposta utiliza um Response Model definido com Pydantic, contendo:

- Texto original.
- Tipo de análise.
- Resultado gerado.
- Modelo utilizado.
- Status do processamento.

## 5. Tratamento de erros

A API foi configurada para retornar os seguintes códigos HTTP:

| Código | Descrição |
|---|---|
| 200 | Processamento realizado com sucesso. |
| 400 | Texto inadequado para processamento. |
| 422 | Dados de entrada inválidos. |
| 500 | Erro interno durante o processamento. |
| 503 | Modelo local indisponível. |

Os códigos 200, 400 e 422 foram testados durante o desenvolvimento. Os tratamentos 500 e 503 foram implementados, mas ainda não foram validados por testes específicos.

## 6. Interface Streamlit

Foi desenvolvida uma página denominada Inteligência Artificial, permitindo que o usuário envie textos ambientais, visualize resumos gerados pelo modelo local e tenha acesso à opção de download do resultado.

## 7. Resultados dos testes

O modelo foi executado localmente, integrado ao FastAPI e acessado por meio da interface Streamlit.

Um dos testes realizados retornou o seguinte resumo:

"Solar and wind power are essential to reducing greenhouse gas emissions."

O resultado demonstra o funcionamento da integração entre a interface, a API e o modelo de linguagem.

## 8. Limitações

O modelo apresenta limitações na compreensão de textos em português e na geração de resumos complexos. Por esse motivo, os testes foram realizados com textos em inglês.

Os resumos podem omitir informações importantes e devem ser revisados pelo usuário.

## 9. Conclusão

O EcoMonitor Brasil evoluiu com a integração de inteligência artificial local, respostas estruturadas e mecanismos de tratamento de erros.

A solução está preparada para receber melhorias na próxima etapa do projeto.

## 10. Referências

- Hugging Face: https://huggingface.co/google/flan-t5-small
- Transformers: https://huggingface.co/docs/transformers/
- FastAPI: https://fastapi.tiangolo.com/
- PyTorch: https://pytorch.org/
- Streamlit: https://streamlit.io/