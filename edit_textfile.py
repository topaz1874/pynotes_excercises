# Insert a string after a word in a specific line of a text file

"""

Input file
line 1: value1
line 2: value2
line 3: value3
line 4: value4
line 5: value5

Insert, for example, "NAME" in the line number 3 just after "line" so
the file would become:

Output file
line 1: value1
line 2: value2
line NAME 3: value3
line 4: value4
line 5: value5

"""

def insert_string(in_file, line, insertion):
    """ Return a list of lines after inserting a word in a specific line. """

    # your code here
    with open(in_file, 'r') as f:
        lines_lst = f.readlines()
        new_line = line -1
        str1 = lines_lst[new_line]
        lines_lst[new_line] = str1.replace(str(line), insertion, 1)
        return lines_lst

def write_to(outfile, from_infile):
    """ Write to a new file lines returned by the above function """

    # your code here
    with open(outfile, 'r') as f:
        data = insert_string(from_infile, 3, 'Name 3')
        f.write(data)






