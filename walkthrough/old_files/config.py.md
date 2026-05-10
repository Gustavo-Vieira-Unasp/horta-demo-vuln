# config.py

Sendo apenas um arquivo mock, farei com que seja possível ver o arquivo antigo de forma fácil

```python
"""Configuração da API demo. NAO USE EM PRODUCAO."""

# Vulnerabilidade plantada: secret hardcoded.
# Detectado por Semgrep (regra hardcoded-aws-key), Trivy (--scanners secret)
# e GitLeaks. Em codigo real, sempre via variavel de ambiente ou secret manager.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Conexao com BD local (sqlite para o lab).
DATABASE_URL = "sqlite:///./horta_demo.db"

# Token "interno" hardcoded (segundo secret plantado).
INTERNAL_API_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"

```
