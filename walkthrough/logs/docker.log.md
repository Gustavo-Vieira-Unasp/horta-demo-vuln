# Log - Docker

```log
[+] Building 16.2s (11/11) FINISHED                                                                                                                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                           0.0s
 => => transferring dockerfile: 382B                                                                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.7                                                                                                                  1.1s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.7@sha256:eedf63967cdb57d8214db38ce21f105003ed4e4d0358f02bedc057341bcf92a0                                                            0.0s
 => => resolve docker.io/library/python:3.7@sha256:eedf63967cdb57d8214db38ce21f105003ed4e4d0358f02bedc057341bcf92a0                                                            0.0s
 => [internal] load build context                                                                                                                                              0.5s
 => => transferring context: 651.83kB                                                                                                                                          0.4s
 => CACHED [2/5] WORKDIR /app                                                                                                                                                  0.0s
 => [3/5] COPY requirements.txt .                                                                                                                                              0.0s
 => [4/5] RUN pip install -r requirements.txt                                                                                                                                  4.6s
 => [5/5] COPY . .                                                                                                                                                             0.9s
 => exporting to image                                                                                                                                                         9.1s
 => => exporting layers                                                                                                                                                        7.4s
 => => exporting manifest sha256:6bda675c9606129798412b73640784b93ca5ba11a688b3ff2f413e76add6c1b0                                                                              0.0s
 => => exporting config sha256:a5dcea4778ee98d5b7264dbcd9337b1d9ff9a82e6debfdb3ce5c4ce313ff4a4e                                                                                0.0s
 => => exporting attestation manifest sha256:ccf7948984db64d743957a06a11d971c48d04fe3877e1c27119704ad2cda0e95                                                                  0.0s
 => => exporting manifest list sha256:f3aae2011464d5f2b43fb930fca2ea1db5a349972ae71ebca4a6d85e0b951dc2                                                                         0.0s
 => => naming to docker.io/library/horta-demo:latest                                                                                                                           0.0s
 => => unpacking to docker.io/library/horta-demo:latest                                                                                                                        1.7s

View build details: [link]
```
