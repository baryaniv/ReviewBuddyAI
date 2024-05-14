FROM python:3.9

WORKDIR /app

COPY etc/requirements.txt . 

RUN apt-get update && apt-get install -y libhdf5-dev

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
