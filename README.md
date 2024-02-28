### Introdução

A Dadosfera utiliza uma abordagem modular baseada em steps para construir pipelines de dados. Cada step é uma unidade funcional que realiza uma tarefa específica, como leitura, transformação ou gravação de dados.

### Pré-requisitos

Antes de iniciar, certifique-se de ter conhecimento básico em processamento de dados, acesso à Dadosfera, e o ambiente configurado com as dependências necessárias.

### Estrutura do Step

Um step é composto por:

1. **Script (`step.py`):** Contém a lógica de processamento.
2. **JSON Schema (`step.py.schema.json`):** Define a estrutura de entrada.
3. **UI Schema (`step.py.uischema.json`):** Estrutura a interface de usuário.

### Exemplo de Configuração

1. **Configuração do Step:**

   - Acesse a Dadosfera e crie um novo step.
   - Configure os parâmetros `param_one` e `param_two` conforme necessário.

2. **Execução:**

   - Execute o step e monitore o progresso.

3. **Validação:**
   - Verifique a saída para confirmar a execução correta.

Este exemplo ilustra o processo básico. Adapte conforme a necessidade do seu pipeline.

O arquivo `step.py` define uma classe chamada `Step`, que encapsula a lógica de um step na Dadosfera. Esta classe contém métodos cruciais, como `custom_function`, que realiza a tarefa específica do step, e `main`, que orquestra a execução das funções customizadas com os parâmetros recebidos. Além disso, inclui métodos para lidar com a execução em diferentes ambientes (`module_handler` para a Dadosfera e `local_handler` para execução local), e `run`, que determina o contexto de execução e invoca o manipulador apropriado.

Este script é um exemplo de como organizar o código de um step, seguindo boas práticas como modularização, clareza e manutenibilidade. A estrutura facilita a compreensão do funcionamento do step e sua integração em pipelines de dados mais amplos na Dadosfera. Vou agora examinar os arquivos `.schema.json` e `.uischema.json` para fornecer detalhes adicionais sobre a configuração e a interface do usuário do step.

O arquivo `step.py.schema.json` define o esquema de validação para os parâmetros de entrada do step. Especifica que o step aceita dois parâmetros, `param_one` e `param_two`, ambos do tipo string. Além disso, estes parâmetros são obrigatórios para a execução do step, conforme indicado pela propriedade `required`. Esse esquema garante que os dados fornecidos ao step estejam de acordo com as expectativas antes de sua execução, contribuindo para a robustez e confiabilidade do pipeline de dados. Vamos prosseguir para examinar o arquivo `.uischema.json`.

O arquivo `step.py.uischema.json` organiza a interface de usuário para a configuração do step, utilizando um layout vertical que contém dois controles dispostos horizontalmente. Cada controle está associado a um dos parâmetros de entrada (`param_one` e `param_two`), e são acompanhados de etiquetas explicativas. Essa organização facilita a interação do usuário com o step, permitindo a configuração intuitiva dos parâmetros necessários para a execução do step na Dadosfera.

### Padrão ao construir um step

Ao criar um novo step na Dadosfera, siga estas convenções para garantir consistência e facilitar a manutenção:

- **Nomeação da Pasta:** Utilize o estilo Snake Case (separado_por_underlines) para o nome da pasta, refletindo claramente a funcionalidade do step.
- **Consistência dos Nomes de Arquivos:** Os nomes dos arquivos dentro da pasta devem corresponder ao nome da pasta, seguidos de suas respectivas extensões.
- **Convenção de Nomenclatura da Classe:** Nomeie a classe no arquivo `.py` usando Camel Case (SeparadoPorMaiusculas), conforme as boas práticas de Python, garantindo que o nome reflita a funcionalidade do step.

Estrutura de Arquivos de Exemplo:

```
feature_extractor
│
├── feature_extractor.py
├── feature_extractor.py.schema.json
└── feature_extractor.py.uischema.json
```

Dentro do `feature_extractor.py`, defina a classe principal seguindo o nome da pasta:

```python
class FeatureExtractor():
    ...
```

Esta estrutura padronizada promove uma organização clara e a facilidade de compreensão, além de facilitar a integração e a colaboração em projetos maiores.

O arquivo `new_default_step.py` apresenta um exemplo de como construir uma função customizada dentro de um step na Dadosfera. Vamos explorar a função `custom_function` detalhadamente para compreender sua construção e propósito.

### Construindo uma Função Customizada

Na classe `Step`, a função `custom_function` é um método estático projetado para realizar tarefas específicas do step. Esta função recebe dois parâmetros, `param_one` e `param_two`, e retorna uma string formatada que concatena esses parâmetros.

```python
@staticmethod
def custom_function(param_one, param_two):
    """Função responsável por executar tarefas específicas do step."""
    return "Step Output: {} {}".format(param_one, param_two)
```

#### Detalhes Importantes:

- **Método Estático:** `@staticmethod` indica que `custom_function` pode ser chamada sem criar uma instância da classe `Step`. Isso é útil para funções que realizam operações que não dependem do estado de um objeto específico.
- **Parâmetros de Entrada:** `param_one` e `param_two` são os parâmetros de entrada da função. Esses parâmetros podem ser de qualquer tipo, mas neste exemplo, são esperadas strings.
- **Retorno da Função:** A função retorna uma string que inclui os valores de `param_one` e `param_two`, demonstrando como os parâmetros de entrada podem ser manipulados dentro da função.

### Exemplo de Uso da Função Customizada

A função `custom_function` é utilizada dentro de outro método da classe, `main`, que atua como orquestrador, recebendo os parâmetros do step e passando-os para a função customizada.

```python
def main(self, param_one, param_two):
    """Orquestra a execução das funções customizadas com os parâmetros recebidos."""
    logger.info(param_one)
    logger.info(param_two)

    # Chama a função customizada e passa os parâmetros
    response = self.custom_function(param_one=param_one, param_two=param_two)

    return response
```

Este método ilustra como a `custom_function` pode ser integrada ao fluxo de trabalho do step, permitindo a modularização e reutilização do código. Ao definir funções customizadas desta forma, você pode construir steps mais complexos e adaptáveis às necessidades específicas do seu pipeline de dados.

### Gerenciamento de Dependências

A gestão correta das dependências é fundamental para garantir que o step funcione conforme esperado em diferentes ambientes. As dependências são bibliotecas e pacotes externos nos quais o seu código se baseia para executar tarefas específicas. Definir claramente essas dependências evita problemas relacionados à incompatibilidade de versões ou à falta de recursos necessários.

Para um step na Dadosfera, você pode especificar as dependências necessárias através de um script de instalação. Este script garante que todas as dependências sejam instaladas e configuradas corretamente antes da execução do step. Aqui está um exemplo de script de instalação para um ambiente Linux, utilizando `bash` e `pip3`:

```bash
#!/bin/bash

# Atualiza a biblioteca pyOpenSSL
pip3 install pyOpenSSL --upgrade

# Instala o AWS CLI e a biblioteca pandas
pip3 install awscli pandas

# Configura o login no AWS CodeArtifact
aws codeartifact login --tool pip --domain dadosfera --domain-owner 611330257153 --region us-east-1 --repository dadosfera-pip

# Instala as bibliotecas específicas da Dadosfera
pip3 install dadosfera==1.6.0b1 dadosfera_logs==1.0.3
```

#### Pontos Chave:

- **Atualização de Bibliotecas:** Garanta que bibliotecas essenciais, como `pyOpenSSL`, estejam atualizadas para evitar vulnerabilidades de segurança e incompatibilidades.
- **Instalação de Ferramentas e Bibliotecas:** O script instala ferramentas úteis como o AWS CLI e bibliotecas como `pandas`, que são comumente utilizadas em análise de dados.
- **Autenticação e Configuração de Repositórios:** A integração com o AWS CodeArtifact permite o gerenciamento seguro de artefatos de software e dependências, necessitando de uma configuração de login para acesso.
- **Dependências Específicas do Projeto:** Instala versões específicas de pacotes relacionados à Dadosfera, garantindo compatibilidade e estabilidade no ambiente de execução do step.

Incluir um script de instalação de dependências como parte da documentação do seu step auxilia outros desenvolvedores a preparar seus ambientes de forma eficiente, promovendo uma experiência de desenvolvimento mais fluída e prevenindo possíveis interrupções devido a problemas de dependência.

### Solução de Problemas (Troubleshooting)

Ao trabalhar com steps na Dadosfera e gerenciar suas dependências, você pode encontrar alguns desafios comuns. Aqui estão algumas dicas de solução de problemas para ajudá-lo a superar esses obstáculos:

#### Reinicie a Sessão Após Instalar Novas Dependências

Após executar o script de instalação de dependências, é essencial **reiniciar a sessão** em que você está trabalhando. Isso garante que todas as novas bibliotecas e atualizações sejam carregadas corretamente e estejam disponíveis para uso no seu ambiente. A reinicialização limpa o estado da sessão e evita conflitos ou problemas de carregamento de bibliotecas.

#### Verifique o Caminho das Dependências

Se, após reiniciar, você ainda enfrentar problemas relacionados à não localização das dependências, verifique se o caminho para as bibliotecas instaladas está corretamente configurado em seu ambiente. Às vezes, bibliotecas instaladas em locais não padrão podem não ser detectadas automaticamente.

#### Contate o Suporte da Dadosfera

Caso os problemas persistam e você não consiga resolver as questões relacionadas à instalação e configuração das dependências, não hesite em contatar o suporte da Dadosfera. A equipe de suporte pode oferecer assistência personalizada para diagnosticar e solucionar problemas específicos do seu ambiente ou configuração.

Lembrar-se dessas etapas de solução de problemas pode economizar tempo e evitar frustrações ao trabalhar com steps na Dadosfera. Certifique-se de documentar quaisquer soluções específicas que você descobrir, pois elas podem ser úteis para outros usuários que enfrentam problemas semelhantes.
