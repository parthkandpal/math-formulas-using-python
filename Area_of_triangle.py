'''Area of triangle is equals to height*base/2'''

def area(h,b):
    return (h*b)/2

height=int(input("Please enter height"))
base=int(input("Please enter base"))

area=area(height,base)

print("Areas of triangle = ", int(area))
