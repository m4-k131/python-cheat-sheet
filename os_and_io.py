import sys 
import csv 


output_path = ""
out_rows = [{}]

with (open(output_path, "w", newline="", encoding="utf-8") if output_path else sys.stdout) as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(csv_file)
    for row in out_rows:
        writer.writerow([v for v in row.values()])
