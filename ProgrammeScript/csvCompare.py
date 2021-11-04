import csv
delimiter = ','
result1 = {}
result2 = {}
with open("Test1.csv", 'r') as data_file:
    data = csv.reader(data_file, delimiter=delimiter)
    headers = next(data)[1:] # month names starting from 2nd column in csv
    for row in data:
        temp_dict = {}
        name = row[0]
        values = []
        # converting each value from string to int / float
        # (as suggested by OP's example)
        for x in row[1:]:
            try:
                values.append(int(x))
            except ValueError:
                try:
                    values.append(float(x))
                except ValueError:
                    print("Skipping value '{}' that cannot be converted " +
                          "to a number - see following row: {}"
                          .format(x, delimiter.join(row)))
                    values.append(0)
        for i in range(len(values)):
            if values[i]: # exclude 0 values
                temp_dict[headers[i]] = values[i]
        result1[name] = temp_dict    
print(result1)

with open("Test2.csv", 'r') as data_file:
    data = csv.reader(data_file, delimiter=delimiter)
    headers = next(data)[1:] # month names starting from 2nd column in csv
    for row in data:
        temp_dict = {}
        name = row[0]
        values = []
        # converting each value from string to int / float
        # (as suggested by OP's example)
        for x in row[1:]:
            try:
                values.append(int(x))
            except ValueError:
                try:
                    values.append(float(x))
                except ValueError:
                    print("Skipping value '{}' that cannot be converted " +
                          "to a number - see following row: {}"
                          .format(x, delimiter.join(row)))
                    values.append(0)
        for i in range(len(values)):
            if values[i]: # exclude 0 values
                temp_dict[headers[i]] = values[i]
        result2[name] = temp_dict    
print(result2)

for Name1, info1 in result1.items():
    for Name2, info2 in result2.items():
        if(Name1==Name2):
                        print("key match found")
                        for key in info1:
                                    for key in info2:
                                        if(info1[key]==info2[key]):
                                            print(info1[key],"is matching with",info2[key])
                                        else:
                                            print(info1[key],"is not matching with",info2[key])


        else:
            print("key is not matching")



