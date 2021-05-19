FROM ubuntu:20.04
COPY requirements.txt /tmp
WORKDIR /tmp



# Install essential packages 
RUN apt-get update && apt-get install python3-pip libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
RUN pwd
RUN pip3 install -r requirements.txt
