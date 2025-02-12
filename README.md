# Project Name: Global Hotel Mapping

## Overview
The Global Hotel Mapping project is designed to map and manage hotel data from various suppliers. This project is written in Python.

## Features
- **Hotel ID Management**: Handles various lists of hotel IDs from multiple suppliers.
- **Data Processing**: Processes and manages hotel data efficiently.
  
## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RoknuzzamanRokon/global_hotel_mapping.git
    cd global_hotel_mapping
    ```

2. Install dependencies:
    ```sh
    pipenv install
    ```
3. Active Virtual Environment
   ```sh
    pipenv shell
    ```

## Setup Environment
### Required credentials to add in the .env file in project directory:

#### 2.1 Database connection credentials
- Database URL set it as a 'DB_HOST' this name string
- Database usernmae set it as a 'DB_NAME' this name string
- Username set it as a 'DB_USER' this name string
- Password set it as a 'DB_PASSWORD' this name string


#### 2.2 Giata API connection credentials
- API key or token set it as a 'GIATA_API_KEY' this name string
- Endpoint URL set it as a 'GIATA_API_URL' this name string

## Usage

1. Ensure all necessary input files are in place.
2. Run the main script:
    ```sh
    python main.py
    ```
    This is used for mapping first-time data vervotech mapping to global mapping table.


### Go to 'find_id' repository and genarate id details for follow database, Here if try to 'grnconnect' hotel. Follow below stap:
   ```sh
     vim get_supplier_hotel_id_list.py  
   ```
   edit 2nd last line this section 'supplier = "grnconnet"'. Here give example for grnconnect supplier.

### Then go to 'for_supplier' repository and run code as you needed for uploaded data.
    
    ```sh
    python goglobal_data_insert_into_GHM.py
    ```

    

