from faker import Faker
from datetime import datetime
import pandas as pd
from pathlib import Path

fake = Faker()
zip_codes = []
def gen_zip_code(n):
    for i in range(n):
        zip_codes.append(
            {
                'zip' : fake.postcode(),
                'city' : fake.city(),
                'state' : fake.state_abbr(),
                'latitude': fake.latitude(),
                'longitude': fake.longitude()
            }
        )
    base_path = Path(__file__).resolve().parent.parent
    file_name = str(datetime.now().strftime('%y-%M-%d_%H-%M-%S'))
    file_path = str(base_path) + '/output/zip_master_' + file_name  + '.csv'
    df = pd.DataFrame(zip_codes)
    df.to_csv(file_path, index= False)
    return df 