with open ('source1.txt', 'r') as f:  # Open lorem.txt for reading text
    contents = f.read()              # Read the entire file to a string
contents = contents.split('\n\n')
print(contents[0])                           # Print the string
