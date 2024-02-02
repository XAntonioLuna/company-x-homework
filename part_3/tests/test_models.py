from datetime import datetime
from app.database.database import Database
from app.models.patient import Patient, fetch_patient_by_id
from app.models.visit import fetch_visits_by_patient_id_and_dates
from app.models.measure import get_measure_by_id

from tests.fixtures import PATIENT_FIXTURE
from tests.fixtures import PATIENTS_DOCTORS_FIXTURE
from tests.fixtures import VISITS_FIXTURE
from tests.fixtures import MEASURE_FIXTURE
from tests.fixtures import MOCK_PATIENT


def test_get_patient():
    mock_database = Database(
        patients=PATIENT_FIXTURE,
        patients_doctors=PATIENTS_DOCTORS_FIXTURE
    )

    expected_value = MOCK_PATIENT

    result = fetch_patient_by_id(5555, mock_database)

    assert result.patient_id == expected_value.patient_id
    assert result.first_name == expected_value.first_name


def test_no_patient():
    mock_database = Database(
        patients=PATIENT_FIXTURE,
        patients_doctors=PATIENTS_DOCTORS_FIXTURE
    )
    assert not fetch_patient_by_id(7777, mock_database)


def test_get_visits():
    mock_database = Database(
        visits=VISITS_FIXTURE
    )

    from_date = datetime(2021,2,1)
    to_date = datetime(2021,9,1)


    result = fetch_visits_by_patient_id_and_dates(5555, from_date, to_date, mock_database)

    assert len(result) == 2
    assert result[0].diagnose == 'DIAGNOSE 1'


def test_get_visits_variable_date():
    mock_database = Database(
        visits=VISITS_FIXTURE
    )

    from_date = datetime(2020,1,1)
    to_date = datetime(2020,12,31)


    result = fetch_visits_by_patient_id_and_dates(5555, from_date, to_date, mock_database)

    assert len(result) == 1
    assert result[0].diagnose == 'DIAGNOSE 3'


def test_get_no_visits():
    mock_database = Database(
        visits=VISITS_FIXTURE
    )

    from_date = datetime(2020,12,31)
    to_date = datetime(2020,1,1)


    result = fetch_visits_by_patient_id_and_dates(7777, from_date, to_date, mock_database)

    assert not result


def test_get_measures():
    mock_database = Database(
        measures=MEASURE_FIXTURE
    )

    result = get_measure_by_id(8123, mock_database)

    assert result.height == 5.9


def test_get_no_measures():
    mock_database = Database(
        measures=MEASURE_FIXTURE
    )

    result = get_measure_by_id(8888, mock_database)

    assert not result
