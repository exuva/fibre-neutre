import math
def calc():
    print("calcul de la fibre neutre")
    # fibre neutre
    fn = float(input("fn"))

    print(" ")
    print("calcul longueur developper")
    R = float(input("rayon interne")
    print ("sans fibre neutre)"))
    Agl = float(input("angle par.. rap a forme"))

    Lp = (math.pi * (R + fn) * Agl) / 180
    Lp = (round(Lp, 2))
    print("longueur developper du plis =", Lp)


calc()