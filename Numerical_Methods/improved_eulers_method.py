#! python
import math

# initial conditions, your step increment,
# what point you want to estimate, and whether you want to show each step (bool)
def improved_eulers(xo, yo, h, evaluate, show):
    steps = math.ceil((evaluate - xo) / h)
    
    x = xo
    y = yo

    for n in range(0, steps+1):
        if show == True:
            print(f"when n = {n}")
            print(f"x = {x}, y = {y}")
        else:
            if n == steps:
                print(f"when n = {n}")
                print(f"x = {x}, y = {y}")
        
        try:
            # k1 = f(lastx, y) INPUT FUNCTION
            k1 = 2 * x * (y**2)
        
            # nextx
            x = x + h
        
            u = y + (h * k1)
        
            # k2 = f(nextx, u) INPUT FUNCTION
            k2 = 2 * x * (u**2)

            # nexty
            y = y + h*((k1 + k2) / 2)
        except OverflowError as e:
            print(f"Your function may have a discontinuity before"
                  + f" x = {x}\n"
                  + f"or is approaching +/- infinity")
            raise e
        
        
