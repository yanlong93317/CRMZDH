import csv
def read_csv():
    with open(file="lgoin.csv") as f:
        data=csv.reader(f)
        set_list=[]
        for user in data:
            set_list.append(user)
        return set_list[1:]
# print(read_csv())
