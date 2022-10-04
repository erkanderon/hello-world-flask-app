FROM python:3.9-buster
USER root
RUN mkdir -p /application/src
WORKDIR /application/src
RUN chmod a+rwx /application/src
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]