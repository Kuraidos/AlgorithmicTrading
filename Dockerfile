FROM python:3.10
WORKDIR /usr/src/app
COPY Pipfile .
COPY src .
RUN pip install pipenv && pipenv install
CMD [ "pipenv", "run", "python", "-m", "flask", "--app", "algorithmic_trading/main", "run" ]