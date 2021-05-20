FROM python:3


WORKDIR /usr/src/app
COPY . .


# Install essential packages
RUN apt-get update && apt-get install cmake nasm python3-pip libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
RUN pip3 install -r requirements.txt

RUN git clone https://github.com/PixarAnimationStudios/USD.git
RUN git clone https://github.com/kcoley/gltf2usd.git

RUN python USD/build_scripts/build_usd.py ./local/USD

RUN export PYTHONPATH=/usr/src/app/local/USD/lib/python
RUN export PYTHONPATH=/usr/src/app/local/USD/bin
EXPOSE 5001

CMD python app.py