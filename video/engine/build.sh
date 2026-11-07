#!/usr/bin/env bash
# 사용법: bash video/engine/build.sh <에피소드 폴더> [썸네일 시각(초)=3.2]
#   환경 변수: MUSIC=soft(기본, 조용한 음악) | loud(드럼 있는 신나는 음악), LUFS=소리 크기
#   필요: node+playwright, ffmpeg, python3+numpy+scipy
set -euo pipefail
EP="$(cd "$1" && pwd)"; THUMB=${2:-3.2}; HERE="$(cd "$(dirname "$0")" && pwd)"
ID=$(python3 -c "import json,sys;print(json.load(open('$EP/episode.json'))['id'])")
MUSIC=${MUSIC:-soft}; [ "$MUSIC" = soft ] && LUFS=${LUFS:--20} || LUFS=${LUFS:--14}
W=${TMPDIR:-/tmp}/shorts-$ID; rm -rf "$W"; mkdir -p "$W/frames" "$EP/out"
python3 "$HERE/make_scene.py" "$EP"
node "$HERE/render.js" "$EP/scene.html" "$W/frames" "$W/timeline.json" 30 4
cp "$W/timeline.json" "$EP/out/timeline.json"
python3 "$HERE/make_music.py" "$W/timeline.json" "$W/audio.wav" $([ "$MUSIC" = soft ] && echo soft)
ffmpeg -y -loglevel error -i "$W/audio.wav" -af loudnorm=I=$LUFS:TP=-2:LRA=9 -ar 48000 "$W/audio_n.wav"
ffmpeg -y -loglevel error -framerate 30 -i "$W/frames/f%05d.jpg" -i "$W/audio_n.wav" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -shortest \
  -movflags +faststart "$EP/out/$ID.mp4"
ffmpeg -y -loglevel error -i "$EP/out/$ID.mp4" -ss "$THUMB" -frames:v 1 "$EP/out/$ID-thumbnail.jpg"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$EP/out/$ID.mp4"
