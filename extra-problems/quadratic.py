import math
import argparse


def quadratic(a, b, c):
    # this function is for getting rid of leading .0
    formatNumber = lambda n: n if n%1 else int(n)

    D = (b**2)-4*a*c # determinant to check for complex numbers situation
    
    m = (-1*(b/a))/2
    m = formatNumber(m) # getting rid of the .0 leading zeros

    if (D) >= 0: # checking for complex numbers
        p = (m**2) - (c/a)
        d = float("{:.2f}".format(math.sqrt(p)))
        x1 = m + formatNumber(d)
        x2 = m - formatNumber(d)
        print("First root: {} \nSecond Root: {}".format(x1, x2))

    else: # what to do if it is a complex number
        p = (m**2) - (c/a)
        imz = str(float("{:.2f}".format(math.sqrt(p*-1)))) + "i"
        
        # because complex numbers roots are conjugate !

        x1 = str(m) + "+" + imz
        x2 = str(m) + "-" + imz
        print("First root: {} \nSecond Root: {}".format(x1, x2))


# construct a argparser

parser = argparse.ArgumentParser()

# adding arguments

parser.add_argument("-a", "--a",required=True, help="write the coefficient of x^2")
parser.add_argument("-b", "--b",required=False, default=0, help="write the coefficient of x")
parser.add_argument("-c", "--c",required=False, default=0, help="write the constant term")

# parsing the args
args = parser.parse_args()

# formula for quadratic equation

a = int(args.a)
b= int(args.b)
c = int(args.c)

quadratic(a,b,c)