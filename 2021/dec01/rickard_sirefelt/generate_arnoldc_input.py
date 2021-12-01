import numpy as np

x = np.loadtxt("input_test.txt").astype(np.int32)

f = open("arnoldC_input_func.arnoldC", "w+")

f.write("LISTEN TO ME VERY CAREFULLY input\n")
f.write("I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE idx\n")
f.write("I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE mod80\n")
f.write("GIVE THESE PEOPLE AIR\n")

for id in range(1 + (int)(x.size/80)):
    f.write("HEY CHRISTMAS TREE r%d\n" % id)
    f.write("YOU SET US UP @I LIED\n")
    f.write("GET TO THE CHOPPER r%d\n" % id)
    f.write("HERE IS MY INVITATION mod80\n")
    f.write("YOU ARE NOT YOU YOU ARE ME %d\n" % id)
    f.write("ENOUGH TALK\n")
    f.write("BECAUSE I'M GOING TO SAY PLEASE r%d\n" % id)
    f.write("HEY CHRISTMAS TREE ret%d\n" % id)
    f.write("YOU SET US UP @I LIED\n")
    f.write("GET YOUR ASS TO MARS ret%d\n" % id)
    f.write("DO IT NOW input%d idx\n" % id)
    f.write("I'LL BE BACK ret%d\n" % id)
    f.write("YOU HAVE NO RESPECT FOR LOGIC\n")
f.write("HASTA LA VISTA, BABY\n\n")

n = 0
f.write("LISTEN TO ME VERY CAREFULLY input%d\n" % n)
f.write("I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE idx\n")
f.write("GIVE THESE PEOPLE AIR\n")

for idx, i in enumerate(x):

    if (idx % 80 == 0):
        n = n + 1
        f.write("HASTA LA VISTA, BABY\n")
        f.write("LISTEN TO ME VERY CAREFULLY input%d\n" % n)
        f.write("I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE idx\n")
        f.write("GIVE THESE PEOPLE AIR\n")

    f.write("HEY CHRISTMAS TREE r%d\n" % idx)
    f.write("YOU SET US UP @I LIED\n")
    f.write("GET TO THE CHOPPER r%d\n" % idx)
    f.write("HERE IS MY INVITATION idx\n")
    f.write("YOU ARE NOT YOU YOU ARE ME %d\n" % idx)
    f.write("ENOUGH TALK\n")
    f.write("BECAUSE I'M GOING TO SAY PLEASE r%d\n" % idx)
    f.write("I'LL BE BACK %d\n" % i)
    f.write("YOU HAVE NO RESPECT FOR LOGIC\n")

f.write("HASTA LA VISTA, BABY\n")
