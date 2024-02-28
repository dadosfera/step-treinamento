# Guia de Criação de Novos Steps

Este guia fornece instruções passo a passo sobre como criar e integrar um novo "step" ao sistema Dadosfera, utilizando os arquivos e estruturas de projeto fornecidos como base.

## Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes pré-requisitos instalados:

- Docker
- Docker Compose
- Python (versão correspondente à usada no `Dockerfile`, neste caso, 3.8)
- Acesso à AWS (se necessário para o seu step)

## Passo 1: Definir a Lógica do Step

1. Copie o arquivo `new_default_step.py` e renomeie-o de acordo com a funcionalidade do seu novo step (por exemplo, `my_custom_step.py`).
2. Modifique a classe copiada para implementar a lógica específica do seu step. Isto inclui:
   - Alterar o nome da classe para algo representativo do seu step.
   - Implementar a lógica específica dentro da função `custom_function`.
   - Ajustar qualquer outra parte do código conforme necessário para atender às necessidades do seu step.

## Passo 2: Definir o Esquema de Dados

1. Copie o arquivo `new_default_step.py.schema.json` e renomeie-o para corresponder ao seu novo step (por exemplo, `my_custom_step.schema.json`).
2. Modifique o esquema para refletir os dados de entrada que seu step espera. Isto inclui:
   - Atualizar as propriedades `param_one` e `param_two` com os nomes e descrições adequados aos seus parâmetros de entrada.
   - Adicionar ou remover propriedades conforme necessário para o seu step.

## Passo 3: Definir o Esquema da UI

1. Copie o arquivo `new_default_step.py.uischema.json` e renomeie-o para corresponder ao seu novo step (por exemplo, `my_custom_step.uischema.json`).
2. Modifique o esquema da UI para refletir como os usuários devem interagir com os parâmetros do seu step. Isto pode incluir:
   - Ajustar os rótulos (`label`) para corresponder aos seus novos parâmetros de entrada.
   - Modificar a estrutura de layout se necessário para melhorar a experiência do usuário.

## Passo 4: Configurar o Ambiente Docker

1. Atualize o `Dockerfile` se necessário, especialmente se o seu step requer novas dependências.
2. Atualize o `docker-compose.yml` para incluir quaisquer novas variáveis de ambiente ou configurações específicas do seu step.

## Passo 5: Testar o Novo Step

1. Rode o comando:
   ```bash
   python3 dev.py
   ```
2. Para limpar o ambiente rode:
   ```bash
   python3 clear.py
   ```
3. Verifique os logs e resultados para garantir que o step está funcionando como esperado.

## Passo 6: Documentação

1. Atualize este `README.md` com detalhes específicos do seu step, incluindo sua finalidade, como ele funciona e quaisquer informações relevantes para os usuários e desenvolvedores.

## Conclusão

Ao seguir estes passos, você será capaz de criar e integrar novos steps ao sistema Dadosfera, aproveitando as bases fornecidas para garantir a consistência e a qualidade dentro do ecossistema de steps.
