import statistics
from typing import Optional
from datetime import datetime, timedelta

from app.models.patient import fetch_patient_by_id
from app.models.visit import fetch_visits_by_patient_id_and_dates
from app.helpers.helpers import calculate_bmi, convert_string_to_datetime


class MedicalReport: 
    def generate_patient_summary_by_id(self, patient_id: int, date: Optional[str] = None) -> None:
        # Ensure patient is an integer
        # Obtain patient model if not found abort
        patient = fetch_patient_by_id(patient_id)
        if not patient:
            print('Patient not found')
            return
        
        # Calculate patient BMI
        patient_bmi = calculate_bmi(
            weight_lbs=patient.weight_lbs,
            height_feet=patient.height_feet
            )

        # Obtain patient's last 12 months of visits up to the report date
        try:
            report_date = convert_string_to_datetime(date) if date else datetime.now()
        except Exception:
            print('Error while parsing date')
            return

        visit_history = fetch_visits_by_patient_id_and_dates(
            patient_id=patient.patient_id,
            from_date=report_date - timedelta(days=365),
            to_date=report_date
        )

        patient_birthday_string = patient.birthday.strftime('%m/%d/%Y')
        print('\n\n--------------Patient summary---------------')
        print(f'Name: {patient.first_name} {patient.last_name}')
        print(f'Birthday {patient_birthday_string}')
        print(f'Gender: {patient.gender}')
        print(f'Height: {patient.height_feet}')
        print(f'Weight: {patient.weight_lbs}')
        print(f'BMI: {patient_bmi}')

        if visit_history:
            # Initialize historic data
            heart_rate_history = []
            max_heart_rate = 0
            min_heart_rate = 5000

            diastolic_pressure_history = []
            max_diastolic_pressure = 0
            min_diastolic_pressure = 5000

            systolic_pressure_history = []
            max_systolic_pressure = 0
            min_systolic_pressure = 5000

            for visit in visit_history:
                # Keep record of measures and its maxes
                heart_rate_history.append(visit.measure.heart_rate)
                if visit.measure.heart_rate > max_heart_rate:
                    max_heart_rate = visit.measure.heart_rate
                if visit.measure.heart_rate < min_heart_rate:
                    min_heart_rate = visit.measure.heart_rate

                diastolic_pressure_history.append(visit.measure.diastolic_pressure)
                if visit.measure.diastolic_pressure > max_diastolic_pressure:
                    max_diastolic_pressure = visit.measure.diastolic_pressure
                if visit.measure.diastolic_pressure < min_diastolic_pressure:
                    min_diastolic_pressure = visit.measure.diastolic_pressure

                systolic_pressure_history.append(visit.measure.systolic_pressure)
                if visit.measure.systolic_pressure > max_systolic_pressure:
                    max_systolic_pressure = visit.measure.systolic_pressure
                if visit.measure.systolic_pressure < min_systolic_pressure:
                    min_systolic_pressure = visit.measure.systolic_pressure

            print(f'\nMax heart rate {max_heart_rate}')
            print(f'Mean heart rate {statistics.mean(heart_rate_history)}')
            print(f'Median heart rate {statistics.median(heart_rate_history)}')
            print(f'Min heart rate {min_heart_rate}')

            print(f'\nMax diastolic pressure {max_diastolic_pressure}')
            print(f'Mean diastolic pressure {statistics.mean(diastolic_pressure_history)}')
            print(f'Median diastolic pressure {statistics.median(diastolic_pressure_history)}')
            print(f'Min diastolic pressure {min_diastolic_pressure}')

            print(f'\nMax systolic pressure {max_systolic_pressure}')
            print(f'Mean systolic pressure {statistics.mean(systolic_pressure_history)}')
            print(f'Median systolic pressure {statistics.median(systolic_pressure_history)}')
            print(f'Min systolic pressure {min_systolic_pressure}')


            print('\n\n--------------Visit summary---------------')
            print('Date              Doctor Id         Diagnose           Heart rate')
            # This could be printed in the loop above but I decided to split it for a better presentation
            for visit in visit_history:
                visit_date_str = visit.visit_date.strftime('%m/%d/%Y')
                print(f'{visit_date_str}         {visit.doctor_id}           {visit.diagnose}         {visit.measure.heart_rate}')
        else:
            print('\n\nNo visits available in selected time period')
        
        print('\n\n')
