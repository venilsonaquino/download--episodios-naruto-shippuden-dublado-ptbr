# Download Episódios Naruto Shippuden Dublado PT-BR

Este projeto tem como objetivo automatizar o download dos episódios do anime Naruto Shippuden totalmente dublado em português brasileiro, completo do episódio 001 ao 500. 

⚠️ **Nota importante**: O arquivo `episodes.json` não está completo com todos os episódios. Basta você adicionar os episódios que faltam e seja feliz!

## Funcionalidades
- ✅ Download automático dos episódios dublados em PT-BR
- ✅ Leitura de uma lista de episódios a partir do arquivo JSON (`episodes.json`)
- ✅ Conversão automática de streams HLS (.m3u8) para arquivos MP4
- ✅ Compatível com media servers como Jellyfin, Plex, etc.
- ✅ Organização automática por temporadas

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
- `episodes.json`: Lista dos episódios a serem baixados (pode ser expandida)
- `requirements.txt`: Dependências Python do projeto

## Como adicionar mais episódios
Para adicionar episódios que não estão no `episodes.json`, basta seguir o padrão:
```json
{
  "Episode": 501,
  "Title": "Naruto Shippuden - S21E501 - Título do Episódio"
}
```

## Requisitos
- Python 3.x
- ffmpeg (para download dos vídeos HLS)

### Instalação do ffmpeg
```zsh
sudo apt update && sudo apt install -y ffmpeg
```
## Licença
Este projeto é apenas para fins educacionais.
