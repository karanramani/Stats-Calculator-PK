FROM python:3

ADD src /src

CMD [ "python", "./src/src_stats-calculator.py"]