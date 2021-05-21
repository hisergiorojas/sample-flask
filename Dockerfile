FROM python:3
WORKDIR /usr/src/app
COPY . .


# Configuration
ARG USD_RELEASE="19.11"
ARG USD_INSTALL="./local/USD"
ENV PYTHONPATH="${PYTHONPATH}:${USD_INSTALL}/lib/python"
ENV PATH="${PATH}:${USD_INSTALL}/bin"
ENV USD_VERSION="20.05"


# Dependencies
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    git build-essential cmake nasm python3-pip python-dev python3-dev \
    libglew-dev libxrandr-dev libxcursor-dev libxinerama-dev libxi-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

# Build + install USD
RUN git clone --branch v${USD_VERSION} --single-branch --depth 1 https://github.com/PixarAnimationStudios/USD.git
RUN cd USD && git checkout tags/v${USD_VERSION} && cd ../
RUN python2 USD/build_scripts/build_usd.py -v --no-usdview "${USD_INSTALL}" 

# Share the volume that we have built to
VOLUME ["./local/USD"]
# Install essential packages
#RUN apt-get update && apt-get install  libglu1-mesa-dev freeglut3-dev mesa-common-dev -y

#RUN git clone https://github.com/hisergiorojas/gltf2usd.git

RUN export PYTHONPATH=$PYTHONPATH:/usr/src/app/local/USD/lib/python
RUN export PATH=$PATH:/usr/src/app/local/USD/bin


# Configuration
ARG UFG_RELEASE="3bf441e0eb5b6cfbe487bbf1e2b42b7447c43d02"
ARG UFG_SRC="usd_from_gltf"
ARG UFG_INSTALL="./local/UFG_BUILD"
ENV USD_DIR="/usr/src/app/local/USD"
ENV LD_LIBRARY_PATH="${USD_DIR}/lib:${UFG_SRC}/lib"
ENV PATH="${PATH}:${UFG_INSTALL}/bin"
ENV PYTHONPATH="${PYTHONPATH}:${UFG_INSTALL}/python"

RUN git clone https://github.com/google/usd_from_gltf.git 

RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/src/app/local/USD:/usr/src/app/usd_from_gltf
RUN export PATH=$PATH:/usr/src/app/local/USD:/usr/src/app/usd_from_gltf

RUN python2 "${UFG_SRC}/tools/ufginstall/ufginstall.py" -v "${UFG_INSTALL}" "${USD_DIR}" --testdata
   

# Start the service
ENTRYPOINT ["usd_from_gltf"]
CMD ["usd_from_gltf"]


EXPOSE 5001

CMD python app.py