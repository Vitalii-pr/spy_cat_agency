# Spy_cat_agency


## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your machine
- [Poetry](https://python-poetry.org/docs/) for dependency management


1. Create a .env file with the database URL:

```
SQLALCHEMY_DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
```
2. Install dependies using poetry
```
poetry install 
```
3. Make migrations and migrate to DB
```
alembic revision -m "initial"
alembic upgrade head
```

4. Run application 
```
uvicorn src.main:app --reload
```


[LINK TO POSTMAN](https://api.postman.com/collections/20679108-728c9c9c-fbd6-4050-86a9-de90197a5f5b?access_key=PMAT-01JBCRP7MMNZM1M78F9X6TAAX3/)