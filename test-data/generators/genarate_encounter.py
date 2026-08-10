from faker import Faker
from datetime import datetime
from pathlib import Path
import pandas as pd

encounter = []
fake = Faker()

def gen_encounter(n, patient_id, provider_id, facility_id, diagnosis_code):
    for i in range(n):
        encounter.append(
            {
                "encounter_id": f"{i + 1:06}",
                "patient_id": fake.random_element(elements=patient_id),
                "provider_id": fake.random_element(elements=provider_id),
                "facility_id": fake.random_element(elements=facility_id),
                "encounter_date": fake.date_between(start_date="-2y", end_date="today"),
                "encounter_start_time": fake.date_between(
                    start_date="-3y", end_date="today"
                ),
                "encounter_end_time": fake.date_between(
                    start_date="-3y", end_date="-1y"
                ),
                "diagnosis_code": fake.random_element(elements=diagnosis_code),
                "encounter_type": fake.random_element(
                    elements=["Office", "ER", "inpatient"]
                ),
            }
        )
    base_path = Path(__file__).resolve().parent.parent
    file_name = '/output/encounter_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
    file_path = str(base_path) + file_name
    df = pd.DataFrame(encounter)
    df.to_csv(file_path, index=False)
    return df