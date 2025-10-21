import os
from conexion.oracle_queries import OracleQueries

def create_tables(query: str):
    list_of_commands = query.split(";")
    oracle = OracleQueries(can_write=True)
    oracle.connect()
    try:
        for command in list_of_commands:
            command = command.strip()
            if command:
                print("Executing:", command)
                try:
                    oracle.executeDDL(command)
                    print("Successfully executed")
                except Exception as e:
                    print("Error:", e)
    finally:
        oracle.close()


def generate_records(query: str, sep: str = ';'):
    list_of_commands = query.split(sep)
    oracle = OracleQueries(can_write=True)
    oracle.connect()
    try:
        for command in list_of_commands:
            command = command.strip()
            if command:
                print("Executing:", command)
                try:
                    oracle.write(command)
                    print("Successfully executed")
                except Exception as e:
                    print("Error:", e)
    finally:
        oracle.close()


def run():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQL_DIR = os.path.join(BASE_DIR, "../sql")

    
    create_tables_file = os.path.join(SQL_DIR, "create_tables_locacoes.sql")
    generate_records_file = os.path.join(SQL_DIR, "inserting_samples_records.sql")
    generate_related_file = os.path.join(SQL_DIR, "inserting_samples_related_records.sql")

   
    with open(create_tables_file, "r") as f:
        query_create = f.read()
    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!\n")

    
    with open(generate_records_file, "r") as f:
        query_generate_records = f.read()
    print("Generating records...")
    generate_records(query=query_generate_records)
    print("Records successfully generated!\n")

   
    with open(generate_related_file, "r") as f:
        query_generate_related_records = f.read()
    print("Generating related records...")
    generate_records(query=query_generate_related_records, sep='--')
    print("Related records successfully generated!\n")


if __name__ == "__main__":
    run()
