# django-project-template

django-project-template is a simple project template for Django based projects. 
PRs for adding new features or any bug fixes are always welcome :smile:.

## Features
- For Django 2.2
- Works with Python 3.6
- Comes with custom user model ready to go
- Pre-built `accounts` app to handle new user sign up via an account activation email.
- [12-Factor](https://12factor.net/) based settings via `python-decouple`
- `Procfile` for deploying to Heroku 

The template structure (only including important stuff) is as follows:
```
├── apps                           <- contains all the apps for the project. New apps should be added to this particular package only.
│   ├── __init__.py
│   ├── accounts                   <- 'accounts' app to handler new user registration and authentication, along with a custom user model.
│   ├── pages                      <- 'pages' app to host all the static/general web pages such as the 'landing' page or the 'about' page.
├── manage.py
├── Procfile                       <- Procfile for Heroku.
├── project_name
│   ├── __init__.py
│   ├── settings                   <- settings package for the project.
│   │   ├── __init__.py
│   │   ├── base.py                <- settings common to both development and production.            
│   │   ├── development.py         <- settings unique to development.
│   │   ├── production.py          <- settings unique to production.
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── runtime.txt
├── static                         <- static files that are to be used throughout the project.
│   ├── css
│   ├── img
│   └── js
└── templates                      <- templates to be used throughout the project.
    ├── base.html                  <- the base template for the project. To be inherited and overridden by every other template of the project. 
```
## How to Install
```bash
$ django-admin.py startproject \
  --template=https://github.com/alfarhanzahedi/django-project-template/archive/master.zip \
  --name=Procfile \
  --extension=py \
  project_name
$ cd project_name
$ pip install -r requirements.txt
$ python manage.py runserver
```
It is considered good practice to run the above commands in a new and separate virtual environment. Read more about virtual environments [here](https://realpython.com/python-virtual-environments-a-primer/).

## Environment Variables

All the required environment variables are availabled in `.env.example` along with their usage explanation.

## Deployment
The project template contains the `Procfile` for deploying it to Heroku.
Within your project directory, run the following commands in the sequence they appear. 
```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser (optional)
```
Also, do not forget to set the project environment variables (under `env`). They can added via the web interface under the project's settings tab (Config Vars). They can also be added via `heroku-cli` also. Instructions can be found [here](https://devcenter.heroku.com/articles/config-vars).  

You should have a Heroku account (if not, create one [here](https://heroku.com/)), and Heroku CLI installed for the commands to work (if not, installation instructions can be found [here](https://devcenter.heroku.com/articles/heroku-cli)).

## License
The MIT License

Copyright (c) 2019 Alfarhan Zahedi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.