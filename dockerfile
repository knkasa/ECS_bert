
FROM python:3.11-slim

WORKDIR /my_dir

COPY . /my_dir

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "deploy.py"]