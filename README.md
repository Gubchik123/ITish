<a href="https://gubchik123.pythonanywhere.com/" target="_blank"><img title="ITish" alt="Header image" src="./md_images/readme_header.png"></a>

_Blog site to practice working with the Flask framework and provide anyone the site to publish posts_

### Demo

Click **<a href="https://gubchik123.pythonanywhere.com/" target="_blank">here</a>** to open ITish blog site

<img title="Demo" alt="Demo image" src="./md_images/demo.jpg">

### Project modules (requirements.txt)gevent

<a href='https://pypi.org/project/Flask'><img alt='Flask' src='https://img.shields.io/pypi/v/Flask?label=Flask&color=blue'></a> <a href='https://pypi.org/project/Flask-Admin'><img alt='Flask-Admin' src='https://img.shields.io/pypi/v/Flask-Admin?label=Flask-Admin&color=blue'></a> <a href='https://pypi.org/project/Flask-Login'><img alt='Flask-Login' src='https://img.shields.io/pypi/v/Flask-Login?label=Flask-Login&color=blue'></a> <a href='https://pypi.org/project/Flask-Migrate'><img alt='Flask-Migrate' src='https://img.shields.io/pypi/v/Flask-Migrate?label=Flask-Migrate&color=blue'></a> <a href='https://pypi.org/project/Flask-SQLAlchemy'><img alt='Flask-SQLAlchemy' src='https://img.shields.io/pypi/v/Flask-SQLAlchemy?label=Flask-SQLAlchemy&color=blue'></a> <a href='https://pypi.org/project/Flask-WTF'><img alt='Flask-WTF' src='https://img.shields.io/pypi/v/Flask-WTF?label=Flask-WTF&color=blue'></a> <a href='https://pypi.org/project/email-validator'><img alt='email-validator' src='https://img.shields.io/pypi/v/email-validator?label=email-validator&color=blue'></a> <a href='https://pypi.org/project/PyMySQL'><img alt='PyMySQL' src='https://img.shields.io/pypi/v/PyMySQL?label=PyMySQL&color=blue'></a> <a href='https://pypi.org/project/python-dotenv'><img alt='python-dotenv' src='https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv&color=blue'></a>

---

### Site structure

The system consists of the following main functional blocks:

-   Registration, authentication and authorization;
-   Guest functionality;
-   User functionality;
-   Admin functionality.

#### Flask Blueprints

-   Auth (for working with registration, authentication and authorization);
-   Blog (for working with posts and others that are connected with them);
-   Profile (for working with user profiles and pages that are connected with them).

#### Technology stack

-   Backend:
    -   Python programming language;
    -   Flask framework with following extensions:
        -   Flask-Admin (for admin panel);
        -   Flask-Login (for 'auth' functionality);
        -   Flask-Migrate (for migrations);
        -   Flask-SQLAlchemy (for database using python objects);
        -   Flask-WTF (for rendering forms).
    -   MySQL / PostgreSQL database;
-   Frontend:
    -   HTML & CSS;
    -   JavaScript;
    -   Bootstrap 5.

### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`ADMIN_PASSWORD`
`SECRET_KEY`
`DATABASE_TEST_URI`
`DATABASE_PRODUCTION_URI`
`DATABASE_DEVELOPMENT_URI`

### Run Locally

Clone the project

```
  git clone https://github.com/Gubchik123/ITish.git
```

Go to the project directory

```
  cd ITish
```

Install dependencies

```
  pip install -r requirements/base.txt
```

Run the project

```
  python run.py / flask run run.py
```

> **Note:** Don't forget about environment variables
