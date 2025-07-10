# YT
Code para Baixar videos do Yutube e outros sites (BETA)


uma solução usando a biblioteca youtube-dl (mais robusta) em conjunto com ffmpeg para garantir o download em 1080p. Esta abordagem é mais confiável e amplamente utilizada.

## 1. Pré-requisitos
Instalar yt-dlp (sucessor do youtube-dl, mais atualizado):
pip install yt-dlp

## 2. Instalar FFmpeg (necessário para combinar áudio e vídeo):

Windows: Baixe do site oficial e adicione ao PATH

Linux: sudo apt install ffmpeg

Mac: brew install ffmpeg

## Como Usar
1. Execute o script Python
2. Cole a URL do vídeo do YouTube quando solicitado
3. O vídeo será baixado na pasta 'downloads' na melhor qualidade disponível até 1080p

## Vantagens desta Solução
1. Mais confiável que pytube (menos sujeita a quebras quando o YouTube muda sua API)
2. Suporte a mais sites além do YouTube
3. Melhor tratamento de erros
4. Atualizações frequentes da biblioteca yt-dlp

## Opções Avançadas
Se quiser customizar ainda mais, você pode modificar a linha do comando:

* Para baixar apenas áudio: '-f', 'bestaudio'
* Para escolher formato específico: '--format', 'mp4'
* Para limitar a qualidade: '--format', 'best[height<=720]'

Esta solução é amplamente utilizada e considerada uma das mais estáveis para download de vídeos do YouTube atualmente.
