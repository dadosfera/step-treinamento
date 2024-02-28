"""Module providing ApplyRulesToCreateGoodAndBadData class"""
import logging
import os


# Configuração básica do logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Define o logger no início do arquivo


class TransformData():
    """Classe que apresenta o formato padrão de um Step Dadosfera"""

    def __init__(self) -> None:
        self.orchest_step_uuid = os.environ.get('ORCHEST_STEP_UUID')
        self.run()

    @staticmethod
    def transform_data(df, selected_columns):
        """Seleciona colunas especificadas de um DataFrame."""
        # Verifica se todas as colunas selecionadas estão presentes no DataFrame
        selected_columns_list = selected_columns.split(',')
        for column in selected_columns_list:
            if column not in df.columns:
                raise ValueError(
                    f"A coluna '{column}' não existe no DataFrame.")

        # Seleciona as colunas especificadas
        transformed_df = df[selected_columns]
        return transformed_df

    def main(self, df, selected_columns):
        """Função responsável por receber os parâmetros do step e orchestar as custom_functions"""

        logger.info(selected_columns)

        response = self.transform_data(
            df=df, selected_columns=selected_columns)

        return response

    def module_handler(self):
        """Função responsável por executar o código quando estiver dentro do mádulo de inteligência"""
        import orchest

        selected_columns = orchest.get_step_param('selected_columns')
        output_name = orchest.get_step_param('output_name')
        incoming_variable_name = orchest.get_step_param(
            'incoming_variable_name')

        df = orchest.get_inputs()[incoming_variable_name]

        # Chama a função get_outlook_contacts e passa os resultados para o Orchest.
        output = self.main(df=df, selected_columns=selected_columns)

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
    TransformData()
