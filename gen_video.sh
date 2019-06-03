#!/bin/bash

if [ $# -ne 1 ]
then
	echo "Usage: $0 <log path>"
	exit 1
fi

LOGFILE=$1

gource $LOGFILE -1280x720 -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm \
	-i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 \
	-threads 0 -bf 0 $LOGFILE.mp4

