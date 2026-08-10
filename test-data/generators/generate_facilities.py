from faker import Faker
import pandas as pd
from datetime import datetime
from pathlib import Path
import random 

def gen_facilities(num: int, zip_codes ):
    fake = Faker()
    facilities = []
    for i in range(num):
        sample_row = zip_codes.sample(n=1).iloc[0]
        facilities.append(
            {
                "facility_id": f"f{0 + i:06}",
                "facility_name": f"{fake.company()} Hospital",
                "zip": sample_row["zip"],
                "city": sample_row["city"],
                "state": sample_row["state"],
                "latitude": sample_row["latitude"],
                "longitude": sample_row["longitude"],
                "status": random.choice(["active", "inactive"]),
            }
        )

    base_path = Path(__file__).resolve().parent.parent
    file_name = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    file_path = str(base_path) + '/output/facilities_' + file_name + '.csv'
    df = pd.DataFrame(facilities)
    df.to_csv(file_path, index = False)
    return df
