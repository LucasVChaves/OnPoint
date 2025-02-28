# OnPoint

Trabalho da Disciplina de Modelagem de Sistemas (DCC117)

## O que é

É um sistema de ponto eletrônico para controle de horas trabalhadas e frequência de funcionários.

## Executando

Para executar o sistema, basta rodar o arquivo `main.py`:

```bash
git clone https://github.com/LucasVChaves/OnPoint.git
cd OnPoint
python main.py
```

## Stack

- Python 3.8
- Tkinter
- Biblioteca std de JSON do Python
- PyInstaller (para criar executável d o sistema)

## Setup do Ambiente

1. Certifique-se de ter o Python 3.8 instalado:

    ```bash
    # Ubuntu
    sudo apt install python3.8
    ```

    No Windows, baixe o instalador no site oficial.

2. Clone o repositório:

    ```bash
    git clone git@github.com:LucasVChaves/OnPoint.git
    ```

3. Crie um ambiente virtual dentro do diretório do projeto:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Prontinho!

> Toda vez que for trabalhar no projeto, ative o ambiente virtual com `source venv/bin/activate`.
> Se começar a usar uma outra biblioteca atualiza o `requirements.txt`.

## Estrutura de Pastas

```text
OnPoint/
├── main.py              # Ponto de entrada do sistema
├── models/
│   ├── __init__.py
│   ├── employee.py
│   └── clock_in_register.py
├── controllers/
│   ├── __init__.py
│   └── clock_in_controller.py
├── views/
│   ├── __init__.py
│   └── main_interface.py
├── utils/
│   ├── __init__.py
│   └── parsers.py
└── data/                 # Base de dados
    ├── employees.json
    └── clock_log.json
```

> `__init__.py` é um arquivo vazio que indica ao Python que a pasta é um pacote.

**⚠️ POR FAVOR NÃO DEEM PUSH NA MAIN, SÓ DÊ MERGE DA DEV IMPLEMENTADA E TESTADA**
