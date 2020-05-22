FROM python:3

ADD *.py /
ADD config.json /

RUN pip install requests
RUN pip install discord


CMD [ "python", "./el_bot.py" ]