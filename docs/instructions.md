# Instructions

## Index

- [Specs](README.md) 
- [Instructions](docs/instructions.md) 
- [How it was developed](docs/how-it-was-developed.md) 
- [API doc](docs/api/orders.md) 

## Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 

## How to run the app?
```bash
docker-compose up
```
This command will expose the app under `http://localhost:8000/`

The app is separated in two containers: app and app_test.

Also, the first time, `docker-compose` will run the migrations and run the command (`populate_db`) to populate the database with Products, Options and Offers for the container `app`. 

## How to enter to the container?
After the previous step.

```bash
docker-compose run app sh
```

Or

```bash
docker-compose run app_test sh
```

## How to run tests?
Once inside the `app_test` container:
```bash
python manage.py tests
```

Take into account dev dependencies are just installed in `app_test` container.

## How to check coverage?
Once inside the `app_test` container:
```bash
coverage run --source='.' manage.py test

coverage report
```

## How to run flake8?
Once inside the container:
```bash
flake8 .
```

## How to run isort?
Once inside the container:
```bash
isort -c .
```

## How to run the django commands?
Once inside the container:
```bash
python manage.py [command_name]
```

There are two commands: populate_db and create_super_user (it will create my super user 😁).

## How to create a super user?
Once inside the container:
```bash
python manage.py createsuperuser
```

Now you can access via `http://localhost:8000/admin/`