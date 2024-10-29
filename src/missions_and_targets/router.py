from fastapi import APIRouter, HTTPException

from .schemas import MissionSchema, TargetSchema, NoteSchema
from ..cat.schemas import CatIdSchema

from .models import Mission, Target

from ..cat.models import Cat


from ..service import db_session, MAX_TARGET_PER_MISSION



mission_router = APIRouter()


@mission_router.get('/', status_code=200, response_model=list[MissionSchema])
def get_all_missions(db: db_session):
    return db.query(Mission).all()

@mission_router.get('/{mission_id}', status_code=200, response_model=MissionSchema)
def get_mission(db:db_session, mission_id:int):
    mission = db.query(Mission).filter(Mission.id==mission_id).first()
    if not mission:
        raise HTTPException(status_code=400, detail='Mission not found')
    return mission

@mission_router.post('/create', status_code=200, response_model=MissionSchema)
def create_mission(db:db_session, targets_info:list[TargetSchema], cat_info:CatIdSchema):

    new_mission = Mission()
    amount = min(len(targets_info), MAX_TARGET_PER_MISSION)
    cat_id = db.query(Cat).filter(Cat.id == cat_info.id).first()

    for i in range(amount):
        target = Target(**targets_info[i-1].model_dump())
        target.mission = new_mission
        new_mission.targets.append(target)
    new_mission.cat_id = cat_id if cat_id else None

    new_mission.check_and_complete_mission(db)
    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)

    return new_mission


@mission_router.delete('/delete/{mission_id}', status_code=200, response_model=MissionSchema)
def delete_mission(db:db_session, mission_id:int):
    mission_to_delete = get_mission(db, mission_id)

    if mission_to_delete.cat_id:
        raise HTTPException(status_code=400, detail='Mission assigned to cat')
    
    db.delete(mission_to_delete)
    db.commit()
    return mission_to_delete


@mission_router.put('/{mission_id}/assing_cat', status_code=200, response_model=MissionSchema)
def assign_cat(db:db_session, mission_id:int, cat_info:CatIdSchema):
    mission_for_cat = get_mission(db, mission_id)
    if  mission_for_cat.complete:
        raise HTTPException(status_code=400, detail="This mission already completed")
    mission_for_cat.cat_id = cat_info.id
    return mission_for_cat



@mission_router.put("/targets/{target_id}/change_complete", status_code=200)
def complete_target(db: db_session, target_id: int):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    target.complete = True
    db.add(target)
    db.commit()
    target.mission.check_and_complete_mission(db)

    return {"status": "Target marked as complete"}

@mission_router.put("/targets/{target_id}/update_notes", status_code=200, response_model=TargetSchema)
def update_target_notes(db: db_session, target_id: int, new_notes: NoteSchema):
    target = db.query(Target).filter(Target.id == target_id).first()


    if not target:
        raise HTTPException(status_code=404, detail="Target not found")

    if target.complete:
        raise HTTPException(
            status_code=400, detail="Cannot update notes for a completed target"
        )
    
    if target.mission.complete:
        raise HTTPException(
            status_code=400,
            detail="Cannot update notes for a target belonging to a completed mission",
        )

    target.notes = new_notes.text
    db.add(target)
    db.commit()

    return target
