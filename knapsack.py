import pulp

model = LpProblem(sense=LpMaximize)

W = 5000

costs = [208,117,105,202,77,162,17,196,169,114,205,79,7,223,107,217,62,9,159,109,60,200,98,31,209,232,129,134,33,6,51,34,183,11,69,24,74,189,174,219,188,92,49,212,70,108,83,125,55,52,143,142,3,73,243,88,214,80,157,127,176,28,249,184,23,87,50,59,4,133,112,29,68,115,248,118,170,85,245,194,37,48,113,66,10,186,138,86,178,12,158,238,242,20,123,199,2,206,137,45,110,149,191,22,227,241,197,13,168,237,111,177,65,32,104,40,140,126,201,75,236,225,38,90,61,64,131,220,81,41,221,36,132,216,72,56,89,124,192,240,172,215,139,247,76,207,179,135,19,82,222,198,14,97,116,44,130,161,175,46,233,156,204,122,171,180,103,250,244,210,187,43,21,155,8,190,101,71,145,195,218,27,146,120,173,119,203,102,16,163,193,15,96,26,213,25,39,95,160,42,235,230,166,231,144,58,84,182,226,164,152,181,239,224,30,121,78,54,94,35,234,57,106,147,18,185,136,141,100,229,1,148,63,67,93,91,150,211,246,165,99,228,151,167,5,128,47,153,154,53]
weight = [32,13,40,16,43,24,39,35,15,17,54,37,6,53,47,38,11,46,41,25,10,51,52,5,49,33,12,30,14,26,31,18,55,50,20,22,42,7,29,34,44,28,21,36,45,9,19,48,8,27,23,26,50,49,14,54,39,6,32,27,18,43,8,7,28,21,20,31,33,44,51,17,22,48,13,52,37,41,24,15,12,42,40,30,10,19,38,55,9,45,5,23,53,36,35,34,29,25,11,47,46,16,16,54,36,48,44,39,45,38,20,27,46,49,25,28,37,43,35,17,51,30,40,32,23,9,47,8,12,33,18,31,21,15,11,7,6,19,10,34,24,42,41,22,55,50,29,26,14,52,13,5,53,6,44,16,13,14,41,12,31,53,33,27,20,25,21,23,19,50,43,36,18,47,39,7,34,52,40,28,35,24,22,48,55,9,45,10,46,26,37,38,54,15,49,42,11,51,5,8,17,32,30,29,7,34,23,25,12,55,36,44,28,10,54,27,19,16,20,5,18,13,26,39,42,22,51,37,43,11,31,29,24,21,41,53,47,9,46,49,6,35,40,52,50,38,30,48,14,32]
# proměnné -- 1, pokud i ty prvek je v batohu, pracujeme pouze s čísly, takže booleany nejsou
variables = [LpVariable(str(i), cat=LpBinary) for i in range(len(costs))]

# podmínky
model += sum([w * v for w,v in zip(weight, variables)]) <= W # zip vezme dva listy a kombinuje je dohromady


# účelová funkce

model += sum([c * v for c,v in zip(costs, variables)]) # zip vezme dva listy a kombinuje je dohromady

model.solve()

for i in range(len(costs)):
    print(f"{i}: {variables[i].value()}")
