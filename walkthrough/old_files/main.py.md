# config.py

Sendo apenas um arquivo mock, farei com que seja possível ver o arquivo antigo de forma fácil

```python
"""
horta-demo-vuln — API FastAPI didatica com vulnerabilidades plantadas.

Lab da Aula 14 (Engenharia de Software, GBECOM53A). Os achados de
Semgrep/Trivy/Syft contra este repo alimentam a triagem da rodada 2.
"""

from __future__ import annotations

from datetime import datetime
from sqlalchemy import create_engine, text

from fastapi import FastAPI

from config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    DATABASE_URL,
)


app = FastAPI(title="horta-demo-vuln", version="0.1.0")
engine = create_engine(DATABASE_URL)


@app.on_event("startup")
def _setup() -> None:
    with engine.begin() as conn:
        conn.execute(text(
            "CREATE TABLE IF NOT EXISTS leituras ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "device_id TEXT, sensor TEXT, valor REAL, ts TEXT)"
        ))


@app.get("/leituras")
def listar_leituras(sensor: str | None = None) -> list[dict]:
    """Lista leituras filtradas por sensor.

    VULNERAVEL a SQL injection: o parametro `sensor` e concatenado
    direto na query. Semgrep flagga regra python.lang.security.audit.sql-concat
    (ou equivalente). Triagem esperada: corrigir (parametrizar).
    """
    base = "SELECT id, device_id, sensor, valor, ts FROM leituras"
    if sensor:
        # Vulnerabilidade ()plantada: string concat com input externo.
        query = base + " WHERE sensor = '" + sensor + "'"
    else:
        query = base
    with engine.begin() as conn:
        rows = conn.execute(text(query)).fetchall()
    return [
        {"id": r[0], "device_id": r[1], "sensor": r[2], "valor": r[3], "ts": r[4]}
        for r in rows
    ]


@app.post("/leituras")
def criar_leitura(payload: dict) -> dict:
    """Insere leitura no BD. Tambem com query construida por concat (plantado)."""
    device_id = payload.get("device_id", "")
    sensor = payload.get("sensor", "")
    valor = float(payload.get("valor", 0))
    ts = datetime.utcnow().isoformat()
    with engine.begin() as conn:
        conn.execute(text(
            "INSERT INTO leituras (device_id, sensor, valor, ts) "
            f"VALUES ('{device_id}', '{sensor}', {valor}, '{ts}')"
        ))
    return {"status": "ok", "device_id": device_id, "sensor": sensor}


@app.post("/irrigacao")
def acionar_irrigacao(payload: dict) -> dict:
    """Aciona irrigacao. Sem autenticacao (vulnerabilidade de design plantada)."""
    zona = payload.get("zona", "default")
    return {
        "zona": zona,
        "status": "acionado",
        # Eco do secret (mais um padrao que GitLeaks vai pegar em log).
        "trace_id": f"req-{AWS_ACCESS_KEY_ID[:6]}",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# Uso "fantasma" do secret para garantir que nao seja removido como dead code.
_DEBUG_KEY = AWS_SECRET_ACCESS_KEY[:4]

```
