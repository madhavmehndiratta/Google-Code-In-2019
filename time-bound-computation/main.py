import time
import numpy
from numba import jit
import matplotlib.pyplot as plot



@jit(nopython=True)
def jit_multiplication(n, a, b):
    number_list = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for var in range(n):
            number_list[i][var] = 0
            for x in range(n):
                number_list[i][var] += a[i][x] * b[x][var]



class matrix_calculation():
    def __init__(self):
        self.timepython = []
        self.inputsize = []
        self.timenum = []
        self.timejit = []

    def generate(self, n):
        ar1 = numpy.random.rand(n, n)
        ar2 = numpy.random.rand(n, n)
        return ar1, ar2

    def multiplication(self, n, a, b):
        number_list = [[0 for col in range(n)] for row in range(n)]
        for i in range(n):
            for element in range(n):
                number_list[i][element] = 0
                for x in range(n):
                    number_list[i][element] += a[i][x] * b[x][element]

    def main(self):
        for i in range (1,20):
            var = i*10
            a,b = self.generate(var)

            start = time.process_time()
            self.multiplication(var, a, b)
            stop = time.process_time()
            self.timepython.append(stop - start)

            start = time.process_time()
            numpy.matmul(a,b)
            stop = time.process_time()
            self.timenum.append(stop - start)

            start = time.process_time()
            jit_multiplication(var, a, b)
            stop = time.process_time()
            self.timejit.append(stop - start)

            self.inputsize.append(var)
            print("\rComputing", i*10, end="")
            time.sleep(0.5)

        
        plot.plot(self.inputsize, self.timepython,label= "With python")
        plot.plot(self.inputsize, self.timenum,label = "With numpy")
        plot.plot(self.inputsize, self.timejit,label = "With python and numba.jit")
        plot.xlabel("Input size")
        plot.ylabel("Time")

        plot.title("Time Bound Computation For Matrix Multiplication")
        plot.legend()
        plot.show()

print("Welcome to the Time Bound Computation For Matrix Multiplication ")
compute = matrix_calculation()
compute.main()
print()
