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




