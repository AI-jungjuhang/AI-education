#!/usr/bin/env bash
# 사용법: bash build.sh   (필요: node+playwright, ffmpeg, python3+numpy)
set -euo pipefail
cd "$(dirname "$0")"
W=${TMPDIR:-/tmp}/shorts-001; rm -rf "$W"; mkdir -p "$W/frames" out
node render.js "$W/frames" 30 4
python3 make_music.py "$W/music.wav" 58
# 음악 크기를 유튜브 권장 수준(약 -16 LUFS)으로 맞춘다
ffmpeg -y -loglevel error -i "$W/music.wav" -af loudnorm=I=-16:TP=-1.5:LRA=7 -ar 48000 "$W/music_n.wav"
ffmpeg -y -loglevel error -framerate 30 -i "$W/frames/f%05d.jpg" -i "$W/music_n.wav" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -shortest \
  -movflags +faststart out/001-next-word.mp4
ffmpeg -y -loglevel error -i out/001-next-word.mp4 -ss 2.2 -frames:v 1 out/001-next-word-thumbnail.jpg
ffprobe -v error -show_entries format=duration,size -of default=nw=1 out/001-next-word.mp4
