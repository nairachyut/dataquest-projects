## 3. Condensing the Class Size Data Set ##

class_size = data["class_size"]

class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]

print(class_size.head(5))

## 5. Computing Average Class Sizes ##

import numpy as np
import pandas as pd

class_size = class_size.groupby("DBN").agg(np.mean)

class_size.reset_index(inplace = True)

data["class_size"] = class_size

print(data["class_size"].head(5))

## 7. Condensing the Demographics Data Set ##

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]

print(data["demographics"].head(5))

## 9. Condensing the Graduation Data Set ##

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]

data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]

print(data["graduation"].head(5))

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for t in cols:
    data["ap_2010"][t] = pd.to_numeric(data["ap_2010"][t], errors = "coerce")
    
print(data["ap_2010"].dtypes)

## 12. Performing the Left Joins ##

combined = data["sat_results"]

combined = combined.merge(data["ap_2010"], how = "left", on = "DBN")

combined = combined.merge(data["graduation"], how = "left", on = "DBN")

print(combined.head(5))

print(combined.shape[0])

## 13. Performing the Inner Joins ##

files = ["class_size", "demographics", "survey", "hs_directory"]

for df in files:
    combined = combined.merge(data[df], how = "inner", on = "DBN")

print(combined.head(5))

print(combined.shape)

## 15. Filling in Missing Values ##

combined = combined.fillna(combined.mean())

combined = combined.fillna(0)

print(combined.head(5))

## 16. Adding a School District Column for Mapping ##

def let(word):
    return word[0:2]

combined["school_dist"] = combined["DBN"].apply(let)

print(combined["school_dist"].head(5))