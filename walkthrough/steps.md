# Passos tomados para resolver debilidades

Meu walkthrough para a atividade `horta-demo-vuln` de Engenharia de Software.

## Instalação

1. Docker:
    * [Link para download oficial](https://www.docker.com/products/docker-desktop/)
    * Reinicie agora ou deixe para depois das outras instalações.
2. Semgrep:
    * [Site para sincronização](https://semgrep.dev/)
    * [Link da extensão](https://marketplace.visualstudio.com/items?itemName=Semgrep.semgrep)
    * Ambas são necessárias.
3. Trivy:
    * [Link para download oficial](https://github.com/aquasecurity/trivy/releases)
4. Syft:
    * [Link para download oficial](https://github.com/anchore/syft/releases)

## venv

É recomendável criar um ambiente virtual (`venv`) para isolar as dependências do projeto e evitar conflitos com outros pacotes instalados no sistema. Pense nele como uma "bolha" separada exclusivamente para este projeto.

PowerShell:

```ps
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Também é necessário instalar o Semgrep via pip (Python):

*Obs.: Você pode instalar diretamente os arquivos usados pelo Professor De Lucca com `pip install -r requirements.txt`*

```ps
python -m pip install semgrep
python -m pip install -r requirements.txt
```

## Semgrep

### Comando - Semgrep

PowerShell e bash:

```ps
semgrep --config=auto .
```

### Logs - Semgrep

[Clique aqui para ver](./logs/semgrep.log.md)

### Pontos para observarmos - Semgrep

1. **SQL Injection**
    * Onde: [main.py](../main.py)
    * Problema: O Semgrep detectou o uso de `sqlalchemy.text` com f-strings (interpolação direta). Isso é perigoso porque o dado que vem do usuário entra direto na query sem nenhum tratamento.
    * Risco: Um atacante pode enviar algo como `sensor=dht22'; DROP TABLE leituras; --` e apagar o seu banco de dados inteiro.

2. **Segurança do Container**
    * Onde: [Dockerfile](../Dockerfile)
    * Problema: Não foi especificado um `USER` no Dockerfile. Por padrão, o container roda como root, o que é uma vulnerabilidade.
    * Risco: Se alguém conseguir invadir sua aplicação FastAPI, terá privilégios de administrador (root) dentro do container, o que facilita ataques de "escape" para o servidor real.

## Trivy

### Comando - Trivy

```ps
trivy fs --scanners vuln,secret .
```

### Logs - Trivy

[Clique aqui para ver](./logs/trivy.log.md)

### Pontos para observarmos - Trivy

1. **CVE-2018-18074**
    * Mencionada anteriormente no [README](../README.md)
    * Severidade: **High** — Permite o vazamento de credenciais ao redirecionar de HTTPS para HTTP.

2. Note que há vulnerabilidades de 2023, 2024 e até 2026 (`CVE-2026-25645`). Brechas sempre são descobertas — isso é normal.

3. Remediação: A coluna **Fixed Version** sugere atualizar para `2.33.0`.

4. **GitHub Personal Access Token**
    * Onde: [config.py](../config.py)
    * Problema: Tokens de acesso **NÃO DEVEM NUNCA ESTAR HARDCODED**.

## Syft

### Comando - Syft

```ps
syft . -o cyclonedx-json > sbom.cdx.json
```

### Log - Syft

[Clique aqui](./logs/syft.log.md)  
[PARTE do JSON gerado](./logs/sbom.cdx.md)

*Obs.: O arquivo `sbom.cdx.json`, por mais que não seja sigiloso, possui, na formatação normal, mais de 10k linhas — então não sobe no GitHub.*

### Pontos para observarmos - Syft

1. **4 = 125**
    * Enquanto o [requirements.txt](../requirements.txt) possui apenas 4 linhas, o Syft encontrou 125 pacotes. Isso porque além dessas 4 bibliotecas diretas, elas dependem de outras, que dependem de outras, que dependem de outras, e assim vai. Matar mosca com bazuca, mas é assim que funciona.

2. **.venv**
    * O Syft entrou na pasta `.venv`, o que explica os 117 executáveis encontrados.

## Scan de Imagem Docker

### Comandos - Docker

```ps
docker build -t horta-demo:latest .
```

*Obs.: Para funcionar, é necessário ter `requests==2.25.1` no [requirements.txt](../requirements.txt).*

```ps
.\trivy.exe image horta-demo:latest
```

*Obs.: Talvez seja necessário usar o caminho completo do `trivy.exe`, especialmente se o PATH não estiver configurado.*

*Obs. 2: MUITO PROVAVELMENTE você vai precisar usar um sufixo no comando, como `> scan_results.txt` ou `| less -S`, por conta da quantidade de texto gerado. Você também pode exportar como JSON ou tabela.*

### Log - Docker

[Clique aqui](scan_results.txt)
