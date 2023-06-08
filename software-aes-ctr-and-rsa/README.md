- Dependências

  - Este software depende da biblioteca `pycryptodome` que irá utilizar o módulo `Crypto`. Abra o terminal e execute as instruções abaixo.
    - Utilize o comando `pip install pycryptodome`
    - Caso não funcione pode utilizar `py -m pip install pycryptodome`

---

- Como utilizar o projeto

  - Utilize o comando `py exe.py`
  - Lembre de criar um arquivo com o texto plano. Ex: (`x.txt`)

---

- Explicação de arquivos
  - `x.txt` é o texto plano.
  - `y.txt` é o texto cifrado com aes.
  - `iv-enc.txt` é o vetor de inicialização cifrado com a chave pública.
  - `k-enc.txt` é a chave simétrica cifrada com a chave pública.
  - `result.txt` é o resultado da decifragem (deve ser igual ao x.txt).
  - `nomePU.txt` é a chave pública gerada.
  - `nomePR.txt` é a chave privada gerada.
  - `exe.py` executa o software.
  - `aes.py` contém bibliotecas e funções para realizar a cifragem e decifragem.
  - `rsa.py` contém bibliotecas e funções relacionadas a chave pública e privada geradas com rsa.
  - `encrypt.py` executa a função de encriptação chamada em 'exe.py'.
  - `decrypt.py` executa a função de decriptação chamada em 'exe.py'.
