FROM python:3


WORKDIR /usr/src/app
COPY . .


# Install essential packages
RUN apt-get update && apt-get install cmake nasm python3-pip libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
RUN pip3 install -r requirements.txt

RUN git clone https://github.com/PixarAnimationStudios/USD.git
RUN git clone https://github.com/hisergiorojas/gltf2usd.git
RUN git clone https://github.com/google/usd_from_gltf.git

RUN python USD/build_scripts/build_usd.py ./local/USD

RUN export PYTHONPATH=$PYTHONPATH:/usr/src/app/local/USD/lib/python
RUN export PATH=$PATH:/usr/src/app/local/USD/bin


RUN python usd_from_gltf/tools/ufginstall/ufginstall.py ./local/UFG_BUILD /user/src/app/local/USD
EXPOSE 5001

CMD python app.py