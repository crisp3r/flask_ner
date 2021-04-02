# init a base image (Alpine is small Linux distro)
FROM python:3.8.8-alpine
# define the present working directory
WORKDIR /flask-ner
# copy the contents into the working dir
ADD . /flask-ner
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
# FLASK_APP=api/app.py flask run
CMD ["FLASK_APP=api/app.py","flask", "run"]
EXPOSE 5000/tcp