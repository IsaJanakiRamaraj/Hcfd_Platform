from datetime import datetime
import random
from pathlib import Path
import pandas as pd
from faker import Faker

fake = Faker()
patients = []
def gen_patients(n,zip_code):
    for i in range(n):
        patients.append(
            {
                "patient_id": f"{i + 1:09}",
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "gender": random.choice(["M", "F"]),
                "dob": fake.date_of_birth(minimum_age=0, maximum_age=100),
                "death_date": random.choice([""]),
                "zip_code": f"{random.choice(zip_code)}",
                "address": fake.street_address(),
                "city": fake.city(),
                "state": fake.state_abbr(),
                "effective_from": fake.date_between(start_date="-2y", end_date="today"),
                "effective_to": fake.date_between(start_date="today", end_date="+2y"),
            }
        )
    base_path = Path(__file__).resolve().parent.parent
    file_name = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    file_path = str(base_path) + '/output/patients_' + file_name + '.csv'
    df = pd.DataFrame(patients)
    df.to_csv(file_path, index=False)
    return df
    