#!/usr/bin/python3
import sys

def main():
    next_biggest_number(int(sys.argv[1]))


def next_biggest_number(num):
    #TODO: Implement me!
    digits = [int(x) for x in str(num)]
    for i in range(len(digits) - 1, 0, -1):
    	if digits[i] > digits[i - 1]:
    		digits2 = digits[i - 1:]
    		remainder = digits[:i - 1]
    		trigger = digits[i-1]
    		digits2.sort()
    		final = digits2[-1]
    		digits2.remove(digits2[-1])
    		remainder.append(final)
    		output = remainder + digits2
    		return output

    		
    	

    return -1

if __name__ == "__main__":
    main()