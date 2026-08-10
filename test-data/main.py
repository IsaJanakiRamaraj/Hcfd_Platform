from generators.generate_facilities import gen_facilities
from generators.generate_zip_code import gen_zip_code
from generators.generate_taxonomy import gen_taxonomy
from generators.generate_providers import gen_provider
from generators.generate_patients import gen_patients
from generators.generate_diagonosis import gen_diagonosis
from generators.generate_procedure import gen_procedures
from generators.genarate_encounter import gen_encounter
from generators.generate_claim import gen_claim
import config

def main():
    zip_df = gen_zip_code(config.NUMBER_OF_ZIPS)
    fac_df = gen_facilities(config.NUMBER_OF_FACILITIES, zip_df)
    tax_df = gen_taxonomy(config.NUMBER_OF_DIAGNOSIS)
    prov_df = gen_provider(
        config.NUMBER_OF_PROVIDERS,
        fac_df["facility_id"].to_list(),
        tax_df["taxonomy_code"].to_list(),
    )
    pati_df = gen_patients(config.NUMBER_OF_PATIENTS, zip_df['zip'])
    diag_df = gen_diagonosis(config.NUMBER_OF_DIAGNOSIS, config.SPECIALTITY)
    proc_df = gen_procedures(config.NUMBER_OF_PROCEDURES, config.SPECIALTITY)
    enc_df = gen_encounter(config.NUMBER_OF_ENCOUNTERS, pati_df['patient_id'].to_list(), prov_df['provider_id'].to_list(), 
    fac_df['facility_id'].to_list(), 
    diag_df['diagnosis_code'].to_list())
    claim_df = gen_claim(config.CLAIMS_PER_DAY,
        pati_df['patient_id'].to_list(), prov_df['provider_id'].to_list(), 
    fac_df['facility_id'].to_list(),
    enc_df['encounter_id'].to_list(), 
    diag_df['diagnosis_code'].to_list(),
    proc_df['procedure_code'].to_list()
    )
    

if __name__ == '__main__':
    main()