# flask_ner

## Description
Exposing spacy ner models over an API


![flask_ner](https://user-images.githubusercontent.com/81632740/113435977-c492ad80-93db-11eb-9de0-c03a25434a0b.png)


## Setup

```sh
git clone https://github.com/crisp3r/flask_ner.git
```

### Server

```sh
$ cd flask_ner
$ docker build -t flaskner_backend -f flask.Dockerfile
$ docker run -d flaskner_backend --name backend
```

### WebApp

```sh
$ cd flask_ner/web
$ npm start
```

## Demo
