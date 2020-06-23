# python-flaskapi

'python-flaskapi' is a simple RESTful API using Python Flask which retrieved records from users table on MySQL DB


## Database Preparation

Run the file db.sql to create table and populate data

## OS ENV Preparation

Set your OS Environment variables for the following
DBHOST
DBUSER
DBPASSWORD
DBNAME


## Setting Up

Create Python Env

```bash
 $ python3 -m venv pyflaskdbenv
```

Activate Python Env
```bash
 $ source pyflaskdbenv/bin/activate
```
Install From Requirements
```bash
 $ pip3 install -r requirements.txt
```


## Run Application

```bash
 $ gunicorn --bind="0.0.0.0:8080" flaskdb:application
```

