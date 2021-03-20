FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000

<<<<<<< HEAD
CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']
=======
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
>>>>>>> 457f71f760132d4ee378b81dd665dbeaa422d20b
