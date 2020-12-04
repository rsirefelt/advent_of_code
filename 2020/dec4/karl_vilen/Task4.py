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

    emptyDict = dict(ecl="", pid="", eyr="", hcl="", byr="", iyr="", cid="", hgt="")

    passports = []
    passports.append(emptyDict.copy())

    for i in theInput:
        j = 0
        if i == []:
            passports.append(emptyDict.copy())
        else:
            while j < len(i):
                theId = i[j]
                theValue = i[j+1]
                passports[len(passports)-1][theId] = theValue
                j+=2

    validAmount = 0

    for i in passports:

        if "" in [i["ecl"],i["pid"],i["eyr"],i["hcl"],i["byr"],i["iyr"],i["hgt"]]:
            continue

        if i["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        pidString = i["pid"]
        if len(pidString) != 9:
            continue
        else:
            for j in pidString:
                if j not in ("0123456789"):
                    continue
        
        if not (2020 <= int(i["eyr"]) <= 2030):
            continue
        
        if i["hcl"][0] != "#":
            continue
        else:
            hairCol = i["hcl"][1:]
            if len(hairCol) != 6:
                continue
            else:
                for j in hairCol:
                    if j not in ("0123456789abcdef"):
                        continue
        
        if not (1920 <= int(i["byr"]) <= 2002):
            continue
        
        if not (2010 <= int(i["iyr"]) <= 2020):
            continue
        

        lenUnit = i["hgt"][-2:]
        length = i["hgt"][:-2]        
        if lenUnit == "cm":
            if not (150 <= int(length) <= 193):
                continue
        elif lenUnit == "in":
            if not (59 <= int(length) <= 76):
                continue
        else:
            continue

        validAmount += 1


    print("Done")
    print(validAmount)
