import os
from dotenv import load_dotenv

# Carrega as variáveis do .env pra cá
load_dotenv()

"""Configuração da API demo. Agora protegidas."""

# 1º Argumento: Busca os valores das variaveis de ambiente. 
# 2º Argumento: Fallback
# Coloque o nome exado de como deixou no .env entre aspas
AWS_ACESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "default_key")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "default_secret")

# Conexao com BD local (sqlite para o lab).
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./default.db")

# Token "interno" (agora não mais) hardcoded (segundo secret plantado).
INTERNAL_API_TOKEN = os.getenv("INTERNAL_API_TOKEN")