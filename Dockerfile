FROM 3.8-alpine

WORKDIR /root/
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8098
ENTRYPOINT [ "/bin/bash",  "entrypoint.sh" ]