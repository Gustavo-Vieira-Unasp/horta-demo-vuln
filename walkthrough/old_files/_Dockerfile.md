# config.py

Sendo apenas um arquivo mock, farei com que seja possível ver o arquivo antigo de forma fácil

```Dockerfile
# Vulnerabilidade plantada: imagem base EOL (Python 3.7 sai de suporte
# em 2023, acumula CVEs nao corrigidas). Trivy `image` lista as CVEs da base.
FROM python:3.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```
