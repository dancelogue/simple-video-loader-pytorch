#!/bin/bash
sudo nvidia-docker build -t dancelogue:simple-video-loader-pytorch .
sudo nvidia-docker run --rm -ti --volume=$(pwd):/simple-video-loader-pytorch:rw --workdir=/simple-video-loader-pytorch --ipc=host dancelogue:simple-video-loader-pytorch /bin/bash