"""Module providing ApplyRulesToCreateGoodAndBadData class"""
import logging
import json
import sys
import os


# Configuração básica do logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Define o logger no início do arquivo


class NewDeafultStep():
    """Classe que apresenta o formato padrão de um Step Dadosfera"""

    def __init__(self) -> None:
        self.orchest_step_uuid = os.environ.get('ORCHEST_STEP_UUID')
        self.run()

    @staticmethod
    def custom_function(param_one, param_two):
        """Função responsável por fazer as funções específicas do step"""

        return "Step Output: {} {}".format(param_one, param_two)

    def main(self, param_one, param_two):
        """Função responsável por receber os parâmetros do step e orchestar as custom_functions"""

        logger.info(param_one)
        logger.info(param_two)

        response = self.custom_function(
            param_one=param_one, param_two=param_two)

        return response

    def module_handler(self):
        """Função responsável por executar o código quando estiver dentro do mádulo de inteligência"""
        import orchest

        param_one = orchest.get_step_param('param_one')
        param_two = orchest.get_step_param('param_two')

        # Chama a função get_outlook_contacts e passa os resultados para o Orchest.
        output = self.main(param_one=param_one, param_two=param_two)

        # Salva o resultado do step em uma variável do módulo de inteligência
        orchest.output(
            data=output, name=f"{self.__class__.__name__}_output")

    def local_handler(self):
        """Função responsável por executar o código quando estiver em desenvolvimento local"""
        if len(sys.argv) != 2:
            raise ValueError(
                "Please provide the required configuration in JSON format")
        config_json = sys.argv[1]
        config = json.loads(config_json)

        param_one = config.get('param_one')
        param_two = config.get('param_two')

        output = self.main(param_one=param_one, param_two=param_two)

        # Salva o resultado do step em um arquivo local
        with open(f"{self.__class__.__name__}_output", 'w', encoding='utf-8') as f:
            f.write(output)

    def run(self):
        """Gerencia o contexto em que o código esta sendo executado, definindo a função de entrada."""
        # Determina o modo de execução com base na variável de ambiente.
        if self.orchest_step_uuid is not None:
            logger.info('Running as an Orchest step')
            self.module_handler()
        else:
            logger.info('Running as standalone script')
            self.local_handler()


if __name__ == '__main__':
    NewDeafultStep()
