import pandas
import json

datacsv = pandas.read_csv("new.csv")
print(datacsv)
datajson = pandas.DataFrame(datacsv).to_json(orient="records")
print(datajson)
datalist = json.loads(datajson)
print(datalist)