while True:
    print("Select the Mode You Wanted:\n1:Capacitor Value\n2:Capacitor code")
    mode = int(input("Enter Mode(1 or 2): "))

    if mode ==1:
        capVal = input("Enter Capacitor Value(With units(nF,pF,uF)): ")
        strlet = ''
        value = ''
        units = ['F','uF','nF','pF']
        powers = [0,-6,-9,-12]
        ref = -9
        for i in capVal:
            if i.isalpha():
                strlet += i
            if i.isnumeric() or i == '.':
                value+= i
        value = float(value)
        index = units.index(strlet)
        powerVal = powers[index]
        capPF = str(int(value*10**(12+powers[index])))
        offset = len(capPF)-2
        capCode = capPF[0:2]+str(offset)
        print(capCode)
    if mode == 2:
        capCode_ = input("Enter Capacitor Code: ")
        neededUnit = input("Enter the unit you needed in answer(F,nF,uF,pF): ")
        units = ['F', 'uF', 'nF', 'pF']
        powers = [0, -6, -9, -12]
        capVal_ = int(capCode_[0:2])*10**(int(capCode_[2]))
        # print(capVal_)
        devidend = 10**(12-abs(powers[units.index(neededUnit)]))
        capVal_ = capVal_/devidend
        print(capVal_,neededUnit)
