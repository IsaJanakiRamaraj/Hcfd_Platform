from faker import Faker
from datetime import datetime
import random
import pandas as pd
from pathlib import Path

fake = Faker()
providers = []
def gen_provider(n, facility_id, taxonomy_code):
    for i in range(n):
        providers.append(
            {
                'provider_id': f'{i+1:07}',
                'npi': f'{fake.numerify("############")}',
                'provider_name': fake.name(),
                'facility_id': f'{random.choice(facility_id)}',
                'taxonomy_code': f'{random.choice(taxonomy_code)}',
                'status': random.choice(['active', 'inactive']),
                'effective_from': fake.date_between(start_date='-2y', end_date='today'),
                'effective_to': fake.date_between(start_date='today', end_date='+2y')
            },
            
        )
    base_path = Path(__file__).resolve().parent.parent
    file_name = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    file_path = str(base_path) + '/output/providers_' + file_name + '.csv'
    df = pd.DataFrame(providers)
    df.to_csv(file_path, index=False)
    return df