# Define a function that does this:
# Given a list of strings, with each string having a student’s name and
# their grades, mutate the input list so the original string positions are
# replaced with their average grades. The function doesn’t need an explicit
# return statement.


def get_averages(lst):
    # your code here
    for i in range(len(lst[:])):
        temp_lst = lst[i].split(',')[1:]
        float_grades = [float(x) for x in temp_lst]
        avg = sum(float_grades)/len(temp_lst)
        lst[i] = avg

reports = ['Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98']
get_averages(reports)
print(reports)
# [74.0, 65.0, 98.0]
