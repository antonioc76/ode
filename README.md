In Numerical_Methods there are 3 automated versions of numerical methods used for approximating differential equations. 

To use these, you need to have python installed. Save the python file or files to your computer, right click on the one you want to use and select "edit with IDLE". Then, replace all instances of the expression for the differential with the expression for YOUR particular differential.

![](git@github.com:antonioc76/ode.git/Images/[main]/edit with IDLE.bmp?raw=true)

For example, if my differential is dy/dx = 2xy^2, then I need to replace every expression with 2 * x * y**2.

For the sake of example, this function (2xy^2) has already been substituted for f(x,y).

Note: the rk4 method involves function calls with x and u as well. These should follow the same form as f(x,y), but y will be replaced with u.

Once you have replaced these expressions with your own, save the file, then press f5 on your keyboard or select "run" at the top of your IDLE window. This will open the python terminal and run the file.

After the file has been run, begin typing the name of the method you're using into the terminal followed by an open parenthesis. Do not press enter.

For example if I have just run "eulers_method" I'll begin by typing "eulers_method(" (without the quotes) into the terminal. 

The terminal should show you a prompt "xo, yo, h, evaluate, show"

Inside the parentheses, type your initial x and y values, your step size h, the point you want to evaluate, and the word True or False depending on whether or not you want to show each step (True) of the estimation or only the last step (False). Then add the closed parenthesis and press enter.

For example, if my initial condition is y(0) = 1, and I want to use eulers method to estimate y(.5) with a step size of .25, and show each step, I would type eulers_method(0,1,.25,.5,True) into the terminal and press enter.
