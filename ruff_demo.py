import sys
import os

def calculate_area( radius ):
    unused_var=   100

    if radius == None:
        return 0
    
    print(f"Calculating area...")
    
    pi=3.14159
    result =  pi*radius**2; print( 'Debug: calculated result' )
    
    return result

def main():
    r=5
    area=calculate_area( r )
    print( "The area is: "+str(area) )

if __name__ == '__main__':
    main()
