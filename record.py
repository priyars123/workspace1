

import csv
import time
def read_csv_record():
     with open("C:\\Users\\priyanka\\Downloads\\Sample-Spreadsheet-10-rows.csv") as file:
         reader=csv.reader(file)
         for line in reader:
             print(line)

def read_lines():
    with open("C:\\Users\\priyanka\\Downloads\\Sample-Spreadsheet-10-rows.csv") as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)
            time.sleep(2)

def read_line_lines():
    with open("C:\\Users\\priyanka\\Downloads\\Sample-Spreadsheet-10-rows.csv") as file:
        reader = csv.reader(file)
        for line in reader:
            yield line

if __name__=='__main__':


   #read_csv_record()
   #read_lines()
   start=time.time()
   gen=read_line_lines()
   print(next(gen))
   print(next(gen))
   end=time.time()
   total_time=end-start
   print(total_time)





