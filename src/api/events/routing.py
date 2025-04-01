from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlmodel import select, Session, SQLModel
from .model import Steps
from ..db.create import get_session
import pandas as pd

router=APIRouter()
#get details from csv file
@router.get("/load_data")
def input_data(session: Session=Depends(get_session)):
    # Get the data from the request body

    try:
        csv_files={
            'Steps': 'C:\\Users\\gaura\\Desktop\\Github\\API_to_SQL\\src\\api\\db\\steps_tracker_dataset.csv',
        }
        df=pd.read_csv(csv_files['Steps'])
        # Convert the DataFrame to a list of dictionaries
        for _,row in df.iterrows():
            event=Steps(
                date=row['date'],
                steps=row['steps'],
                distance_km=row['distance_km'],
                calories_burned=row['calories_burned'],
                active_minutes=row['active_minutes'],
                sleep_hours=row['sleep_hours'],
                water_intake_liters=row['water_intake_liters'],
                mood=row['mood']
            )
            session.add(event)

        session.commit()
        session.refresh(event)
        return {"message": "Data loaded successfully"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    


#get data
@router.get("/get_data")
def get_data(session: Session=Depends(get_session)):
    query=select(Steps).limit(10)
    event=session.exec(query).fetchall()
    #print([dict(row) for row in event])
    return [dict(row) for row in event]

@router.get("/test_data")
def test_data(session: Session=Depends(get_session)):
    query=(
        select(
        Steps,
        )
        .where(
            Steps.mood == "happy",
            )
        .order_by(
            Steps.distance_km.desc(),
            )
    )
    event=session.exec(query).fetchall()
    #print([dict(row) for row in event])
    return [dict(row) for row in event]
    