FROM python:3.9.5
ENV PYTHONUNBUFFERED 1 # 파이썬 출력 버퍼링이 기본으로 작동하기 때문에 파이썬 로그가 늦게 출력됨에 따라 버퍼링 없앰


RUN apt-get update -y
RUN apt-get install -y vim # vi 설치
RUN apt-get install -y net-tools # 네트워크 툴
RUN apt-get install -y dnsutils
RUN apt install -y cloud-init

RUN apt-get install -y python3-dev
RUN apt-get install -y default-libmysqlclient-dev
#
RUN mkdir /srv/docker-server


ADD . /srv/docker-server
#
WORKDIR /srv/docker-server

RUN pip install --upgrade pip # pip 업그레이드
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT ["sh","/entrypoint.sh"]

