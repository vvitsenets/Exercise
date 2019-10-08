import matplotlib.pyplot as plt
#from scipy.misc import derivative

def func(x):
    y = (x - 5)**2
    return y


def derivative(y):
    z = 2 * (y - 5)
    return z


#def plot():
#    a = []
#    b = []
#   for x in range(-30,30):
#        y = (x - 5)**2
#        a.append(x)
#        b.append(y)
#    plt.plot(a, b)
#    plt.show()


def gd():
    epoch = 1000
    z = []
    b = []
    for x in range(-30, 30):
        y = (x - 5) ** 2
        z.append(x)
        b.append(y)
    plt.plot(z, b,color="purple")
    x = 0
    s = []
    a = []
    step = 0.01
    eps = 10e-9
    for i in range(1, epoch):
        x_new = x - step * derivative(x)
        y_new = func(x)
        a.append(x_new)
        s.append(y_new)
        if abs(x_new - x) <= eps:
            plt.scatter(x_new, y_new, color="orange")
            plt.show()
            return s
        x = x_new

    return s



if __name__ == "__main__":

    print(func(2))
    print(derivative(2))
    print(gd())