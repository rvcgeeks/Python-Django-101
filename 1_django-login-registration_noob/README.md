# Django login system - simple and noob

This is the resource material for "Python Django 101"
which is a simple login system with a local database.

This project demonstrates basic django application, along with
1) creating django apps
2) sessions in django
3) error message passing for validation
4) use of forms in django
5) Models in django

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This application was tested on Kali Linux 2019.3

1) Python
2) Django framework
3) bcrypt library

To install the requirements one can run,
```
pip install -r requirements.txt
```
with super user privileges 

## Deployment

first create migrations for 'User' model in myapp by
```
python manage.py makemigrations user_auth
```

create a local database dump by migrating the project models by
```
python manage.py migrate
```

Open up the development server by
```
python manage.py runserver
```

Then browse to localhost:8000 to see the site running


## Author

* **Rajas Chavadekar** 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

