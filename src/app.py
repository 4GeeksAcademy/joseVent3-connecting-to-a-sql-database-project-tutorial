import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

engine.execute("""

CREATE TABLE IF NOT EXISTS publishers(
    publisher_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(publisher_id)
);

CREATE TABLE IF NOT EXISTS authors(
    author_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(50) NULL,
    last_name VARCHAR(100) NULL,
    PRIMARY KEY(author_id)
);

CREATE TABLE IF NOT EXISTS books(
    book_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    total_pages INT NULL,
    rating DECIMAL(4, 2) NULL,
    isbn VARCHAR(13) NULL,
    published_date DATE,
    publisher_id INT NULL,
    PRIMARY KEY(book_id),
    CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
);

CREATE TABLE IF NOT EXISTS book_authors (
    book_id INT NOT NULL,
    author_id INT NOT NULL,
    PRIMARY KEY(book_id, author_id),
    CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

""")
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

engine.execute("INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media');"
                "INSERT INTO publishers(publisher_id,name) values (2,'monk knows');"
                "INSERT INTO publishers(publisher_id,name) values (3,'Silver Peter');"
                "INSERT INTO publishers(publisher_id,name) values (4,'Mc Daniels');"
                "INSERT INTO publishers(publisher_id,name) values (5,'Ropero hans');"
                "INSERT INTO publishers(publisher_id,name) values (6,'Albert&Sweigart');"
                "INSERT INTO publishers(publisher_id,name) values (7,'Alfred A. Knopf');"
)

engine.execute( "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (1,'Merritt',null,'Eric');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (2,'Linda',null,'Mui');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (3,'Alecos',null,'Papadatos');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (4,'Anthony','Molinaro');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (5,'David',null,'Cronin');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (6,'Richard',null,'Blum');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (7,'Yuval','Noah','Harari');"
                "INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (8,'Paul',null,'Albitz');"
)


# 4) Use pandas to print one of the tables as dataframes using read_sql function

result_dataFrame = pd.read_sql("Select * from publishers;", engine)
print(result_dataFrame)