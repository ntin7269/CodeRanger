FROM python:3.11
RUN apt-get update && apt-get install -y g++
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=OJ.settings
ENV PYTHONBUFERED=1

CMD ["python","manage.py","runserver","0.0.0.0:8000"]