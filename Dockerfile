FROM nvidia/cuda:9.0-base

RUN apt-get update && apt-get install -y ffmpeg python3-pip unrar

# Python dependencies
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install --upgrade pip

# Torch and dependencies:
ADD requirements.txt /
RUN pip install -r /requirements.txt

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES=video,compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=9.0"
