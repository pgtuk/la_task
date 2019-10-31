FROM python:3.7.3-slim
WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		netbase \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends dpkg-dev gcc build-essential libglib2.0-0 \
    libsm6 libxext6 libxrender-dev

COPY requirements.txt requirements.txt

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/app.py"]