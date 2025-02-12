from sqlalchemy import MetaData, Table, create_engine, update
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
# connection_string = "mysql+pymysql://root:@localhost/innova_db_v1.25"

engine = create_engine(connection_string)

metadata = MetaData()  
Session = sessionmaker(bind=engine)
session = Session()

vervotech_mapping = Table("vervotech_mapping_2", metadata, autoload_with=engine)
global_hotel_mapping = Table("global_hotel_mapping", metadata, autoload_with=engine)



def get_a_column_info_follow_a_id(unica_id):
    query = (
        vervotech_mapping
        .select()
        .with_only_columns(vervotech_mapping.c.ProviderHotelId, vervotech_mapping.c.ProviderFamily) 
        .where(vervotech_mapping.c.UnicaId == unica_id)
    )
    result = session.execute(query).mappings().all()
    return result
