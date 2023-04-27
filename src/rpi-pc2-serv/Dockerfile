FROM navikey/raspbian-bullseye:latest

RUN apt-get update -y && apt-get upgrade -y --with-new-pkgs 

RUN apt-get install git cmake gcc libraspberrypi-bin libraspberrypi-dev liblog4cpp5-dev libv4l-dev  -y

RUN mkdir /prod

RUN apt-get install g++ -y

RUN cd /prod && git clone https://github.com/mpromonet/v4l2rtspserver && cd /prod/v4l2rtspserver && cmake . && make && sudo make install 

COPY server_entrypoint.sh /prod/server_entrypoint.sh

ENTRYPOINT ["/prod/server_entrypoint.sh"]

WORKDIR prod
EXPOSE 8000
