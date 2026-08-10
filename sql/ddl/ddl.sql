--catalog
create catalog if not exists healthcare;

--bronze schema
create schema if not exists healthcare.bronze;

--silver schema
create schema if not exists healthcare.silver

--gold schema 
create schema if not exists healthcare.gold;

--audit schema
create schema if not exists healthcare.audit;

--metadata schema 
create schema if not exists healthcare.metadata;

--fraud schema
create schema if not exists healthcare.fraud;

--Stream schema
create schema if not exists healthcare.stream;




