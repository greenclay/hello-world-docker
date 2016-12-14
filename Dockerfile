FROM python:3-onbuild

CMD [ "python", "./tornado_server.py" ]

EXPOSE 80
