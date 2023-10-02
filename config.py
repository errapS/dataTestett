import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'ENGINE': 'psycopg2',
    'HOST': os.getenv("DB_HOST"),
    'USER': os.getenv("DB_USER"),
    'PASSWORD': os.getenv("DB_PWD"),
    'NAME': os.getenv("DB_NAME"),
    'PORT': os.getenv("DB_PORT")
}