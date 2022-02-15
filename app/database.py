from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALECHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(SQLALECHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# while True:
#     try:
#         conn = psycopg2.connect(host='127.0.0.1', database='fastapi', user='postgres', password='log22gan',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection was Successful")
#         break
#     except Exception as error:
#         print("Connecting to Database failed")
#         print("Error: ", error)
#         time.sleep(5)