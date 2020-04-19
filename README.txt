Calculator
==========

Getting Started
---------------

- Change directory into your newly created project.

    cd Calculator

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

Docker Instructions:

    mkdir docker_images
    cd docker_images

    mkdir calculator_app
    cd calculator_app

    git clone https://github.com/pavanniyogi/Calculator.git src

    vi Dockerfile
        FROM ubuntu:latest
        RUN apt-get update -y && apt-get install -y python3 python3-pip && pip3 install --upgrade pip setuptools && apt-get install curl
        RUN mkdir -p /var/calculator
        ADD src/ /var/calculator
        ADD requirements.txt /var/calculator
        WORKDIR /var/calculator
        RUN pip3 install -e .
        RUN python setup.py develop
        EXPOSE 6543
        CMD pserve development.ini

    docker image build -t pavanniyogi/calc-app:v3 .
    docker image ls

    docker container run -d --name calc-app-final -p 6543:6543 pavanniyogi/calc-app:v3
    docker container ls

    docker container exec -it calc-app-final curl localhost:6543/sum/1/2 
