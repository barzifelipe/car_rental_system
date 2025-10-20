import json
import os
import oracledb
from pandas import DataFrame

class OracleQueries:

    def __init__(self, can_write: bool = False):
        self.can_write = can_write
        self.host = "localhost"
        self.port = 1521
        self.service_name = 'XEPDB1'

        # Caminho seguro para o arquivo de autenticação, relativo a este script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        auth_file = os.path.join(base_dir, "passphrase", "authentication.oracle")

        if not os.path.exists(auth_file):
            raise FileNotFoundError(f"Authentication file not found: {auth_file}")

        with open(auth_file, "r") as f:
            content = f.read().strip()
            self.user, self.passwd = content.split(',')

        self.conn = None
        self.cur = None

    def __del__(self):
        if hasattr(self, "cur") and self.cur:
            self.close()

    def connectionString(self) -> str:
        """
        String de conexão no modo Thin do oracledb.
        """
        return f"{self.host}:{self.port}/{self.service_name}"

    def connect(self):
        """
        Conecta ao banco Oracle usando oracledb Thin.
        """
        self.conn = oracledb.connect(
            user=self.user,
            password=self.passwd,
            dsn=self.connectionString()
        )
        self.cur = self.conn.cursor()
        return self.cur

    def sqlToDataFrame(self, query: str) -> DataFrame:
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return DataFrame(rows, columns=[col[0].lower() for col in self.cur.description])

    def sqlToMatrix(self, query: str) -> tuple:
        self.cur.execute(query)
        rows = self.cur.fetchall()
        matrix = [list(row) for row in rows]
        columns = [col[0].lower() for col in self.cur.description]
        return matrix, columns

    def sqlToJson(self, query: str) -> str:
        self.cur.execute(query)
        columns = [col[0].lower() for col in self.cur.description]
        rows = [dict(zip(columns, row)) for row in self.cur.fetchall()]
        return json.dumps(rows, default=str)

    def write(self, query: str):
        if not self.can_write:
            raise Exception("Can't write using this connection")
        self.cur.execute(query)
        self.conn.commit()

    def executeDDL(self, query: str):
        self.cur.execute(query)

    def close(self):
        if hasattr(self, "cur") and self.cur:
            self.cur.close()
            self.cur = None
        if hasattr(self, "conn") and self.conn:
            self.conn.close()
            self.conn = None
