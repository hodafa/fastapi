# Use the official Python image
FROM python:3.9

WORKDIR /app

COPY . /app

# Install any needed packages
RUN pip install --no-cache-dir -r ./requirements.txt


