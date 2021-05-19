FROM ubuntu:20.04


# Install essential packages 
RUN apt-get update && apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
