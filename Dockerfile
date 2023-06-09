FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD uvicorn app:app --host 0.0.0.0
