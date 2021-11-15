import random
ids = [i for i in range(1,11,1)]
names = ['Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley', 'Jennifer', 'Joshua', 'Amanda', 'Daniel', 'David', 'James', 'Robert', 'John', 'Joseph', 'Andrew', 'Ryan', 'Brandon', 'Jason', 'Justin', 'Sarah']
ages = [i for i in range(20,100,1)]
genders = ["M","F"]*1000
random.shuffle(ages)
random.shuffle(names)
random.shuffle(genders)
d = {"people":[
    # {
    #     #id
    #     #name
    #     #age
    #     #gender
    # }
]}

for i in range(len(ids)):
    temp = {}
    temp["id"]=ids[i]
    temp["name"]= names[i]
    temp["age"] = ages[i]
    temp["gender"] = genders[0]
    d["people"].append(temp)

import json
json.dump(
    d,
    open("people.json", "w"))
