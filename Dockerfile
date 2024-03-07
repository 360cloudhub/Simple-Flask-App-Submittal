FROM python:3.8-slim-buster

WORKDIR /app
ADD ./requirements.txt requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app

EXPOSE 5000
CMD ["python", "app.py"]