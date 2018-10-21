'''Area of triangle is equals to height*base/2'''

def area(h,b):
    return (h*b)/2

print(area(10,5))


class counter(int):
    counter=10
    def increment(self):

        for i in range(1,10):
            print("incrementing...... {}".format(i))

    def reset(self):
        counter=0
        counter.increment()

obj=counter

print(obj.increment(1))

