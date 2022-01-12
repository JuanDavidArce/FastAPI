FROM ubuntu

RUN mkdir app
RUN apt update
RUN apt upgrade
RUN apt install python3 -y
RUN apt install python3-pip -y
COPY requirements.txt ./app/requirements.txt
RUN pip3 install -r ./app/requirements.txt 
WORKDIR /app
EXPOSE 8000
CMD [ "uvicorn","main:app","--reload","--host","0.0.0.0"]   