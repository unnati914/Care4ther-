#!/usr/bin/env bash

ffmpeg -i 1407_annotated/%d.jpg -vcodec mpeg4 1407.mp4
ffmpeg -i 1407.mp4 -pix_fmt rgb24 1407.gif