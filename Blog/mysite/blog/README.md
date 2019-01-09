# Django Simple Blog Demo

## About

This is a demo project for simple blogging using Django.


It was made using **Python 3.6** + **Django** and database is **SQLite**.
**Bootstrap** was used for styling.


There is a login and registration functionality included.

User has his own blog page, where he can add new blog posts. 
Every authenticated user can comment on posts made by other users.

Non-authenticated users can see all blog posts, but cannot add new posts or comment.

App is covered with tests.

## Prerequisites

\[Optional\] Install virtual environment:

```bash
$ python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Run migrations:
```bash
$ python manage.py migrate
```

Initialize data:
```bash
$ python manage.py loaddata users posts comments
```

Run server on port 8000:
```bash
$ python manage.py runserver 8000
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$ chmod +x scripts/run.sh
$ scripts/run.sh
```

## Post Installation

Go to the web browser and visit `http://localhost:8000/home`

Admin username: **admin**

Admin password: **adminpassword**

User username: **abcd**

User password: **abcdpassword**

## Helper Tools

### Django Admin

It is possible to add additional admin user who can login to the admin site. Run the following command:
```bash
$ python manage.py createsuperuser
```
Enter your desired username and press enter.
```bash
Username: admin_username
```
You will then be prompted for your desired email address:
```bash
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```bash
Password: **********
Password (again): *********
Superuser created successfully.
```

Go to the web browser and visit `http://localhost:8000/admin`

### Tests

#### Default
Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Running tests:
```bash
$ python manage.py test blog
```


``` 

					
