from typing import Optional
from app.database.database import Database, NoResultsFoundException

DATABASE_SERVICE = Database()

class Measure:
    def __init__(
        self,
        measure_id: int,
        height: Optional[float] = None,
        weight: Optional[float] = None,
        heart_rate: Optional[int] = None,
        diastolic_pressure: Optional[int] = None,
        systolic_pressure: Optional[int] = None
        ):
        self.measure_id = measure_id
        self.height = height
        self.weight = weight
        self.heart_rate = heart_rate
        self.diastolic_pressure = diastolic_pressure
        self.systolic_pressure = systolic_pressure

def get_measure_by_id(measure_id: int, database_service: Optional[Database] = DATABASE_SERVICE) -> Measure:
    try:
        measure = database_service.get_measure_by_id(measure_id)
    except NoResultsFoundException:
        return None

    return Measure(
        measure_id = measure_id,
        height = measure.get('height'),
        weight = measure.get('weight'),
        heart_rate = measure.get('heart_rate'),
        diastolic_pressure = measure.get('diastolic_pressure'),
        systolic_pressure = measure.get('systolic_pressure')
    )