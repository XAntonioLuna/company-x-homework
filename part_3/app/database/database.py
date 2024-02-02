from typing import Tuple
from datetime import datetime

#---------------Mock table data--------------------------
PATIENTS = {
    1111: {
        'patient_first_name': 'Antonio',
        'patient_last_name': 'Luna',
        'patient_birthday': datetime(1988,6,13),
        'patient_gender': 'male',
        'patient_most_recent_height': 5.9,
        'patient_most_recent_weight': 176.3,
    },
    2222: {
        'patient_first_name': 'Amy',
        'patient_last_name': 'Chang',
        'patient_birthday': datetime(1993,7,8),
        'patient_gender': 'female',
        'patient_most_recent_height': 5.4,
        'patient_most_recent_weight': 110.2,
    },
    3333: {
        'patient_first_name': 'Jennifer',
        'patient_last_name': 'Johnson',
        'patient_birthday': datetime(2000,1,15),
        'patient_gender': 'undisclosed',
        'patient_most_recent_height': 5.57,
        'patient_most_recent_weight': 141.09,
    }
}

PATIENTS_DOCTORS = {
    1111: [9123, 9567, 9007],
    2222: [9123],
    3333: [9567, 9007],
}

VISITS = {
    1111: {
        '08/15/2021': {
            'measures_id': 8123,
            'doctor_id': 9123,
            'diagnose': 'Tendency to HODL'
        },
        '06/13/2021': {
            'measures_id': 8122,
            'doctor_id': 9123,
            'diagnose': 'Allergy to polen'
        },
        '07/15/2020': {
            'measures_id': 8121,
            'doctor_id': 9123,
            'diagnose': 'Arrow to the knee'
        },
    }
}

MEASURES = {
    8123: {
        'height': 5.9,
        'weight': 176.3,
        'heart_rate': 103,
        'diastolic_pressure': 120,
        'systolic_pressure': 80
    },
    8122: {
        'height': 5.8,
        'weight': 186.3,
        'heart_rate': 102,
        'diastolic_pressure': 121,
        'systolic_pressure': 81
    },
    8121: {
        'height': 5.7,
        'weight': 196.3,
        'heart_rate': 101,
        'diastolic_pressure': 122,
        'systolic_pressure': 82
    },
}
#-----------------------------------------------------------

class NoResultsFoundException(Exception):
    pass

class Database:
    def __init__(
        self,
        patients = PATIENTS,
        patients_doctors = PATIENTS_DOCTORS,
        visits = VISITS,
        measures = MEASURES
    ):
        self.patients = patients
        self.patients_doctors = patients_doctors
        self.visits = visits
        self.measures = measures
    
    # Simulates a SELECT to Patients with a JOIN to PatientsDoctors
    def get_patient_information(self, patient_id: int) -> Tuple[dict, dict]:
        try:
            patient_info = self.patients[patient_id]
            doctor_list = self.patients_doctors[patient_id]
        except Exception:
            raise NoResultsFoundException

        return patient_info, doctor_list
    
    def get_visits_by_patient_id(self, patient_id: int) -> dict:
        try:
            visits = self.visits[patient_id]
        except Exception:
            raise NoResultsFoundException

        return visits
    
    def get_measure_by_id(self,measure_id: int) -> dict:
        try:
            measure = self.measures[measure_id]
        except Exception:
            raise NoResultsFoundException

        return measure