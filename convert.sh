#!/bin/bash

if [ $# -ne 3 ]
then
	echo "Usage: $0 <repo path> <start version> <end version>"
	exit 1
fi

BINDIR=`dirname $0`

REPO_PATH=$1
START_VER=$2
END_VER=$3

git -C $REPO_PATH log $START_VER..$END_VER --date=unix --format="%h %ad %an" \
	--stat --no-merges | $BINDIR/_convert.py
