# __name__ is a python variable which indicates the function in which it is operating
import librarym.geoareasm as geoareas

def calcuate_area(base,height):
    return(1/2*base*height)

if __name__ == "__main__":
    print("I am in main function")
    print(calcuate_area(5,10))

print(geoareas.cal_sq_area(6))
