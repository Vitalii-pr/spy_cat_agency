
from fastapi import APIRouter, HTTPException


from .models import Cat
from .schemas import CatSchema, UpdateCat

from ..service import db_session




cats_router = APIRouter()


@cats_router.get("/", status_code=200, response_model=list[CatSchema])
def get_all_cats(db: db_session) -> list[CatSchema]:
    all_cats = db.query(Cat).all()
    return all_cats


@cats_router.post("/create", status_code=200, response_model=CatSchema)
def add_cat(db: db_session, cat_data: CatSchema) -> CatSchema:
    db.add(Cat(**cat_data.model_dump(include=["name", "salary", "year", "breed"])))
    db.commit()
    return cat_data

@cats_router.get('/{cat_id}/', status_code=200, response_model=CatSchema)
def get_cat_by_id(db:db_session, cat_id:int):
    cat_by_id:Cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat_by_id:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat_by_id


@cats_router.put("/update/{cat_id}/", status_code=400, response_model=CatSchema)
def update_salary(cat_id:int, cat_info:UpdateCat, db: db_session):
    cat = get_cat_by_id(db, cat_id)
    cat.salary = cat_info.salary
    db.commit()
    return cat


@cats_router.delete('/delete/{cat_id}', status_code=200, response_model=CatSchema)
def delete_cat(db: db_session, cat_id: int):
    cat_to_delete:Cat = db.query(Cat).get(cat_id)
    if not cat_to_delete:
        raise HTTPException(status_code=404, detail="Cat not found")
    db.delete(cat_to_delete)
    db.commit()
    return cat_to_delete

    
