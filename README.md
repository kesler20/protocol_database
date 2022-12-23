# Protocol Database

The excel database can be manipulated from the ``ExcelDatabase`` 

## Example

```python
from exceldatabase import ExcelDatabase

if __name__ == "__main__":
  db = ExcelDatabase()
  db.create_table("my_routine", ["Week Day", "Expenses"], [
                  ["Monday", 0.5], ["Tuesday",0.2]])
  print(db.get_table("my_routine"))
  db.preview_table("my_routine")
```
>output
```bash
  Week Day  Expenses
0   Monday       0.5
1  Tuesday       0.2
```

To inspect the file if the preview_table method does not run you can run the following command
```bash
start excel protocol_database\my_routine.xlsx
```
>output
<div style="width: 100%; display: flex; justify-content: center; align-items: center;">
  <img src="./img/my_routine.PNG" alt="" srcset="" style="width: 30%;">
</div>

the ``ExcelDatabase`` class is specified below 
Example of creating a table

## Design Overview

```mermaid
classDiagram
   ExcelDatabase <|-- object
   ExcelDatabase : - folder_name str
   ExcelDatabase : + folder_name() str
   ExcelDatabase : + database() DataFrame
   ExcelDatabase : + database_info() None
   ExcelDatabase : + _pp() None
   ExcelDatabase : + create_table() None
   ExcelDatabase : + get_table() DataFrame
   ExcelDatabase : + query_table() DataFrame
   ExcelDatabase : + get_table_slice() Any
   ExcelDatabase : + get_n_rows_from_tables_above() Any
   ExcelDatabase : + get_n_rows_from_tables_below() Any
   ExcelDatabase : + table_info() Any
   ExcelDatabase : + get_table_names() List[str]
   ExcelDatabase : + get_value_by_column_name() Any
   ExcelDatabase : + get_value_by_column_index() Any
   ExcelDatabase : + delete_table() Any
   ExcelDatabase : + append_row() None
   ExcelDatabase : + update_rows() None
   ExcelDatabase : + delete_rows() None
   ExcelDatabase : + put_column() None
   ExcelDatabase : + insert_column() None
   ExcelDatabase : + delete_columns() Any
```
## Schema
The database is organized in folders and excel files, where folders represent databases and excel files are tables

## Improvements
- [ ] create a way to index the different files (if i want to link two values from two different tables) some potential solutions
* use sub_folders within the folder (database) to group related tables (parents of a table)
* include a schema 
- [ ] Implement loc method
using the loc method the rows could be updated more effectively
import pandas as pd
```python
# Update rows 2 through 4 in column 'B' to be 0
df.loc[2:4, 'B'] = 0
# Update rows where the value in column 'A' is greater than 2
df.loc[df['A'] > 2, 'B'] = 0
# Update columns 'B' and 'C' for all rows
df.loc[:, ['B', 'C']] = 0
```
