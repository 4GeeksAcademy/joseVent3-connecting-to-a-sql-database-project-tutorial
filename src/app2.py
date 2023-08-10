import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()


engine.execute( "INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media');"
                "INSERT INTO publishers(publisher_id,name) values (2,'monk knows');"
                "INSERT INTO publishers(publisher_id,name) values (3,'Silver Peter');"
                "INSERT INTO publishers(publisher_id,name) values (4,'Mc Daniels');"
                "INSERT INTO publishers(publisher_id,name) values (5,'Ropero hans');"
                "INSERT INTO publishers(publisher_id,name) values (6,'Albert&Sweigart');"
                "INSERT INTO publishers(publisher_id,name) values (7,'Alfred A. Knopf');"
)

engine.execute("INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (1,'Lean Software Development: An Agile Toolkit',240,4.17,'9780320000000','2003-05-18',5);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (2,'Facing the Intelligence Explosion',91,3.87,null,'2013-02-01',7);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (3,'Scala in Action',419,3.74,'9781940000000','2013-04-10',1);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (4,'Patterns of Software: Tales from the Software Community',256,3.84,'9780200000000','1996-08-15',1);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (5,'Anatomy Of LISP',446,4.43,'9780070000000','1978-01-01',3);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (6,'Computing machinery and intelligence',24,4.17,null,'2009-03-22',4);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (7,'XML: Visual QuickStart Guide',269,3.66,'9780320000000','2009-01-01',5);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (8,'SQL Cookbook',595,3.95,'9780600000000','2005-12-01',7);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (9,'The Apollo Guidance Computer: Architecture And Operation (Springer Praxis Books / Space Exploration)',439,4.29,'9781440000000','2010-07-01',6);"
               "INSERT INTO books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) VALUES (10,'Minds and Computers: An Introduction to the Philosophy of Artificial Intelligence',222,3.54,'9780750000000','2007-02-13',7);"
)

engine.execute("INSERT INTO book_authors (book_id, author_id) values (8,4);"
               "INSERT INTO book_authors (book_id, author_id) values (8,4);"
               "INSERT INTO book_authors (book_id, author_id) values (8,4);"
               "INSERT INTO book_authors (book_id, author_id) values (8,4);"
)