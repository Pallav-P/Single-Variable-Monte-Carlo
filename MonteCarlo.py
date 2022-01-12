# let the integral(a,b,f(x)) represent an integral from a to b of the function f(x) with respect to x
# let avg(f(x),a,b) represent the average of a function on the closed interval a,b
# Using the Second Fundamnental theorem of calculus avg(f(x),a,b) = 1/(b-a) * integral(a,b,f(x))
# rearranging the function given in the second fundamental theorem of calculus we get (b-a)avg(f(x),a,b) = integral(a,b, f(x))

# We compute average of the function on the interval using multiple random samples in the given interval.
# We then use this calculated average to find the integral using the equation given above.

import numpy as np


func_name = "f(x)"
def func(x):
    return np.sin(x)

def generate_random(a, b, num_samples):
    return np.random.uniform(a, b, num_samples)



def calculate_average(list, num_samples):
    sum = 0
    for i in range(0, num_samples):
        sum += func(list[i])

    return sum / num_samples




def run(a, b, num_samples):
    

    list = generate_random(a, b, num_samples)

    average = calculate_average(list, num_samples)

    integral = (b - a) * average

    print(f"{integral}")

    return integral

def integral(a, b, num_samples, num_iter):
    avg_sum = 0
    for i in range(0, num_iter):
        avg_sum += run(a, b, num_samples)
    avg_integral = avg_sum / num_iter
    print(f"The integral of {func_name} using Monte Carlo Method from {a} to {b} using {num_samples} samples and {num_iter} iterations is: {avg_integral}")

if __name__ == "__main__":
    print(f"Integrating {func_name} \n")
    print("Enter the bounds of integration")
    a = float(input("Enter the lower bound: "))
    b = float(input("Enter the upper bound: "))

    

    num_samples = int(input("Enter the number of samples to be used for one Monte Carlo Calculation: "))

    num_threads = int(input("Enter the number of iterations the code should be run for: "))

    print(f"The integral of {func_name} using Monte Carlo Method from {a} to {b} using {num_samples} samples is:")
    integral(a, b, num_samples, 100)
    z = input()