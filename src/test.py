from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(can_write=True)
oracle.connect()
result = oracle.sqlToMatrix("select * from dual")
print(result)

print()

result = oracle.sqlToDataFrame("select * from dual")
print(result)

print()

result = oracle.sqlToJson("select * from dual")
print(result)

oracle.executeDDL("create table test_float (x numeric(5, 3))")
oracle.write("insert into test_float values(9.4)")
oracle.write("insert into test_float values(4.8)")
result = oracle.sqlToDataFrame("select * from test_float")
print(result)
oracle.executeDDL("drop table test_float")