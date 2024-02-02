from app.medical_report import MedicalReport

patient_id = input('\nInput patient ID (Available ids are 1111, 2222, 3333)\n>>')
selected_date = input('\nInput data for report with format MM/DD/YYYY the report will show historic from 12 prior to the input date (press enter to use today\'s date\n>>')

patient_id_int = None
try:
    patient_id_int = int(patient_id)
except Exception:
    print('Invalid user ID use numbers only')

if patient_id_int:
    MedicalReport().generate_patient_summary_by_id(patient_id_int, selected_date)