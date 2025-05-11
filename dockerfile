FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 libglib2.0-0 libnss3 libgconf-2-4 \
    libfontconfig1 libxss1 libappindicator3-1 libasound2 libatk1.0-0 libgtk-3-0 \
    chromium-driver chromium

ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV PATH=$CHROMEDRIVER_PATH:$PATH

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi selenium uvicorn

CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8000"]
