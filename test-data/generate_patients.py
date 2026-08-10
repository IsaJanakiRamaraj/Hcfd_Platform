from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime
import random 

fake = Faker()
patients = []
for i in range(10):
    patients.append(
        {
            "patient_id": f"p{i + 1:06}",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(["M", "F"]),
            "dob": fake.date_of_birth(minimum_age=18, maximum_age=60),
            "death_date": None,
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip": fake.postcode(),
        }
    )

df = pd.DataFrame(patients)
f_name =  './patients/'+ 'patients' + str(datetime.now().timestamp()) + '.csv'
df.to_csv(f_name, index = False) 