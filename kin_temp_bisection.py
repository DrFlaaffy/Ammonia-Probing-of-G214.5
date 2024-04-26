#---------------------------
#Kinetic Temperature via bisection method
#Friesen et al. (2017), ApJ, 843, 63, equation 4
#---------------------------
# Initial temperatures
lower_bound = 3 #Kelvin
higher_bound = 20
t_rot = 11.736435 #Rotational temperature
t_0 = 41.5 #Energy difference between states
epsilon = 0.001 #Accuracy
#---------------------------
def func(t_k):
    return t_rot - t_k*(1 + t_k/t_0 * np.log(1 + 3/5 * np.exp(-15.7/t_k)))

def bisection(a,b):
    if (func(a) * func(b) >= 0):
        print("The root is out of bounds.")
        return
    c = a
    while ((b-a) >= epsilon):
        c = (a+b)/2
        if (func(c) == 0.0):
            break
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
    print('The value of T_k is : ',"%.4f"%c)

bisection(lower_bound, higher_bound)

