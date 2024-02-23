import os
import sys
import sqlite3
import pandas

if __name__ == "__main__":
  # variable declarations
  input_file = "database.db"
  output_file = "database.csv"
  table_name = "logsmodel"
  if(len(sys.argv) == 1):
    print("The number of arguments is insufficient")
  elif(len(sys.argv) == 2):
    input_file = sys.argv[1]
  elif(len(sys.argv) == 3):
    input_file = sys.argv[1]
    output_file = sys.argv[2]
  elif(len(sys.argv) == 4):
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    table_name = sys.argv[3]
  else:
    print("Unable to determine position of arguments")
  connection = sqlite3.connect(input_file)
  query_string = f"SELECT * FROM {table_name};"
  dataframe = pandas.read_sql_query(query_string,connection)
  dataframe.to_csv(os.getcwd() + "\\" + output_file, sep='|')