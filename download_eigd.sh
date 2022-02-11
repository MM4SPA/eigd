#!/bin/sh
BASEURL="https://data.uni-hannover.de/dataset"
# EIGD-Handball
mkdir -p data/eigd/handball && cd data/eigd/handball
mkdir video positions

# wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/7ce00147-f97a-44e0-9058-d1bb3bbe2229/download/eigd-h_vid_part_0.zip"
# wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/8d1b00e0-56f5-4524-a9f3-6cc22a6301c3/download/eigd-h_vid_part_1.zip"
# wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/1b49f55b-f0ae-497a-80e2-9edc042a8909/download/eigd-h_vid_part_2.zip"
# wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/9d5a7e7b-0a8f-4005-abeb-651c4e0252b1/download/eigd-h_vid_part_3.zip"
# wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/c0587090-5d4b-4fb9-93cc-adb2fdf7cd1f/download/eigd-h_vid_part_4.zip"
# for i in range {0..4}
# do
#   unzip eigd-h_vid_part_$i.zip -d ./video/
# done

wget "${BASEURL}/e5d15129-9dd4-460b-a7a9-4d75e041c8ad/download/eigd-h_annotations.jsonl" -O event_annotations.jsonl
# wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/fd24e032-742d-4609-9052-cec310a2a563/download/eigd-h_pos.zip" && unzip eigd-h_pos.zip -d ./positions
cd ../../..

# EIGD-Soccer
mkdir -p data/eigd/soccer/video && cd data/eigd/soccer/
wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/d755230e-2768-4a59-a345-fc4dbbfd7476/download/eigd-s_annotations.jsonl" -O event_annotations.jsonl
wget "${BASEURL}/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/f55c250c-e9e8-4999-8b16-8974c55fbf9d/download/eigd-s_video_urls.tsv" -O eigd-s_video_urls.tsv