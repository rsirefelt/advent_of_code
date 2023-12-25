if __name__ == '__main__':

    f=open("Task24.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace(" ","")
        i = i.split("@")
        a = i[0].split(",")
        b = i[1].split(",")
        for i in range(0, len(a)):
            a[i] = int(a[i])
        for i in range(0, len(b)):
            b[i] = int(b[i])
        theInput.append([a,b])
    f.close()

    vxCandidates_full = []
    vyCandidates_full = []
    vzCandidates_full = []
    vRange = 5000

    for i in range(len(theInput)-1):
        vxCandidates_new = []
        vyCandidates_new = []
        vzCandidates_new = []
        for j in range(i+1, len(theInput)):
            
            px1 = theInput[i][0][0]
            py1 = theInput[i][0][1]
            pz1 = theInput[i][0][2]

            px2 = theInput[j][0][0]
            py2 = theInput[j][0][1]
            pz2 = theInput[j][0][2]

            vx1 = theInput[i][1][0]
            vy1 = theInput[i][1][1]
            vz1 = theInput[i][1][2]

            vx2 = theInput[j][1][0]
            vy2 = theInput[j][1][1]
            vz2 = theInput[j][1][2]

            if vx1 == vx2:
                for vRock in range(-vRange, vRange):
                    if vRock == vx1:
                        continue
                    remainder = (px1-px2) % (vRock - vx1)
                    if remainder == 0 and vx1 not in vxCandidates_new:
                        vxCandidates_new.append(vRock)
            if vy1 == vy2:
                for vRock in range(-vRange, vRange):
                    if vRock == vy1:
                        continue
                    remainder = (py1-py2) % (vRock - vy1)
                    if remainder == 0 and vy1 not in vyCandidates_new:
                        vyCandidates_new.append(vRock)
            if vz1 == vz2:
                for vRock in range(-vRange, vRange):
                    if vRock == vz1:
                        continue
                    remainder = (pz1-pz2) % (vRock - vz1)
                    if remainder == 0 and vz1 not in vzCandidates_new:
                        vzCandidates_new.append(vRock)

        if len(vxCandidates_new)>0:
            if vxCandidates_full == []:
                vxCandidates_full = vxCandidates_new.copy()
            else:
                for k in vxCandidates_full:
                    if k not in vxCandidates_new:
                        vxCandidates_full.remove(k)
        if len(vyCandidates_new)>0:
            if vyCandidates_full == []:
                vyCandidates_full = vyCandidates_new.copy()
            else:
                for k in vyCandidates_full:
                    if k not in vyCandidates_new:
                        vyCandidates_full.remove(k)
        if len(vzCandidates_new)>0:
            if vzCandidates_full == []:
                vzCandidates_full = vzCandidates_new.copy()
            else:
                for k in vzCandidates_full:
                    if k not in vzCandidates_new:
                        vzCandidates_full.remove(k)

    thevx = vxCandidates_full[0]
    thevy = vyCandidates_full[0]
    thevz = vzCandidates_full[0]

    px1 = theInput[0][0][0]
    py1 = theInput[0][0][1]
    pz1 = theInput[0][0][2]
    px2 = theInput[1][0][0]
    py2 = theInput[1][0][1]
    pz2 = theInput[1][0][2]
    vx1 = theInput[0][1][0]
    vy1 = theInput[0][1][1]
    vz1 = theInput[0][1][2]
    vx2 = theInput[1][1][0]
    vy2 = theInput[1][1][1]
    vz2 = theInput[1][1][2]

    slope1 = (vy1 - thevy)/(vx1 - thevx)
    slope2 = (vy2 - thevy)/(vx2 - thevx)

    point1 = py1 - (slope1 * px1)
    point2 = py2 - (slope2 * px2)

    thepx = round((point2-point1) / (slope1-slope2))
    thepy = round(slope1 * thepx + point1)

    t = ((thepx - px1) / (vx1 - thevx))

    thepz = pz1 + (vz1 - thevz) * t

    print(thepx + thepy + thepz)