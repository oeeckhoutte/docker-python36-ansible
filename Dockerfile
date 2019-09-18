FROM python:3.6

RUN apt-get update
RUN apt-get install -y jq moreutils
RUN pip install yq
WORKDIR /tmp
COPY requirements.txt ./
COPY fernet-decrypt.py ./
RUN pip install -r requirements.txt
RUN pyinstaller fernet-decrypt.py
RUN mv dist/fernet-decrypt/* /usr/bin/
RUN rm -rf dist
RUN chmod +x /usr/bin/fernet-decrypt
