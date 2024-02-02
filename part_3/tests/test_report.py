import pytest
from datetime import datetime

from tests.fixtures import PATIENT_FIXTURE
from tests.fixtures import PATIENTS_DOCTORS_FIXTURE
from tests.fixtures import VISITS_FIXTURE
from tests.fixtures import MEASURE_FIXTURE
from tests.fixtures import MOCK_PATIENT
from tests.fixtures import MOCK_VISITS

from app.medical_report import MedicalReport


def test_generate_patient_summary_by_id(mocker):
    # Set up
    mock_patient = mocker.patch('app.medical_report.fetch_patient_by_id', return_value=MOCK_PATIENT)
    mock_visits = mocker.patch('app.medical_report.fetch_visits_by_patient_id_and_dates', return_value=MOCK_VISITS)

    # Run the thing
    MedicalReport().generate_patient_summary_by_id(patient_id=5555, date='08/13/2021')

    # Check results
    mock_patient.assert_called_once_with(5555)
    mock_visits.assert_called_once_with(from_date=datetime(2020, 8, 13, 0, 0), patient_id=5555, to_date=datetime(2021, 8, 13, 0, 0))

def test_generate_patient_summary_by_id_no_patient(mocker):
    # Set up
    mock_patient = mocker.patch('app.medical_report.fetch_patient_by_id', return_value=None)
    mock_visits = mocker.patch('app.medical_report.fetch_visits_by_patient_id_and_dates', return_value=MOCK_VISITS)

    # Run the thing
    MedicalReport().generate_patient_summary_by_id(patient_id=5555, date='08/13/2021')

    # Check results
    mock_patient.assert_called_once_with(5555)
    mock_visits.assert_not_called()

def test_generate_patient_summary_bad_date(mocker):
    # Set up
    mock_patient = mocker.patch('app.medical_report.fetch_patient_by_id', return_value=MOCK_PATIENT)
    mock_visits = mocker.patch('app.medical_report.fetch_visits_by_patient_id_and_dates', return_value=MOCK_VISITS)

    # Run the thing
    MedicalReport().generate_patient_summary_by_id(patient_id=5555, date='99/15/2021@')

    # Check results
    mock_patient.assert_called_once_with(5555)
    mock_visits.assert_not_called()


def test_generate_patient_summary_by_id_no_visits(mocker):
    # Set up
    mock_patient = mocker.patch('app.medical_report.fetch_patient_by_id', return_value=MOCK_PATIENT)
    mock_visits = mocker.patch('app.medical_report.fetch_visits_by_patient_id_and_dates', return_value=None)

    # Run the thing
    MedicalReport().generate_patient_summary_by_id(patient_id=5555, date='08/13/2021')

    # Check results
    mock_patient.assert_called_once_with(5555)
    mock_visits.assert_called_once_with(from_date=datetime(2020, 8, 13, 0, 0), patient_id=5555, to_date=datetime(2021, 8, 13, 0, 0))