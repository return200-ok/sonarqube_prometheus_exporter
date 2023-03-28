FROM python:3.8-slim

WORKDIR /sonarqube_exporter/
COPY . .
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt


EXPOSE 8198
ENTRYPOINT [ "/bin/sh",  "entrypoint.sh" ]