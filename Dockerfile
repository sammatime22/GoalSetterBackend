FROM python:3.5.2
ADD . /goalsetterbackend
WORKDIR /goalsetterbackend
RUN pip install -r requirements.txt
RUN ls
RUN ls goalsetterbackend
CMD [ "python", "./goalsetterbackend/manage.py", "runserver", "0.0.0.0:8787"]
