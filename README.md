# dataTestett

install docker and log in 

docker run --name datatestett-postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=datatestett postgres
docker ps to check the status od the container

create table in databasem in this case "people"

CREATE TABLE people (
   person_id serial primary key,
   name VARCHAR(200),
   height INT,
   mass INT,
   hair_color VARCHAR(20),
   skin_color VARCHAR(20),
   eye_color VARCHAR(20),
   birth_year VARCHAR(20),
   gender VARCHAR(10),
   created_on TIMESTAMP default now() NOT NULL
);

python -m venv venv
to activate venv run venv\Scripts\activate

pip install dotenv
pip install peewee
pip install psycopg2
pip install schedule


SQL trigger function

CREATE OR REPLACE FUNCTION public.archiveonupdate()
RETURNS TRIGGER AS $$
DECLARE
    archive_table_name TEXT;
    column_names TEXT[];
    column_list TEXT;
    placeholders TEXT;
BEGIN
    archive_table_name := 'archivedPeople_' || to_char(NOW(), 'YYYY_MM_DD_HH24_MI_SS');
    
    EXECUTE 'CREATE TABLE IF NOT EXISTS ' || quote_ident(archive_table_name) || ' (LIKE people INCLUDING ALL)';
    
   	EXECUTE 'INSERT INTO' || quote_ident(archive_table_name) || 'SELECT * FROM people';
   
    EXECUTE 'DELETE FROM people';
   
   	EXECUTE 'INSERT INTO people SELECT * FROM' || quote_ident(archive_table_name);
    
	    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


create trigger archive_people_trigger before
insert
    on
    public.people for each row
    when (((new.name is null)
        and (new.height is null)
            and (new.mass is null))) execute function archiveonupdate()




