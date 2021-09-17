#!/usr/bin/python3
import sys

def main():
    next_biggest_number(int(sys.argv[1]))


def next_biggest_number(num):
  
    digits = [int(x) for x in str(num)]
    for i in range(len(digits) - 1, 0, -1):
    	if digits[i] > digits[i - 1]:
    		digits2 = digits[i - 1:]
    		remainder = digits[:i - 1]
    		trigger = int(digits[i - 1])
    		digits2.sort()
    		greater = [i for i in digits2 if i > trigger]
    		rightone = greater[0]
    		digits2.remove(rightone)
    		remainder.append(rightone)
    		almostoutput = remainder + digits2
    		strings = [str(integer) for integer in almostoutput]
    		strings2 = "".join(strings)
    		output = int(strings2)


    		return output
    	

    return -1

if __name__ == "__main__":
    main()