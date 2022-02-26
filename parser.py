with open ('source1.txt', 'r') as f:  # Open lorem.txt for reading text
    contents = f.read()              # Read the entire file to a string
contents = contents.split('\n\n')
print(len(contents))
content1 = contents[0].split('\n')
print(content1)
import csv

header = ['title', 'authors', 'year','venue','index','references','abstract']
data = ['Afghanistan', 652090, 'AF', 'AFG']


with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)