"""Print Fibonacci series from 0 to input(numberOfSeries) with a for loop"""

def main():
    while(True):
        print("Please enter the number of fibonacci series :")
        numberOfSeries=int(input())
        print("******************")
        fibonacciSerieLoop(numberOfSeries)


def fibonacciSerieLoop(n):
    first = 0
    second = 1
    for i in range(1, n+1):
        print(first)
        third = first+second
        first = second
        second = third


if __name__ == '__main__':
    main()


# by Arman Azarnik
# armanazarnik@gmail.com