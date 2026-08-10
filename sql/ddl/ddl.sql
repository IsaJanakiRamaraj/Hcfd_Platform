--catalog
create catalog if not exists healthcare;

--bronze schema
create schema if not exists healthcare.bronze;

--silver schema
create schema if not exists healthcare.silver;

--gold schema 
create schema if not exists healthcare.gold;

--audit schema
create schema if not exists healthcare.audit;

--metadata schema 
create schema if not exists healthcare.metadata;

--fraud schema
create schema if not exists healthcare.fraud;

--Stream schema
--create schema if not exists healthcare.stream;

create table if not exists healthcare.bronze.claims(
    claim_id long,
    patient_id long,
    provider_id long,
    facility_id string,
    encounter_id long,
    claim_date date,
    service_date date,
    diagnosis_code long,
    procedure_code string,
    units int,
    claim_amount float,
    claim_status string
);


