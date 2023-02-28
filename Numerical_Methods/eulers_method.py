#! python
import math

# initial conditions, your step incriment,
# what point you wanna estimate, and whether or not you want to show each step
def eulers_method(xo, yo, h, evaluate, show):
    steps = math.ceil((evaluate - xo) / h)
    
    x = xo
    y = yo
    
    for n in range(0, steps+1):
        if(show):
            print(f"when n = {n}")
            print(f" x = {x},y = {y}")
        else:
            if n == steps:
                print(f"when n = {n}")
                print(f" x = {x},y = {y}")

        #nexty = lasty + step*f(lastx, lasty) INPUT FUNCTION
        try:
            y = y + (h*(2*x*(y**2)))
        except OverflowError as e:
            print(f"Your function may have a discontinuity before"
                  + f" x = {x}\n"
                  + f"or is approaching +/- infinity")
            raise e
            
        #nextx = lastx + step
        x = x + h
        


        
