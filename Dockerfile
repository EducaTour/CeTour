FROM python:3.11.4-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install cron -y && apt-get clean

# setup python
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

COPY . /app/

WORKDIR /app

# Expose
EXPOSE 8000
RUN chmod +x ./entrypoint.sh
CMD ["./entrypoint.sh"]
