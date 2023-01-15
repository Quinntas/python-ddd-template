import mysql.connector
from decouple import config
from fastapi import HTTPException


class DatabaseController(object):
    def __init__(self, user: str, password: str, host: str = 'localhost'):
        self.user = user
        self.password = password
        self.host = host
        self.connection = self.connect()
        self.cursor = self.connection.cursor(buffered=True)

    @staticmethod
    def get_keys(data: dict) -> str:
        return ', '.join(key for key in data.keys())

    @staticmethod
    def wrap(value: any) -> str:
        if type(value) == str:
            return f"'{value}'"
        return f"{value}"

    def get_values(self, data: dict) -> str:
        return ', '.join(self.wrap(value) for value in data.values())

    def get_params(self, data: dict, join_str: str = ' AND ') -> str:
        return join_str.join(f"{key} = {self.wrap(data[key])}" for key in data)

    @staticmethod
    def get_columns(data: list) -> str:
        return ', '.join(key for key in data)

    def connect(self) -> mysql.connector.connection:
        try:
            return mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        except mysql.connector.errors.ProgrammingError as e:
            raise HTTPException(status_code=400, detail=e)

    def execute(self, command: str):
        try:
            self.cursor.execute(command + ';')
            self.connection.commit()
        except mysql.connector.errors.OperationalError as e:
            raise HTTPException(status_code=400, detail=e.__str__())
        except mysql.connector.errors.IntegrityError as e:
            raise HTTPException(status_code=400, detail=e.__str__())
        except mysql.connector.errors.ProgrammingError as e:
            raise HTTPException(status_code=400, detail=e.__str__())
        except mysql.connector.errors.InternalError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

    async def wipe_table(self, table_name: str, database_name: str) -> str:
        """
        Wipes all values from table
        """
        self.execute(f"DELETE FROM {database_name}.{table_name}")
        return f"{table_name} was wiped successfully."

    async def drop_table(self, table_name: str, database_name: str) -> str:
        """
        Drop a table
        """
        self.execute(f"DROP TABLE {database_name}.{table_name}")
        return f"{table_name} was dropped successfully."

    async def create_table(self, table_name: str, database_name: str, attributes: str):
        """
        REMINDER: INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        REMINDER: STRING TYPE = VARCHAR(255)
        """
        return self.execute(f"CREATE TABLE {database_name}.{table_name} {attributes}")

    async def insert_value(self, table_name: str, database_name: str, data: dict):
        """ EX: INSERT INTO test_table VALUES ('Maria', 'Joaquima', 300000) """
        return self.execute(
            f"INSERT INTO {database_name}.{table_name} ({self.get_keys(data)}) VALUES ({self.get_values(data)})")

    async def select_all_from_table(self, table_name: str, database_name: str) -> list | None:
        """
        EX: SELECT * from test_table
        """
        self.execute(f"SELECT * FROM {database_name}.{table_name}")
        return self.cursor.fetchall()

    async def select_from_params(self, table_name: str, database_name: str, params: dict, fetch: str = 'ALL',
                                 columns: list = None) -> list | None:
        """
        EX: SELECT * from test_table WHERE pay = 10000 AND first_name = Caio

        fetch: ALL | ONE
        """
        if not columns or len(columns) == 0:
            columns = ['*']
        self.execute(
            f"SELECT {self.get_columns(columns)} FROM {database_name}.{table_name} WHERE {self.get_params(params)}")
        if fetch == 'ONE':
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    async def remove_row(self, table_name: str, database_name: str, params: dict):
        """
        EX: DELETE from test_table WHERE pay = 10000 AND first_name = Caio
        """
        return self.execute(f"DELETE FROM {database_name}.{table_name} WHERE {self.get_params(params)}")

    async def update_value(self, table_name: str, database_name: str, values: dict, params: dict):
        """
        EX: UPDATE test_table SET pay = 10000 WHERE first_name = Caio
        """
        return self.execute(
            f"UPDATE {database_name}.{table_name} SET {self.get_params(values, ', ')} WHERE {self.get_params(params)}")

    async def create_table_from_dict(self, table_name: str, database_name: str, data: dict) -> str:
        if "SCHEMA" not in data:
            return f"No SCHEMA found"
        attributes = ', '.join(f"{key} {data['SCHEMA'][key]}" for key in data['SCHEMA'].keys())
        if 'FOREIGN_KEYS' in data:
            attributes += (f", FOREIGN KEY ({f_key}) REFERENCES {data['FOREIGN_KEYS'][f_key]['REFERENCES']}" for f_key
                           in data['FOREIGN_KEYS'])
        await self.create_table(table_name, database_name, '(' + attributes + ')')
        return f"{table_name} was created successfully."

    async def create_database(self, database_name: str) -> str:
        self.execute(f"CREATE DATABASE {database_name}")
        return f"{database_name} was created successfully."

    async def drop_database(self, database_name: str) -> str:
        self.execute(f"DROP DATABASE {database_name}")
        return f"{database_name} was dropped successfully."

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()


database = DatabaseController(
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST')
)
