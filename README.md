# fastApi-Studies

Projeto de estudos com **FastAPI**, organizado com uma estrutura em Python, testes e uploads.

##  Estrutura do Projeto

- `src/fast_start`: código principal da aplicação FastAPI  
- `tests`: testes automatizados (pytest)  
- `uploads`: diretório para arquivos enviados pela aplicação  
- `pyproject.toml`: gerenciador de dependências com Poetry  
- `poetry.lock`: bloqueio de versões  
- `.gitignore`: arquivos e diretórios ignorados pelo Git

##  Descrição

Este projeto serve como base para aprendizado de FastAPI, com foco em:

- Criação de endpoints usando FastAPI
- Validação com Pydantic
- Execução local com Poetry
- Testes automatizados
- Upload de arquivos

##  Pré-requisitos

- Python ≥ 3.8  
- [Poetry](https://python-poetry.org/) instalado

##  Instalação

```bash
git clone https://github.com/sandrorsjunior/fastApi-Studies.git
cd fastApi-Studies
poetry install
