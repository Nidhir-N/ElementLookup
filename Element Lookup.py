elementList=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
 'Rg', 'Cn', 'Uut', 'Uuq', 'Uup', 'Uuh', 'Uus', 'Uuo']


def findatomic(element):
    for i in range(0,118):
        if elementList[i]==element:
            return i+1
        


def findperiod(atomic):
    if atomic-2<=0:
        return 1
    elif atomic-10<=0:
        return 2
    elif atomic-18<=0:
        return 3
    elif atomic-36<=0:
        return 4
    elif atomic-54<=0:
        return 5
    elif atomic-86<=0:
        return 6
    else:
        return 7



def findgroup(atomic,element):
    if atomic==1:
        return 1
    elif atomic==2:
        return 18
    elif atomic<11:
        if atomic-2<3:
            return atomic-2
        else:
            return atomic+8
    elif atomic<19:
        if atomic-10<3:
            return atomic-10
        else:
            return atomic
    elif atomic<37:
        return atomic-18
    elif atomic<55:
        return atomic-36
    elif atomic<86:
        if atomic-54<4:
            return atomic-54
        elif atomic-54<18:
            return f"{element} is a Lanthanide, it has no group!"
        else:
            return atomic-68
    else:
        if atomic-86<4:
            return atomic-86
        elif atomic-86<18:
            return f"{element} is an Actinide, it has no group!"
        else:
            return atomic-100



while True:
    element=input("What is the atomic symbol of the element (Ex: H, Au, Na): ")
    if element in elementList:
        break
    else:
        print("Please enter a valid element symbol!")


atomic=findatomic(element)

period=findperiod(atomic)

group=findgroup(atomic,element)


print(f"Element {element} has the following chracteristics!")
print(f"Atomic Number: {atomic}")
print(f"Period: {period}")
print(f"Group: {group}")
