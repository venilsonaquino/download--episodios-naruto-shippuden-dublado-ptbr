import requests
import json
import os

def download_file(url: str, file_name: str, chunk_size: int = 1024*1024):
    """
    Faz o download de um arquivo grande por stream.
    :param url: URL do arquivo para download
    :param file_name: Nome do arquivo de saída
    :param chunk_size: Tamanho de cada bloco em bytes (padrão: 1MB)
    """
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total = int(response.headers.get("content-length", 0))
        downloaded = 0

        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:  # ignora keep-alive
                    file.write(chunk)
                    downloaded += len(chunk)
                    # Exibe progresso simples
                    print(f"\rBaixado {downloaded/1024/1024:.2f} MB de {total/1024/1024:.2f} MB", end="")

    print(f"\n✅ Download concluído: {file_name}")

def main():
    # Carrega o JSON
    with open("episodes.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    base_url = "https://cdn-s01.mywallpaper-4k-image.net/stream/n/naruto-shippuden-dublado/"

    show_folder = f"{data['Show']} ({data['Year']})"

    for season in data["Seasons"]:
        season_folder = f"{season['Season']}"
        folder_path = os.path.join(show_folder, season_folder)
        os.makedirs(folder_path, exist_ok=True)
        for ep in season["Episodes"]:
            ep_num = ep["Episode"]
            # caso queira fazer o downalod a partir de algum ep
            # if ep_num < 484:
            #     continue
            title = ep["Title"].replace("/", "-").replace("\\", "-")
            url = f"{base_url}{ep_num}.mp4/index.m3u8"
            file_name = os.path.join(folder_path, f"{title}.mp4")
            print(f"\nIniciando download: {title}")
            download_file(url, file_name)

if __name__ == "__main__":
    main()