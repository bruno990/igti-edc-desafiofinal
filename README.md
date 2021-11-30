# Desafio final do Bootcamp Engenheiro de Dados Cloud do IGTI

O desafio consiste em:
1. Criar um cluster Kubernetes para a realização das atividades (Utilizado EKS).
2. Realizar a instalação e configuração do Spark Operator
3. Realizar a instalação e configuração de outas ferramentas que se deseje utilizar
(Airflow, Argo CD etc.).
4. Realizar a ingestão dos dados do Censo da Educação Superior 2019 no AWS S3. Dados disponíveis em <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior>. 
Os dados devem ser ingeridos de maneira automatizada na zona raw ou zona crua ou zona bronze do seu Data Lake.
5. Utilizar o SparkOperator no Kubernetes para transformar os dados no formato parquet e escrevê-los na zona staging ou zona silver do seu data lake.
6. Fazer a integração com alguma engine de data lake. No caso da AWS, você deve:  
    a. Configurar um Crawler para a pasta onde os arquivos na staging estão depositados;  
    b. Validar a disponibilização no Athena.

8. Use a ferramenta de Big Data ou a engine de Data Lake para investigar os dados e responder às perguntas do desafio.