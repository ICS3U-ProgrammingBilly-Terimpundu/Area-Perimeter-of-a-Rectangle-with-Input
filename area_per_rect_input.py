
import math


def main():
    # input
    print("Today we will calculate the area and")
    print("perimeter of a rectangle")
    l = int(input("Enter the length: (cm)"))
    w = int(input("Enter the width: (cm)"))
    
    # process
    area = l * w
    perimeter = 2*(l + w)
    
# output
    print("")
    print ("Area = {} cm^2".format(area))
    print ("Perimeter = {} cm".format(perimeter))

 
if __name__ == "__main__":
    main()