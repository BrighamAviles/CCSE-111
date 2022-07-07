import math
from datetime import datetime

#creating text file
outfile = open('volums.txt', 'w')

# to be able to add dates   
now = datetime.now()
    
width = int(input("Enter the width of the tire in mm: "))
aspect = int(input("Enter the aspect ratio of the tire:"))
diameter = int(input("Enter the diameter of the wheel in inches:"))

volum = math.pi * (width ** 2 * aspect) * (width * aspect + 2540 * diameter) / 10000000000  
    
outfile.write (str(now) + "\n")
outfile.write (str(width) + "\n")
outfile.write (str(aspect) + "\n")
outfile.write (str(diameter) + "\n" )
outfile.write (str(volum) + "\n")
    
outfile.close()