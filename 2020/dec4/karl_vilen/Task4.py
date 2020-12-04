import os, sys, traceback, csv, time
sys.path.insert(0, os.path.abspath(".."))
import argparse


if __name__ == '__main__':

    f=open("Task4.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace(":", " ")
        i = i.split()
        theInput.append(i)
    f.close()

    a = dict(ecl="", pid="", eyr="", hcl="", byr="", iyr="", cid="", hgt="")

    passport = []
    passport.append(a.copy())

    for i in theInput:
        j = 0
        if i == []:
            passport.append(a.copy())
        else:
            while j < len(i):
                theId = i[j]
                theValue = i[j+1]
                passport[len(passport)-1][theId] = theValue
                j+=2

    validAmount = 0

    debugError = True

    for i in passport:

        inValid = False

        if i["ecl"] == "":
            inValid = True
            if debugError:
                print("inValid ecl 1")
                print(i["ecl"])
        else:
            if i["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                inValid = True
                if debugError:
                    print("inValid ecl 2")
                    print(i["ecl"])

        if i["pid"] == "":
            inValid = True
            if debugError:
                print("inValid pid 1")
                print(i["pid"])
        else:
            if len(i["pid"]) != 9:
                inValid = True
                if debugError:
                    print("inValid pid 2")
                    print(i["pid"])
            else:
                theString = i["pid"]
                for j in theString:
                    if j not in ("0123456789"):
                        inValid = True
                        if debugError:
                            print("inValid pid 3")
                            print(i["pid"])
        
        if i["eyr"] == "":
            inValid = True
            if debugError:
                print("inValid eyr 1")
                print(i["eyr"])
        elif 2020 > int(i["eyr"]) or int(i["eyr"]) > 2030:
            inValid = True
            if debugError:
                print("inValid eyr 2")
                print(i["eyr"])
        
        if i["hcl"] == "":
            inValid = True
            if debugError:
                print("inValid hcl 1")
                print(i["hcl"])
        else:
            if i["hcl"][0] != "#":
                inValid = True
                if debugError:
                    print("inValid hcl 2")
                    print(i["hcl"])
            else:
                theString = i["hcl"][1:]
                if len(theString) != 6:
                    if debugError:
                        print("inValid hcl 3")
                        print(i["hcl"])
                    inValid = True
                else:
                    for j in theString:
                        if j not in ("0123456789abcdef"):
                            inValid = True
                            if debugError:
                                print("inValid hcl 4")
                                print(i["hcl"])
                            break
        
        if i["byr"] == "":
            inValid = True
            if debugError:
                print("inValid byr 1")
                print(i["byr"])
        elif 1920 > int(i["byr"]) or int(i["byr"])  > 2002:
            inValid = True
            if debugError:
                print("inValid byr 2")
                print(i["byr"])
        
        if i["iyr"] == "":
            inValid = True
            if debugError:
                print("inValid iyr 1")
                print(i["iyr"])
        elif 2010 > int(i["iyr"]) or int(i["iyr"])  > 2020:
            inValid = True
            if debugError:
                print("inValid iyr 2")
                print(i["iyr"])
        
        if i["hgt"] == "":
            inValid = True
            if debugError:
                print("inValid hgt 1")
                print(i["hgt"])
        else:
            
            if i["hgt"][-2:] not in ["cm", "in"]:
                inValid = True
                if debugError:
                    print("inValid hgt 2")
                    print(i["hgt"])
            else:

                if i["hgt"][-2:] == "cm":
                    if 150 > int(i["hgt"][:-2]) or int(i["hgt"][:-2])  > 193:
                        inValid = True
                        if debugError:
                            print("inValid hgt 3")
                            print(i["hgt"])
                elif i["hgt"][-2:] == "in":
                    if 59 > int(i["hgt"][:-2]) or int(i["hgt"][:-2])  > 76:
                        inValid = True
                        if debugError:
                            print("inValid hgt 4")
                            print(i["hgt"])

        if inValid == False:
            validAmount += 1


    print("Done")
    print(validAmount)

