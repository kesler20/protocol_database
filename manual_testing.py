import pandas as pd
from protocol_database.exceldatabase import ExcelDatabase
from protocol_database._base import folder_name
# test_client = ExcelDatabase()
# test_client.create_database(folder_name)
# test_client.create_table(
#     "test this table", ["test this column", "another column"], [[0, 1], [2, 2]])
# test_client.append_row([4, 12], "test this table")
# print(test_client.get_table("test this table"))

df1 = pd.DataFrame([0,1,1])
df2 = pd.DataFrame([0,1,1])
print(df1 == df2)