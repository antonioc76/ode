#! python
import math

# initial conditions, your step incriment,
# what point you want to estimate, and whether you want to show each step (bool)
def rk4(xo, yo, h, evaluate, show):
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
            #k1 = f(lastx, lasty) INPUT FUNCTION
            k1 = 2 * x * (y**2)

            #k2 = f(lastx + h/2, lasty + h/2) INPUT FUNCTION
            k2 = 2 * (x + (h/2)) * (y+(h/2)*k1)**2

            #k3 = f(lastx + h/2, lasty + hk2/2) INPUT FUNCTION
            k3 = 2 * (x + h/2) * (y + (h * k2)/2)**2

           # nextx = lastx + h
            x = x + h
            #k4 = f(nextx, lasty + hk3) INPUT FUNCTION
            k4 = 2 * (x) * (y + (h * k3))**2

            # nexty = lasty + h/6(k1+2k2+2k3+k4) INPUT FUNCTION
            y = y + (h / 6) * (k1 + (2*k2) + (2*k3) + k4)
        except OverflowError as e:
            print(f"Your function may have a discontinuity before"
                  + f" x = {x}\n"
                  + f"or is approaching +/- infinity")
            raise e
            
        
