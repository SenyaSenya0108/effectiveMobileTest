FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py ./

EXPOSE 8081

RUN useradd -ms /bin/bash develop

USER develop

CMD ["python3", "app.py"]