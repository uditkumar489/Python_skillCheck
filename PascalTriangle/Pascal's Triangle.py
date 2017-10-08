"""
code by udtech
Pascal's Triangle (with a formatted output)
by Infant 2017

Pascal's Triangle is a triangular array of numbers in which those numbers at the ends of the rows are 1 and each of the others is the sum of the nearest two numbers in the row above. For more info check this out https://goo.gl/EMcPvv


For Example: A trinagle with an input of 3 would look like this

                    1
                   1 1
                  1 2 1

Note: It is recomended to use a maximum of 10 for an input in order for the output to look ordered in a mobile device and upto a maximum of 25 on a computer for the output to look pretty ;)
"""


# function to create a pascal's triangle of size num
def pascalGen(num, r=[]):
    for item in range(num):
        length = len(r)
        r = [1 if i == 0 or i == length else r[i - 1] + r[i] for i in range(length + 1)]
        yield r


# function that draws the triangle
def draw_triangle(num):
    pascal = list(pascalGen(num))
    max = len(' '.join(map(str, pascal[-1])))
    for p in pascal:
        print(' '.join(map(str, p)).center(max) + '\n')


# enter the size of the triangle
print("enter size of triangle : ")
draw_triangle(int(input()))

# feedback
j = (35 * '*')
k = "\nLet me know how you like the code\n"
l = "\n\t         And\n"
m = "\t        Leave\n"
n = "\t      An Upvote\n"
o = "\t   If You Like It ;)"
print(j, k, l, m, n, o)