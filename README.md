# flask_ner

## DESCRIPTION
Exposing spacy ner models over an API


![flask_ner](https://user-images.githubusercontent.com/81632740/113435977-c492ad80-93db-11eb-9de0-c03a25434a0b.png)


## SETUP

```sh
git clone https://github.com/crisp3r/flask_ner.git
```

### Server

Docker

```sh
$ cd flask_ner
$ docker build -t flaskner_backend -f flask.Dockerfile
$ docker run -d flaskner_backend --name backend
```
Pip

```sh
$ cd flask_ner
$ pip install -r ./requirements.txt
$ FLASK_APP=api/app.py flask run
```

### WebApp

```sh
$ cd flask_ner/web
$ npm start
```

### Tests

```sh
$ cd flask_ner
$ source env/bin/activate
$ python -m pytest
```

## DEMO
TODO
