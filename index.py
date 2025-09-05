import requests
import json
import os
import subprocess

def download_video_with_ffmpeg(url: str, file_name: str):
    """
    Faz o download de um vídeo a partir de uma URL m3u8 usando ffmpeg.
    :param url: URL do arquivo m3u8 para download
    :param file_name: Nome do arquivo de saída
    """
    print(f"Iniciando download com ffmpeg: {file_name}")
    
    try:
        # Comando ffmpeg para baixar vídeo HLS
        cmd = [
            'ffmpeg',
            '-i', url,
            '-c', 'copy',
            '-bsf:a', 'aac_adtstoasc',
            '-y',  # sobrescrever arquivo se existir
            file_name
        ]
        
        # Executa o comando e captura saída
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Download concluído: {file_name}")
        else:
            print(f"❌ Erro no download: {file_name}")
            print(f"Erro: {result.stderr}")
            
    except FileNotFoundError:
        print("❌ ffmpeg não encontrado. Instale o ffmpeg para usar este script.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

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
            download_video_with_ffmpeg(url, file_name)

if __name__ == "__main__":
    main()