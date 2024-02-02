from typing import List, Optional
from datetime import datetime

from app.database.database import Database, NoResultsFoundException

from app.helpers.helpers import convert_string_to_datetime
from app.models.measure import get_measure_by_id, Measure


DATABASE_SERVICE = Database()

class Visit:
    def __init__(
        self,
        visit_id: int,
        patient_id: int, 
        doctor_id: int,
        visit_date: int,
        diagnose: str,
        measure: Measure
        ):
        self.visit_id = visit_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.visit_date = visit_date
        self.diagnose = diagnose
        self.measure = measure
    

def fetch_visits_by_patient_id_and_dates(patient_id: int, from_date: datetime, to_date: datetime, database_service: Optional[Database] = DATABASE_SERVICE) -> List[Visit]:
    try:
        visit_history = database_service.get_visits_by_patient_id(patient_id)
    except NoResultsFoundException:
        return None

    visit_list = []
    # Normally a DB would do the filtering by date but here I'll do it by hand
    for visit in visit_history:
        visit_date = convert_string_to_datetime(visit)

        # Exclude visits out of range
        if visit_date < from_date or visit_date > to_date:
            continue

        visit_record = visit_history[visit]
        measure_id = visit_record.get('measures_id')
        measure = get_measure_by_id(measure_id)
        visit_list.append(
            Visit(
                visit_id=visit_record.get('visit_id'),
                patient_id=visit_record.get('patient_id'),
                doctor_id=visit_record.get('doctor_id'),
                visit_date=visit_date,
                diagnose=visit_record.get('diagnose'),
                measure=measure
                )
            )
    
    return visit_list
