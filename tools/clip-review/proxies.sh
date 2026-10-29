#!/usr/bin/env bash
# 1080p H.264 editing copies of every clip, plus JPGs of the photos.
# Usage: proxies.sh <source folder> <project folder>
# Originals in the source folder are never touched. Skips any proxy that
# already exists, so a rerun only fills gaps.
set -euo pipefail

SRC="$1"
DIR="$(cd "$2" && pwd)"
mkdir -p "$DIR/proxies" "$DIR/photos"

proxy() {
  local src="$1" out="$2/proxies/$(basename "${1%.*}").mp4"
  [[ -s "$out" ]] && return 0
  # ffmpeg applies the phone's rotation flag on decode; scale the short side to 1080.
  ffmpeg -nostdin -v error -y -i "$src" \
    -vf "scale='if(gt(iw,ih),-2,1080)':'if(gt(iw,ih),1080,-2)'" \
    -c:v h264_videotoolbox -b:v 12M -c:a aac -b:a 192k \
    -movflags +faststart "$out.part.mp4"
  mv "$out.part.mp4" "$out"
}
export -f proxy

find "$SRC" -maxdepth 1 -type f \( -iname '*.mov' -o -iname '*.mp4' \) -print0 |
  xargs -0 -P 4 -I{} bash -c 'proxy "$1" "$2"' _ {} "$DIR"

find "$SRC" -maxdepth 1 -type f \( -iname '*.heic' -o -iname '*.jpg' \) -print0 |
  while IFS= read -r -d '' f; do
    out="$DIR/photos/$(basename "${f%.*}").jpg"
    [[ -s "$out" ]] || sips -s format jpeg -Z 2160 "$f" --out "$out" >/dev/null
  done
# sips keeps the phone's rotation flag instead of rotating pixels; bake it in.
python3 -c "
import sys
from PIL import Image, ImageOps
for p in sys.argv[1:]:
    im = Image.open(p)
    if im.getexif().get(0x0112, 1) != 1:
        ImageOps.exif_transpose(im).save(p, quality=92)
" "$DIR"/photos/*.jpg

echo "$(ls "$DIR/proxies" | grep -c '\.mp4$') proxies, $(ls "$DIR/photos" | wc -l | tr -d ' ') photos"
