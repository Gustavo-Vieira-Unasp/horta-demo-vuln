# Vulnerabilidade (des)plantada: imagem base EOL (Python 3.7 sai de suporte
# em 2023, acumula CVEs nao corrigidas). Trivy `image` lista as CVEs da base.
FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
