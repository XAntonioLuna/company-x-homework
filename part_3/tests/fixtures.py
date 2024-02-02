from datetime import datetime
from app.models.patient import Patient
from app.models.visit import Visit
from app.models.measure import Measure

PATIENT_FIXTURE = {
    5555: {
        'patient_first_name': 'Jane',
        'patient_last_name': 'Doe',
        'patient_birthday': datetime(2000,7,7),
        'patient_gender': 'female',
        'patient_most_recent_height': 5.9,
        'patient_most_recent_weight': 176.3,
    }
}

PATIENTS_DOCTORS_FIXTURE = {
    5555: [9007],
}

VISITS_FIXTURE = {
    5555: {
        '08/15/2021': {
            'measures_id': 8123,
            'doctor_id': 9123,
            'diagnose': 'DIAGNOSE 1'
        },
        '06/13/2021': {
            'measures_id': 8122,
            'doctor_id': 9123,
            'diagnose': 'DIAGNOSE 2'
        },
        '07/15/2020': {
            'measures_id': 8121,
            'doctor_id': 9123,
            'diagnose': 'DIAGNOSE 3'
        },
    }
}

MEASURE_FIXTURE = {
    8123: {
        'height': 5.9,
        'weight': 176.3,
        'heart_rate': 103,
        'diastolic_pressure': 120,
        'systolic_pressure': 80
    }
}

MOCK_PATIENT = Patient(
        patient_id=5555,
        first_name='Jane',
        last_name='Doe',
        birthday=datetime(2000,7,7),
        gender='female',
        weight_lbs=177,
        height_feet=5,
        treating_doctors=[9007]
    )

MEASURE_1 = Measure(
    measure_id = 8000,
    height = 5,
    weight = 177,
    heart_rate = 120,
    diastolic_pressure = 150,
    systolic_pressure = 90
)

VISIT_1 = Visit(
    visit_id=4000,
    patient_id=5555,
    doctor_id=9079,
    visit_date=datetime(2021,8,13),
    diagnose='High pressure',
    measure=MEASURE_1
)

MOCK_VISITS = [
    VISIT_1
]