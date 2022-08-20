FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /django/