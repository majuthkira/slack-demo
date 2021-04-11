From python:3

WORKDIR /usr/src/app

COPY bot.py .
COPY requirement.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirement.txt

CMD ["python", "bot.py"]