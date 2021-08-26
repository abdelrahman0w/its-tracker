# ITS Tracker

- [ITS Tracker](#its-tracker)
  - [Description](#description)
  - [Installation](#installation)
    - [Installation Requirements](#installation-requirements)
    - [Installation Steps](#installation-steps)
  - [Usage](#usage)

## Description

ITS Tracker is a web-based dashboard and admin panel created with Django. It's used to monitor and control an Intelligent Traffic System.

To try a demo, go to: [its.pythonanywhere.com](https://its.pythonanywhere.com/). and use the following credentials:

- username: demo
- password: De.mo.123

## Installation

### Installation Requirements

Basically, it's a django-based website. That's why everything you will need is python and python libraries as follows.

- [Python >= 3.7.*](https://www.python.org/)
- The following libraries:

    - asgiref==3.3.4
    - dj-database-url==0.5.0
    - dj-static==0.0.6
    - Django==3.2.3
    - geographiclib==1.50
    - Pillow==8.2.0
    - pytz==2021.1
    - sqlparse==0.4.1
    - static3==0.7.0
    - whitenoise==5.2.0
    - python-decouple==3.4
    - django-filter==2.4.0
    - django-crispy==forms-1.12.0
    - geocoder==1.38.1

### Installation Steps

To Initializing the project on your local machine, you have to do the following:

1. Install **[Python >= 3.7.*](https://www.python.org/)** from the official website (["https://www.python.org/"](https://www.python.org/))
2. Run the following
    ```bash
    python3 -m pip install -r requirements.txt
    ```

## Usage

**To start using the project on your local machine, run the following commands:**

```bash
python3 manage.py collectstatics
```

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

```bash
python3 manage.py runserver
```

**To create a super user, run the following commands:**

```bash
python3 manage.py makesuperuser
```
