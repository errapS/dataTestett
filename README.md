# Data Fetching from API and Storing in PostgreSQL with Docker

This README provides detailed instructions for setting up a PostgreSQL database server using Docker, creating the necessary table, and configuring your Python environment to fetch data from an API and store it in the database. The project uses the `psycopg2`, `peewee`, and `schedule` libraries for Python and leverages Docker for containerized PostgreSQL.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setting Up PostgreSQL with Docker](#setting-up-postgresql-with-docker)
- [Creating the Database Table](#creating-the-database-table)
- [Python Environment Setup](#python-environment-setup)
- [SQL Trigger Function](#sql-trigger-function)

---

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package manager)

## Setting Up PostgreSQL with Docker

1. **Install Docker**: Make sure Docker is installed and running on your system.

2. **Login to Docker**: If you're not already logged in to Docker, open your terminal and run:
   
   ```bash
   docker login
   ```

3. **Start a PostgreSQL Docker Container**: Run the following command to start a Docker container with PostgreSQL:

   ```bash
   docker run --name datatestett-postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=datatestett postgres
   ```

4. **Verify Container Status**: Check the status of the container to ensure it's running:

   ```bash
   docker ps
   ```

## Creating the Database Table

1. **Connect to the PostgreSQL Database**: You can use a PostgreSQL client like `psql` or any GUI tool to connect to the database using the following details:

   - Host: `localhost`
   - Port: `5432`
   - Username: `postgres`
   - Password: `datatestett`

2. **Create the 'people' Table**: Execute the following SQL command to create the 'people' table:

   ```sql
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
   ```

## Python Environment Setup

1. **Create a Virtual Environment**: To isolate project dependencies, create a Python virtual environment. Run the following commands in your project directory:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Python Libraries**:
   Install the necessary Python libraries using `pip`:

   ```bash
   pip install dotenv peewee psycopg2 schedule
   ```

## SQL Trigger Function

The project includes an SQL trigger function that archives data from the 'people' table before inserting new records.

```sql
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
    
    EXECUTE 'INSERT INTO ' || quote_ident(archive_table_name) || ' SELECT * FROM people';
   
    EXECUTE 'DELETE FROM people';
   
    EXECUTE 'INSERT INTO people SELECT * FROM ' || quote_ident(archive_table_name);
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to execute the function before insert
CREATE TRIGGER archive_people_trigger BEFORE INSERT ON public.people
FOR EACH ROW
WHEN (
    (NEW.name IS NULL)
    AND (NEW.height IS NULL)
    AND (NEW.mass IS NULL)
)
EXECUTE FUNCTION archiveonupdate();
```

---

You have now successfully set up a PostgreSQL database with Docker, created the necessary 'people' table, and configured your Python environment for data fetching and storage. You can integrate your Python script to fetch data from an API and insert it into the 'people' table as needed.
