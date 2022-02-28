import re
newline=''
with open("source1.txt", 'r') as f:
    for line in f:
        if line.strip().startswith("#*"):
            se=re.search("#\*(.*)\\n",line).group(1)
            newline+='\n'+se
        elif line.strip().startswith("#@"):
            se=re.search("#\@(.*)\\n",line).group(1)
            newline+=','+se
        elif line.strip().startswith("#t"):
            se=re.search("#t(.*)\\n",line).group(1)
            newline+=','+se
        elif line.strip().startswith("#c"):
            se=re.search("#c(.*)\\n",line).group(1)
            newline+=','+se
        elif line.strip().startswith("#index"):
            se=re.search("#index(.*)\\n",line).group(1)
            newline+=','+se
        elif line.strip().startswith("#!"):
            se=re.search("#\!(.*)\\n",line).group(1)
            newline+=','+se
            break

with open("formated.txt","w") as f:
    f.write(newline)

# from email import header
# from os import sep
# import pandas as pd

# read_file=pd.read_csv("/home/gnaneswar/Desktop/formated.txt", sep=":",header=None)
# read_file.columns=['title', 'authors', 'year','index','references','abstract']
# read_file.to_csv("/home/gnaneswar/Desktop/formated.csv",index=None)


# import re
# import source.txt
# se=re.search("#*(.*)\\n","source.txt").group(1)
# print(se)


# with open ('source.txt', 'r') as f:  # Open lorem.txt for reading text
#     contents = f.read()              # Read the entire file to a string
# contents = contents.split('\n\n')
# print(len(contents))
# content1 = contents[0].split('\n')
# print(content1)
# import csv

# header = ['title', 'authors', 'year','venue','index','references','abstract']
# data = ['Afghanistan', 652090, 'AF', 'AFG']


# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)

