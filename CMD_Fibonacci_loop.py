"""Python CMD program for printing Fibonacci series from 0 to input value(number_Of_Series) with a for loop.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
    """
    main function for interacting with the user
    """
    while(True):
    # while loop to keep the program running

        print("Please enter the number of Fibonacci series :")
        number_Of_Series = int(input())
        # casting the input string into integer

        print("Your Fibonacci serie :")
        result = Fibonacci_Serie_Generator_Loop(number_Of_Series)
        # storing Fibonacci serie from 0 to number_Of_Series in result variable 

        array_printer(result)
        print("**************************************************")
        

def Fibonacci_Serie_Generator_Loop(number):
    """
    function for generating the Fibonacci series with a for loop.
    @param number: the input for serie number.
    @type text: int
    @return: Fibonacci_Series
    @rtype: array of integers
    @examples: 
     >>> Fibonacci_Serie_Generator_Loop(0)
         []
     >>> Fibonacci_Serie_Generator_Loop(5)
         [0, 1, 1, 2, 3]
    """
    Fibonacci_Series = [None]*(number)
    # initializing an empty array with lenght of number

    first = 0
    second = 1
    for i in range(0, number):
        Fibonacci_Series[i] = first
        third = first+second
        first = second
        second = third

    return Fibonacci_Series


def array_printer(array):
    """
    function for printing each array element in a line.
    @param array: an array of elements.
    @type text: anything like integer, double and string.
    @examples: 
         array_1 = []
         array_2 = [1, 2, 3]
     >>> array_printer(array_1)
          
     >>> array_printer(array_2)
         1
         2
         3
    """
    for element in array:
        print(element)


if __name__ == '__main__':
    main()
    # run the main function after executing this file