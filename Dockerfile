FROM python:3


WORKDIR /usr/src/app
COPY . .


# Install essential packages 
RUN apt-get update && apt-get install cmake python3-pip libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD python app.py