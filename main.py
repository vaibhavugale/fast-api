import json
from fastapi import FastAPI, HTTPException,Path,Query
from pathlib import Path as Ph
from typing import List, Dict, Any

app = FastAPI()


def load_data() -> List[Dict[str, Any]]:
    file_path = Ph("patient.json")
    if not file_path.exists():
        return []

    with open(file_path, "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/patient/{p_id}")
def get_patient(
    p_id: str = Path(...,description="Id of the patient in the DB",example="pat_001"),
    sort_by=Query("Sort key"),
    order=Query("Sort order")
    ):

    data = load_data()
    patient = next((p for p in data if p["id"] == p_id), None)

    print(patient)

    if patient:
        return patient
    
    raise HTTPException(404,"Patient not found !!!")
