# ☁️ Upload Automatizado para o Google Cloud Storage

*Script Python para migração e sincronização de diretórios locais com buckets do GCP.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)

---

## 🎯 Sobre o Projeto

Este projeto automatiza o processo de upload de arquivos de um ambiente local diretamente para um **Google Cloud Storage Bucket**. O script foi desenhado para percorrer recursivamente diretórios e subpastas, replicando a exata estrutura de arquivos local no ambiente em nuvem, garantindo integridade e organização dos dados.

## ✨ Funcionalidades

* **Autenticação Segura:** Conexão nativa com o GCP via chave de Conta de Serviço (Service Account).
* **Varredura Recursiva:** Mapeia automaticamente todas as subpastas e arquivos da origem.
* **Espelhamento de Estrutura:** Mantém a hierarquia de pastas intacta no Cloud Storage.
* **Logging Detalhado:** Monitoramento da execução via console, com registro claro de sucessos e falhas em cada upload.

## ⚙️ Pré-requisitos

Para rodar esta automação, você precisará configurar o ambiente no Google Cloud e na sua máquina local.

### 1. Google Cloud Platform (GCP)
* **Projeto Ativo:** Crie ou utilize um projeto existente no [Google Cloud Console](https://console.cloud.google.com/).
* **API Habilitada:** Ative a **Google Cloud Storage API** no seu projeto.
* **Conta de Serviço (Credentials):** 
   * Crie uma Conta de Serviço com permissões de gravação no Storage (ex: *Storage Object Admin*).
   * Gere a chave em formato **JSON** e salve-a na raiz deste projeto.

### 2. Ambiente Local
* **Python 3.x** instalado na máquina.
* Gerenciador de pacotes `pip`.

## 🚀 Como Executar

1. Clone este repositório para a sua máquina local:
```bash
git clone https://github.com/brazaraujoneto/up-fileslocal-to-bucketgcp.git
