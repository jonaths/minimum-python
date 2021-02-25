FROM python:3.8.0-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get clean

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY app/ app/
COPY .env .

WORKDIR app/