#!/bin/bash

if [ $# -ne 3 ]
then
	echo "Usage: $0 <repo path> <start version> <end version>"
	exit 1
fi

REPO_PATH=$1
START_VER=$2
END_VER=$3

git -C $REPO_PATH log --pretty=format:user:%aN%n%ct --reverse --raw \
	--encoding=UTF-8 --no-renames $START_VER..$END_VER
