# reporter.py
import pandas
import os
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
print("READING GRADEBOOK CSV FILE...")
# if CSV file in same dir as this Python script:
#USE OS JOIN FOR FULL POINTS ON PROJECTS
csv_filepath = os.path.join(os.path.dirname(__file__), "data", "gradebook.csv") 
grades = pandas.read_csv(csv_filepath)
print("GRADES:", type(grades))
#print(dir(grades))
print(grades.tail())
# grades["student_id"]
# grades["final_grade"]

# FIND AVG GRADE
# stats["games"].max()
grades_col = grades["final_grade"]
print("GRADES COLUMN", type(grades_col))
avg_grade = grades_col.mean()
print("AVG GRADE:", avg_grade)