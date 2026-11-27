# app/Dockerfile

FROM python:3.15-slim

WORKDIR .

COPY . .

RUN pip install streamlit \
    && apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2


EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "front.py", "--server.port=8501", "--server.address=0.0.0.0"]