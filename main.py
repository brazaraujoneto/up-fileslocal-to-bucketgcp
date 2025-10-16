import os
import logging # Biblioteca para log
from google.cloud import storage 
from google.api_core import exceptions

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def upload_to_gcp(bucket_name, source_directory, destination_folder):
    try:
        # Caminho para o arquivo de credenciais JSON
        credentials_path = r"ADICIONE AQUI O SEU CAMINHO\seu_arquivo_de_credenciais.json"

        # Carrega as credenciais explicitamente e cria o cliente
        storage_client = storage.Client.from_service_account_json(credentials_path)

        bucket = storage_client.bucket(bucket_name)

        if not os.path.exists(source_directory):
            logging.error(f"ERRO: O diretório de origem '{source_directory}' não existe.")
            return


        for root, dirs, files in os.walk(source_directory):
            for file in files:
                source_file_path = os.path.join(root, file)

                relative_path = os.path.relpath(source_file_path, source_directory)
                destination_blob_name = os.path.join(destination_folder, relative_path).replace("\\", "/")

                logging.info(f"Preparando para enviar o arquivo: {source_file_path}")


                blob = bucket.blob(destination_blob_name)
                blob.upload_from_filename(source_file_path)

                logging.info(f"SUCESSO: Arquivo '{file}' enviado para '{destination_blob_name}' no bucket '{bucket_name}'.")

    except exceptions.NotFound:
        logging.error(f"ERRO: O bucket '{bucket_name}' não foi encontrado. Verifique o nome do bucket.")
    except exceptions.Forbidden as e:
        logging.error(f"ERRO DE PERMISSÃO: Verifique se a conta de serviço tem permissão para escrever no bucket. Detalhes: {e}")
    except Exception as e:
        logging.error(f"FALHA no upload: {e}")

if __name__ == "__main__":

    NOME_DO_BUCKET = "seu-nome-do-bucket-aqui"
    DIRETORIO_ORIGEM = r"ADICIONE AQUI O SEU CAMINHO\diretorio_origem"

    PASTA_DESTINO_NO_BUCKET = "pasta_destino_no_bucket"

    logging.info("--- Iniciando script de upload ---")
    upload_to_gcp(NOME_DO_BUCKET, DIRETORIO_ORIGEM, PASTA_DESTINO_NO_BUCKET)
    logging.info("--- Script finalizado ---")