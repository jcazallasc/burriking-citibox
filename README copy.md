# lana-python-challenge

## Index

- [Challenge](docs/challenge.md) 
- [API doc](docs/api/checkout-backend.md) 
- [Frontend doc](docs/checkout-frontend.md)
- [How it was developed](docs/how-it-was-developed.md) 

## Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 

## How to run the app?
```bash
docker-compose up
```
This command will expose the app under `http://localhost:8000/`

Also, the first time, `docker-compose` will run the migrations and run the commands (`load_products` and `load_offers`) to populate the database. 

## How to enter to the container?
After the previous step.

```bash
docker-compose exec app sh
```

## How to run tests?
Once inside the container:
```bash
python manage.py tests
```

## How to run flake8?
Once inside the container:
```bash
flake8
```

## How to run the django commands?
Once inside the container:
```bash
python manage.py [command_name]
```

There are two commands: load_products and load_offers. Those commands import data from csv files

## How to create a super user?
Once inside the container:
```bash
python manage.py createsuperuser
```

Now you can access via `http://localhost:8000/admin/`