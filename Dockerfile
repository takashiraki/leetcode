FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt update \
    && apt install -y git lazygit tmux vim \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .