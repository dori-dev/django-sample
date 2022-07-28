# Django Sample

The sample project for django framework.

#

# How to Run Project

## Download Codes

```
git clone https://github.com/dori-dev/django-sample.git
```

```
cd django-sample
```

## Build Virtual Environment

```
python -m venv env
```

```
source env/bin/activate
```

## Install Project Requirements

```
pip install -r requirements.txt
```

## Create .Env File

set your environment variables in `.env.local` to `.env.production`.<br>

## Set STATE Variable

if you doesn't set `STATE` environ variable, project run with `debug=False`

```
export STATE=LOCAL
```

## Migrate Models

```
python manage.py makemigrations notes
```

```
python manage.py migrate
```

## Add Super User

```
python manage.py createsuperuser
```

## Run Codes

```
python manage.py runserver
```

## Open On Browser

Home Page: [127.0.0.1:8000](http://127.0.0.1:8000/)<br>
Admin Page: [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

#

# How to Deploy on Heroku

Push to Heroku:

```
heroku login
```

```
heroku create
```

```
git push heroku master
```

Run bash on Heroku with `heroku run bash` and write this commands:

```
python manage.py makemigrations notes
```

```
python manage.py migrate
```

```
python manage.py collectstatic
```

```
python manage.py createsuperuser
```

Open your website:

```
heroku open
```

See Logs:

```
heroku logs --tail
```

#

## Links

Demo of Project: [dori-django-sample.herokuapp.com](https://dori-django-sample.herokuapp.com/)

Download Source Code: [Click Here](https://github.com/dori-dev/django-sample/archive/refs/heads/master.zip)

My Github Account: [Click Here](https://github.com/dori-dev/)
