FROM python:3.8.12-slim-buster

ARG aws_access_key_id
ARG aws_secret_access_key

ENV aws_access_key_id=$aws_access_key_id
ENV aws_secret_access_key=$aws_secret_access_key

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY extract-censo.py ./extract-censo.py

CMD ["python", "extract-censo.py"]