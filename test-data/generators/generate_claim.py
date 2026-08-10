from faker import Faker
from datetime import datetime
from pathlib import Path
import pandas as pd

claim = []
fake = Faker()
def gen_claim(n, patient_id, provider_id, facility_id, encounter_id, diagnosis_code, procedure_code):
    for i in range(n):
        claim.append(
            {
                "claim_id": f"{i + 1:010}",
                "patient_id": fake.random_element(elements=patient_id),
                "provider_id": fake.random_element(elements=provider_id),
                "facility_id": fake.random_element(elements=facility_id),
                "encounter_id": fake.random_element(elements=encounter_id),
                "claim_date": fake.date_between(start_date="-2y", end_date="today"),
                "service_date": fake.date_between(start_date="-2y", end_date="today"),
                "diagnosis_code": fake.random_element(elements=diagnosis_code),
                "procedure_code": fake.random_element(elements=procedure_code),
                "units": fake.random_int(min=1, max=10),
                "claim_amount": fake.pydecimal(
                    left_digits=5, right_digits=2, positive=True
                ),
                "claim_status": fake.random_element(["approved", "denied", "pending"]),
            }
        )
    df = pd.DataFrame(claim)
    base_path = Path(__file__).resolve().parent.parent
    file_name = 'claim_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
    file_path = base_path / 'output' / file_name
    df.to_csv(file_path, index=False)
