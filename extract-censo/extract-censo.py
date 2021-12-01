import requests as rq
from zipfile import ZipFile
from io import BytesIO
import logging
from requests.exceptions import URLRequired
import boto3
from botocore.exceptions import ClientError
import os
import argparse

class Extract():

    def __init__(self, url, bucket_name=''):
        self.url = url
        self.bucket_name = bucket_name

    def download(self):
        self.arq = rq.get(self.url, stream=True)
        print(self.arq.status_code)
        return self.arq
    
    def extract(self, arq):
        z = ZipFile(BytesIO(arq.content))
        z.extractall(path='./tmp')

    def upload_file(self, object_name=None):

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(self.file_name)

        # Upload the file
        s3 = boto3.client('s3', region_name='us-east-2', 
        aws_access_key_id=os.getenv('aws_access_key_id'), aws_secret_access_key=os.getenv('aws_secret_access_key'))
        try:
            with open('raw/' + self.file_name, "rb") as f:
                response = s3.upload_fileobj(f, self.bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def run(self):
        arq = self.download()
        self.extract(arq)
        

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', default='https://download.inep.gov.br/microdados/microdados_educacao_superior_2019.zip',
                    help='URL para download do arquivo')
    parser.add_argument('--bucket_name',  dest='bucket_name', default='igti-edc-desafiofinal',
                    help='S3 Bucket Name')
    parser.add_argument('--file_path',  dest='file_path', default='./tmp/DADOS/ESCOLAS/ESCOLA_95.TXT',
                    help='File path for upload to S3')                    

    args = parser.parse_args()

    etl = Extract(url=args.url, bucket_name=args.bucket_name)
    etl.run()

    s3_client = boto3.client('s3', region_name='us-east-2', 
                        aws_access_key_id=os.getenv('aws_access_key_id'), 
                        aws_secret_access_key=os.getenv('aws_secret_access_key'))

    s3_upload_cfg = boto3.s3.transfer.TransferConfig()

    pasta = os.listdir('./tmp')

    print("Upload ALUNO")
    s3_client.upload_file(f"./tmp/{pasta[0]}/dados/SUP_ALUNO_2019.CSV", 
        "igti-edc-desafiofinal",
        "raw/censoedsup2019/aluno/SUP_ALUNO_2019.CSV",
        Config=s3_upload_cfg
    )

    print("Upload DOCENTE")
    s3_client.upload_file(f"./tmp/{pasta[0]}/dados/SUP_DOCENTE_2019.CSV", 
        "igti-edc-desafiofinal",
        "raw/censoedsup2019/docente/SUP_DOCENTE_2019.CSV",
        Config=s3_upload_cfg
    )

    print("Upload CURSO")
    s3_client.upload_file(f"./tmp/{pasta[0]}/dados/SUP_CURSO_2019.CSV", 
        "igti-edc-desafiofinal",
        "raw/censoedsup2019/curso/SUP_CURSO_2019.CSV",
        Config=s3_upload_cfg
    )

    print("Upload IES")
    s3_client.upload_file(f"./tmp/{pasta[0]}/dados/SUP_IES_2019.CSV", 
        "igti-edc-desafiofinal",
        "raw/censoedsup2019/IES/SUP_IES_2019.CSV",
        Config=s3_upload_cfg
    )