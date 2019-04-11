FROM python:3.6
MAINTAINER Piotr Rybinski 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000