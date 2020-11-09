FROM python:3

ADD src /src

RUN pip install numpy scipy

CMD [ "python", "./src/src_stats-calculator.py"]