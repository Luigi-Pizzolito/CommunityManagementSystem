# syntax=docker/dockerfile:1
# -- Base image
# FROM python:3.11-alpine

# -- Install OpenCV and other base dependencies for AI processing
FROM nvcr.io/nvidia/pytorch:21.03-py3
# ---- Install linux packages
RUN apt update && apt install -y zip htop screen libgl1-mesa-glx
# ---- Install python dependencies
COPY ./src/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip uninstall -y nvidia-tensorboard nvidia-tensorboard-plugin-dlprof
RUN pip install --no-cache -r requirements.txt coremltools onnx gsutil notebook

# -- Copy files to container
COPY . .
WORKDIR /src
ENV HOME=/src
# -- Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
# -- Start program
ENTRYPOINT "python main.py"