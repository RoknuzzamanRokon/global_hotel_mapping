from sqlalchemy import MetaData, Table, create_engine, update, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


FILE_PATH = os.getenv('FIND_ID_FILE_PATH')


db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
engine = create_engine(connection_string)

metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

vervotech_mapping = Table("vervotech_mapping", metadata, autoload_with=engine)

def get_unique_id_list():
    query = select(vervotech_mapping.c.VervotechId).distinct()
    result = session.execute(query).scalars().all()
    return result

def save_id_list_to_file(file_name="id_list_file.txt"):
    unique_ids = get_unique_id_list()
    
    file_path = os.path.join(FILE_PATH, file_name)
    with open(file_path, "w") as file:

        for unica_id in unique_ids:
            file.write(f"{unica_id}\n")
    
    print(f"Unique IDs saved to {file_name}")
    print(f"Total unique IDs: {len(unique_ids)}")

save_id_list_to_file()