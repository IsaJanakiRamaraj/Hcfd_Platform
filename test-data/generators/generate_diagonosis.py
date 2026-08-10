from pathlib import Path
import pandas as pd
import random
from datetime import datetime
from faker import Faker

fake = Faker()
diagonosis = []

def gen_diagonosis(n, category):
    for i in range(n):
        diagonosis.append(
            {
                'diagnosis_code': fake.random_int(
                    min=10000, max=99999),
                'description': "",
                'category': random.choice(category), 
                'severity': random.choice(
                    ["minor", "moderate", "major"]),
            }
        )
    df = pd.DataFrame(diagonosis)
    base_path = Path(__file__).resolve().parent.parent
    file_name = 'diagnosis_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
    file_path = str(base_path) + '/output/' + file_name
    df.to_csv(file_path, index= False)
    return df