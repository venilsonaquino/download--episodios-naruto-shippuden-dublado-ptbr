# Download Episodes Naruto Shippuden

Este projeto tem como objetivo automatizar o download dos episódios do anime Naruto Shippuden.

## Funcionalidades
- Leitura de uma lista de episódios a partir de um arquivo JSON (`episodes.json`)
- Download automático dos episódios listados

## Como usar
1. Clone o repositório:
   ```zsh
   git clone https://github.com/venilsonaquino/download-episodes-naruto-shippuden.git
   ```
2. Crie e ative um ambiente virtual (recomendado):
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências do projeto:
   ```zsh
   pip install -r requirements.txt
   ```
4. Execute o script principal:
   ```zsh
   python3 index.py
   ```

## Estrutura do Projeto
- `index.py`: Script principal para download dos episódios
- `episodes.json`: Lista dos episódios a serem baixados

## Requisitos
- Python 3.x
- ffmpeg (para download dos vídeos HLS)

### Instalação do ffmpeg
```zsh
sudo apt update && sudo apt install -y ffmpeg
```
## Licença
Este projeto é apenas para fins educacionais.
