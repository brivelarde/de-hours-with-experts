#!/usr/bin/python3
import sys

def main():
    print(next_biggest_number(int(sys.argv[1])))


def next_biggest_number(num):
    notlist = [int(x) for x in str(num)]
    for n in range(len(notlist) - 1, 0, -1):
    	if (notlist[n] > notlist[n - 1]):
    		group_two = notlist[n - 1:]
    		remainder_one = notlist[:n - 1]
    		x = (notlist[n - 1])
    		group_two.sort()
    		y = -1
    		for num in group_two:
    			if (num > x ):
    				y = num
    				break
    		group_two.remove(y)
    		group_final = remainder_one + [y] + group_two
    		string1 = [str(integer) for integer in group_final]
    		string2 = "".join(string1)
    		integer_final = int(string2)

    		return (integer_final)
    return (-1)

    		
    		

    	


if __name__ == "__main__":
    main()



