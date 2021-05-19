FROM ubuntu:20.04
WORKDIR /usr/src/app
COPY . .


# Install essential packages 
RUN apt-get update && apt-get install python3 python3-pip libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD [“python3”, “./app.py”]