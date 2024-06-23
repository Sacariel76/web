FROM ubuntu:22.04

SHELL [ "/bin/bash", "-c" ]

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-setuptools \
    python3-venv \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

WORKDIR /apps/api_Demo_01
RUN python3 -m venv apiEnv
RUN source apiEnv/bin/activate

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
EXPOSE 5001
CMD ["uwsgi","-w","src.main:app","--socket","0.0.0.0:5001", "--protocol","http"]