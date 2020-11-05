FROM python:3

ADD src /src

CMD[ "python", "./src/stats-calculator.py" ]