# Logs

```logs
2026-05-08T00:33:48-03:00       INFO    [vulndb] Need to update DB
2026-05-08T00:33:48-03:00       INFO    [vulndb] Downloading vulnerability DB...
2026-05-08T00:33:48-03:00       INFO    [vulndb] Downloading artifact...        repo="mirror.gcr.io/aquasec/trivy-db:2"
92.08 MiB / 92.08 MiB [----------------------------------------------------------------------------------------------------------------------------------] 100.00% 7.12 MiB p/s 13s
2026-05-08T00:34:05-03:00       INFO    [vulndb] Artifact successfully downloaded       repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-05-08T00:34:05-03:00       INFO    [vuln] Vulnerability scanning is enabled
2026-05-08T00:34:05-03:00       INFO    [secret] Secret scanning is enabled
2026-05-08T00:34:05-03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-05-08T00:34:05-03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.70/guide/scanner/secret#recommendation for faster secret detection
2026-05-08T00:34:28-03:00       WARN    [pip] Unable to find python `site-packages` directory. License detection is skipped.    err="site-packages directory not found"
2026-05-08T00:34:28-03:00       INFO    Number of language-specific files       num=1
2026-05-08T00:34:28-03:00       INFO    [pip] Detecting vulnerabilities...

Report Summary

┌──────────────────┬──────┬─────────────────┬─────────┐
│      Target      │ Type │ Vulnerabilities │ Secrets │
├──────────────────┼──────┼─────────────────┼─────────┤
│ requirements.txt │ pip  │        5        │    -    │
├──────────────────┼──────┼─────────────────┼─────────┤
│ config.py        │ text │        -        │    1    │
└──────────────────┴──────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


requirements.txt (pip)
======================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 4, HIGH: 1, CRITICAL: 0)

┌──────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│ Library  │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ requests │ CVE-2018-18074 │ HIGH     │ fixed  │ 2.19.1            │ 2.20.0        │ python-requests: Redirect from HTTPS to HTTP does not remove │
│          │                │          │        │                   │               │ Authorization header                                         │
│          │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2018-18074                   │
│          ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│          │ CVE-2023-32681 │ MEDIUM   │        │                   │ 2.31.0        │ python-requests: Unintended leak of Proxy-Authorization      │
│          │                │          │        │                   │               │ header                                                       │
│          │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2023-32681                   │
│          ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│          │ CVE-2024-35195 │          │        │                   │ 2.32.0        │ requests: subsequent requests to the same host ignore cert   │
│          │                │          │        │                   │               │ verification                                                 │
│          │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-35195                   │
│          ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│          │ CVE-2024-47081 │          │        │                   │ 2.32.4        │ requests: Requests vulnerable to .netrc credentials leak via │
│          │                │          │        │                   │               │ malicious URLs                                               │
│          │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-47081                   │
│          ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│          │ CVE-2026-25645 │          │        │                   │ 2.33.0        │ requests: Requests: Security bypass due to predictable       │
│          │                │          │        │                   │               │ temporary file creation                                      │
│          │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-25645                   │
└──────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

config.py (secrets)
===================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 1)

CRITICAL: GitHub (github-pat)
════════════════════════════════════════
GitHub Personal Access Token
────────────────────────────────────────
 config.py:13 (offset: 548 bytes)
────────────────────────────────────────
  11   
  12   # Token "interno" hardcoded (segundo secret plantado).
  13 [ INTERNAL_API_TOKEN = "****************************************"
  14   
────────────────────────────────────────
```
