# horta-demo-vuln — repo demo para o lab de DevSecOps (Aula 14 ES)

API FastAPI minimalista da horta com vulnerabilidades **plantadas** para o
laboratório da Aula 14. Não use isto em produção. Sério.

## Vulnerabilidades plantadas (gabarito do professor)

1. **SQL injection em `GET /leituras`** — `config.py`/`main.py`: filtro `sensor`
   é interpolado direto na query (string concat, sem parametrização).
2. **Dependência com CVE conhecido** — `requirements.txt`: `requests==2.19.1`
   (CVE-2018-18074, CVSS 9.8). Trivy pega.
3. **Secret hardcoded** — `config.py`: `AWS_SECRET_ACCESS_KEY` em texto
   plano. Semgrep + Trivy `--scanners secret` + GitLeaks pegam.
4. **Dockerfile com base EOL** — `Dockerfile`: `python:3.7`. Trivy
   `image` acumula CVEs da imagem base.

## Como rodar o lab (4 comandos)

```bash
# Pré-requisito: ter Semgrep, Trivy e Syft instalados.

# SAST
semgrep --config=auto .

# SCA + secrets
trivy fs --scanners vuln,secret .

# SBOM em CycloneDX JSON
syft . -o cyclonedx-json > sbom.cdx.json

# (Opcional) scan de imagem se buildar o Dockerfile
docker build -t horta-demo:latest .
trivy image horta-demo:latest
```

## Endpoints

- `POST /leituras` — registra leitura.
- `GET /leituras?sensor=dht22` — lista (vulnerável a SQLi pelo filtro).
- `POST /irrigacao` — aciona zona.

## Estrutura

- `main.py` — FastAPI app.
- `config.py` — credenciais (problema plantado).
- `requirements.txt` — dependências (CVE plantada).
- `Dockerfile` — imagem (base EOL plantada).
