from typing import Optional
from datetime import datetime

from app.database.database import Database, NoResultsFoundException

DATABASE_SERVICE = Database()

class Patient:
    def __init__(
        self, 
        patient_id: int,
        first_name: str,
        last_name: str,
        birthday: datetime,
        gender: str,
        weight_lbs: float,
        height_feet: float,
        treating_doctors: []
        ):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.weight_lbs = weight_lbs
        self.height_feet = height_feet
        self.treating_doctors = treating_doctors

def fetch_patient_by_id(patient_id: int, database_service: Optional[Database] = DATABASE_SERVICE) -> Optional[Patient]:
    try:
        patient_info, doctor_list = database_service.get_patient_information(patient_id)
    except NoResultsFoundException:
        return None

    return Patient(
        patient_id=patient_id,
        first_name=patient_info.get('patient_first_name'),
        last_name=patient_info.get('patient_last_name'),
        birthday=patient_info.get('patient_birthday'),
        gender=patient_info.get('patient_gender'),
        weight_lbs=patient_info.get('patient_most_recent_weight'),
        height_feet=patient_info.get('patient_most_recent_height'),
        treating_doctors=doctor_list,
        )
