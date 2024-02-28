"""Module providing ApplyRulesToCreateGoodAndBadData class"""
import logging
import os
import pandas as pd


# Configuração básica do logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Define o logger no início do arquivo


class ReadData():
    """Classe que apresenta o formato padrão de um Step Dadosfera"""

    def __init__(self) -> None:
        self.orchest_step_uuid = os.environ.get('ORCHEST_STEP_UUID')
        self.run()

    @staticmethod
    def custom_function(source):
        """Lê dados de uma fonte especificada e retorna um DataFrame."""
        # Exemplo: Ler de um arquivo CSV
        if source.endswith('.csv'):
            df = pd.read_csv(source)
        # Adicione condições adicionais para outras fontes de dados conforme necessário
        else:
            raise ValueError("Tipo de fonte de dados não suportado.")
        return df

    def main(self, source_file_path):
        """Função responsável por receber os parâmetros do step e orchestar as custom_functions"""

        logger.info(source_file_path)

        response = self.custom_function(source=source_file_path)

        return response

    def module_handler(self):
        """Função responsável por executar o código quando estiver dentro do mádulo de inteligência"""
        import orchest

        source_file_path = orchest.get_step_param('source_file_path')
        output_name = orchest.get_step_param('output_name')

        # Chama a função get_outlook_contacts e passa os resultados para o Orchest.
        output = self.main(source_file_path=source_file_path)

        # Salva o resultado do step em uma variável do módulo de inteligência
        orchest.output(
            data=output, name=output_name)

    def run(self):
        """Gerencia o contexto em que o código esta sendo executado, definindo a função de entrada."""
        # Determina o modo de execução com base na variável de ambiente.
        if self.orchest_step_uuid is not None:
            logger.info('Running as an Module step')
            self.module_handler()
        else:
            logger.info(
                'Para executar esse código é necessário estar dentro do módulo.')


if __name__ == '__main__':
    ReadData()
