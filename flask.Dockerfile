# init a base image (Spacy seems to work not in alpine but in ubuntu)
FROM python:3.8
# define the present working directory
WORKDIR /flask-ner
# copy the contents into the working dir
ADD . /flask-ner
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# install the current project as an editable package.
# this will add the current project in sys.path of python
# so that when performing lookups for other modules, python will
# also first look up in this package.
RUN pip install -e .
ENV FLASK_APP=/flask-ner/api/app.py
CMD ["flask", "run"]
# Expose 
EXPOSE 5000/tcp
