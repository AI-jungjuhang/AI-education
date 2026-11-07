#!/usr/bin/env bash
# 사용법: bash build.sh   (필요: node+playwright, ffmpeg, python3+numpy+scipy)
set -euo pipefail
cd "$(dirname "$0")"
W=${TMPDIR:-/tmp}/shorts-001; rm -rf "$W"; mkdir -p "$W/frames" out
node render.js "$W/frames" "$W/timeline.json" 30 4
cp "$W/timeline.json" out/timeline.json
python3 make_music.py "$W/timeline.json" "$W/audio.wav"
# 소리 크기를 쇼츠·릴스에서 흔한 수준(약 -14 LUFS)으로 맞춘다
ffmpeg -y -loglevel error -i "$W/audio.wav" -af loudnorm=I=-14:TP=-1.5:LRA=9 -ar 48000 "$W/audio_n.wav"
ffmpeg -y -loglevel error -framerate 30 -i "$W/frames/f%05d.jpg" -i "$W/audio_n.wav" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -shortest \
  -movflags +faststart out/001-next-word.mp4
ffmpeg -y -loglevel error -i out/001-next-word.mp4 -ss 3.2 -frames:v 1 out/001-next-word-thumbnail.jpg
ffprobe -v error -show_entries format=duration,size -of default=nw=1 out/001-next-word.mp4
