# Logs

```logs

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘

METRICS: Using configs from the Registry (like --config=p/ci) reports pseudonymous rule metrics to semgrep.dev.
To disable Registry rule metrics, use "--metrics=off".
When using configs only from local files (like --config=xyz.yml) metrics are sent only when the user is logged in.

More information: https://semgrep.dev/docs/metrics

Scanning 7 files (only git-tracked) with:
                                      
✔ Semgrep OSS
  ✔ Basic security coverage for first-party code vulnerabilities.
                                              
✔ Semgrep Code (SAST)
  ✔ Find and fix vulnerabilities in the code you write with advanced scanning and expert security rules.
                                                     
✘ Semgrep Supply Chain (SCA)
  ✘ Find and fix the reachable vulnerabilities in your OSS dependencies.
 
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00                                                                                                                        
                   
                   
┌─────────────────┐
│ 3 Code Findings │
└─────────────────┘
                             
    Dockerfile
   ❯❯❱ dockerfile.security.missing-user.missing-user
          ❰❰ Blocking ❱❱
          By not specifying a USER, a program in the container may run as 'root'. This is a security hazard.
          If an attacker can control a process running as root, they may have control over the container.   
          Ensure that the last USER in a Dockerfile is a USER other than 'root'.                            
          Details: https://sg.run/Gbvn                                                                      
                                                                                                            
           ▶▶┆ Autofix ▶ USER non-root CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
           13┆ CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
                          
    main.py
   ❯❯❱ python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
          ❰❰ Blocking ❱❱
          sqlalchemy.text passes the constructed SQL statement to the database mostly unchanged. This means  
          that the usual SQL injection protections are not applied and this function is vulnerable to SQL    
          injection if user input can reach here. Use normal SQLAlchemy operators (such as `or_()`, `and_()`,
          etc.) to construct SQL.                                                                            
          Details: https://sg.run/yP1O                                                                       
                                                                                                             
           51┆ rows = conn.execute(text(query)).fetchall()
            ⋮┆----------------------------------------
           66┆ conn.execute(text(
           67┆     "INSERT INTO leituras (device_id, sensor, valor, ts) "
           68┆     f"VALUES ('{device_id}', '{sensor}', {valor}, '{ts}')"
           69┆ ))

                
                
┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 3 (3 blocking)
 • Rules run: 1204
 • Targets scanned: 7
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 1204 rules on 7 files: 3 findings.
```
