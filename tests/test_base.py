
import unittest
from protocol_database.exceldatabase import ExcelDatabase
from protocol_database._base import folder_name, base_table_name, base_df_values, base_df_cols

print("Testing:" + ExcelDatabase.__doc__)


class Test_ExcelDatabase(unittest.TestCase):

    def setUp(self):
        self.test_client = ExcelDatabase()
        self.test_client.create_database(folder_name)
        self.test_client.create_table(
            base_table_name, base_df_cols, base_df_values)

    def tearDown(self):
        self.test_client.delete_database(folder_name)

if __name__ == "__main__":
    unittest.main()
