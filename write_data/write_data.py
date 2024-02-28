"""Module providing ApplyRulesToCreateGoodAndBadData class"""
import logging
import os


# Configuração básica do logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Define o logger no início do arquivo


class WriteData():
    """Classe que apresenta o formato padrão de um Step Dadosfera"""

    def __init__(self) -> None:
        self.orchest_step_uuid = os.environ.get('ORCHEST_STEP_UUID')
        self.run()

    @staticmethod
    def write_data(df, destination):
        """Escreve o DataFrame transformado para um destino especificado."""
        # Exemplo: Escrever em um arquivo CSV
        df.to_csv(destination, index=False)

    def main(self, destination, df):
        """Função responsável por receber os parâmetros do step e orchestar as custom_functions"""

        logger.info(destination)

        response = self.write_data(df=df, destination=destination)

        return response

    def module_handler(self):
        """Função responsável por executar o código quando estiver dentro do mádulo de inteligência"""
        import orchest

        destination = orchest.get_step_param('destination')
        incoming_variable_name = orchest.get_step_param(
            'incoming_variable_name')

        df = orchest.get_inputs()[incoming_variable_name]

        # Chama a função get_outlook_contacts e passa os resultados para o Orchest.
        self.main(destination=destination, df=df)

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
    WriteData()
