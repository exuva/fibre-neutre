import math
def calc():
    print("calcul de la fibre neutre")
    # fibre neutre
    e = float(input("epaisseur mat="))
    b = (1 / 3)
    c = (1 / 2)
    Ri = float(input("rayon interieur="))
    if Ri <= 4:
        fn = e * b
    else:
        fn = e * c
    fn = (round(fn, 2))
    print("fn =", fn)
    print(" ")
    print("calcul longueur.. developper")
    R = float(input("rayon interne (sans fibre neutre)"))
    Agl = float(input("angle par.. rap a forme="))

    Lp = (math.pi * (R + fn) * Agl) / 180
    Lp = (round(Lp, 2))
    print("longueur developper du plis =", Lp)


calc()