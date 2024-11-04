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


[LINK TO POSTMAN](https://bold-spaceship-277786.postman.co/workspace/My-Workspace~85ff1f14-b8a6-4fda-8605-c959635be063/collection/20679108-728c9c9c-fbd6-4050-86a9-de90197a5f5b?action=share&creator=20679108)
