uqf = [];

def Initialise (n):
    for i in range(n) :
        uqf.append(i)
    print("Array initialised with " + str(n) + " elements")
    return uqf

def Union (p, q, uqf) :
    val = uqf[p]
    for i in range(len(uqf)) :
        if uqf[i] == val :
            uqf[i] = uqf[q]

    print("Union performed on " + str(p) + " and " + str(q) + "!")
    print(uqf)

def UnionCheck (p, q, uqf) :
    if uqf[p] == uqf[q] :
        print(str(p) + " and " + str(q) + " are connected!")
        return True
    else :
        print(str(p) + " and " + str(q) + " are NOT onnected!")
        return False

print(Union(0, 3, Initialise(12)))
print(Union(0, 2, uqf))
print(UnionCheck(0, 3, uqf))
