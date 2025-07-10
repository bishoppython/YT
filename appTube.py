import os
import subprocess
from urllib.parse import urlparse, parse_qs

def download_youtube_video(url, output_path='./downloads'):
    """
    Baixa vídeos do YouTube em 1080p usando youtube-dl e ffmpeg
    """
    try:
        # Verificar se a URL é válida
        if not is_valid_youtube_url(url):
            print("URL do YouTube inválida.")
            return False

        # Criar diretório se não existir
        os.makedirs(output_path, exist_ok=True)

        # Comando para baixar em 1080p (melhor qualidade de áudio e vídeo)
        command = [
            'yt-dlp',
            '-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '--merge-output-format', 'mp4',
            '-o', f'{output_path}/%(title)s.%(ext)s',
            '--no-warnings',
            url
        ]

        # Executar o comando
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("\n✅ Download concluído com sucesso!")
            return True
        else:
            print("\n❌ Erro durante o download:")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {str(e)}")
        return False

def is_valid_youtube_url(url):
    """
    Verifica se a URL é do YouTube
    """
    parsed = urlparse(url)
    if 'youtube.com' not in parsed.netloc and 'youtu.be' not in parsed.netloc:
        return False
    
    if 'youtube.com' in parsed.netloc:
        query = parse_qs(parsed.query)
        return 'v' in query or 'watch' in parsed.path
    
    return True

if __name__ == "__main__":
    print("YouTube Downloader (1080p) - Sem Pytube")
    print("---------------------------------------")
    url = input("Cole a URL do vídeo: ").strip()
    
    if download_youtube_video(url):
        print("O vídeo foi salvo na pasta 'downloads'")
    else:
        print("Falha ao baixar o vídeo. Verifique a URL e sua conexão.")