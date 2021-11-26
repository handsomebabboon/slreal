def f2c(in_f):
    return ((in_f-32)*5)/9  

def f2k(in_f):
    return 273.5 + ((in_f - 32.0) * (5.0/9.0))

def c2k(in_c):
    return (in_c + 273.15)
    
def c2f(in_c):
    return (in_c * 1.8) + 32

def k2c(in_k):
    return in_k - 273
def k2f(in_k):
    return 1.8 * (in_k - 273) + 32

def doConversion():
    conversions = []
    while True:
        unitfrom = input('enter unit to convert from c - celcius f - fahreneheit k - kelvin , -1 to exit \n')

        if unitfrom == '-1':
            break

        unitto = input('enter unit to convert to c - celcius k - kelvin f - fahrenheit\n')
        mag = float(input('enter quantity of unit: '))

        if unitfrom == 'f' and unitto =='c':
            res = f2c(mag)
            print("{} degrees fahreneheit is equal to {} degrees celcius".format(mag,res))
            conversions.append('fahrenehit to celcius ,{} fahrenehit = {} celcius'.format(mag,res))
        elif unitfrom == 'f' and unitto =='k':
            res = f2k(mag)
            print("{} degrees fahrenehit is equal to {} kelvin".format(mag,res))
            conversions.append('fahrenehit to kelvin ,{} fahreneheit = {} kelvin'.format(mag,res))
        elif unitfrom == 'c' and unitto =='k':
            res = c2k(mag)
            print("{} degrees celcius is equal to {} kelvin".format(mag,res))
            conversions.append('celcius to kelvin, {} celcius = {} kelvin'.format(mag,res))
        elif unitfrom == 'c' and unitto =='f':
            res = c2f(mag)
            print("{} degrees celcius is equal to {} degress fahrenheit".format(mag,res))
            conversions.append('celcius to fahrenheit, {} celcius = {} fahrenheit'.format(mag,res))
        elif unitfrom == 'k' and unitto =='c':
            res = k2c(mag)
            print("{} kelvin is equal to {} degress celcius".format(mag,res))
            conversions.append('kelvin to celcius, {} kelvin = {} celcius'.format(mag,res))
        elif unitfrom == 'k' and unitto =='f':
            res = k2f(mag)
            print("{} kelvin is equal to {} degress fahrenheit".format(mag,res))
            conversions.append('kelvin to fahrenehit, {} kelvin = {} fahrenheit'.format(mag,res))

        elif unitfrom == unitto:
            
            res = mag
            if unitfrom == 'f':
                print("{} degrees fehrenheit is equal to {} degress fahreneheit".format(mag,res))
                conversions.append('fahreneheit to fahrenehit, {} degrees fahrenehit = {} degrees fahrenheit'.format(mag,res))
            elif unitfrom == 'c':
                print("{} degrees celcius is equal to {} degrees celcius".format(mag,res))
                conversions.append('celcius to celcius, {} degrees celcius = {} degrees celcius'.format(mag,res))
            else:
                print("{} kelvin is equal to {} kelvin".format(mag,res))
                conversions.append('kelvin to kelvin, {} kelvin = {} kelvin'.format(mag,res))
        else:
            break

    return conversions

def fromConversions(res):                   #function to extract conversions satisfyingg user specified "from" value 
    while True:
        choice = input('enter which conversions to view (from conversions) f:fahrenehit , k:kelvin , c:celcius , -1:exit \n')

        if choice == 'f':
            for str in conversions:
                if str[0] == 'f':
                    res.append(str)
            print(res)
            res.clear()
        elif choice == 'k':
            for str in conversions:
                if str[0] == 'k':
                    res.append(str)
            print(res)
            res.clear()
        elif choice == 'c':
            for str in conversions:
                
                if str[0] == 'c':
                    res.append(str)
            print(res)
            res.clear()
        elif choice == '-1':
            break
        
        else:
            print('invalid input')


def toConversions(res):             #function to extract conversions satisfying user specified "to" value
    while True:
        choice = input('enter which conversions to view (to conversions) f:fahrenehit , k:kelvin , c:celcius , -1:exit \n')

        if choice == 'f':
            for str in conversions:
                if str[-10] == 'f':
                    res.append(str)
            print(res)
            res.clear()
        elif choice == 'k':
            for str in conversions:
                if str[-6] == 'k':
                    res.append(str)
            print(res)
            res.clear()
        elif choice == 'c':
            for str in conversions:
                if str[-7] == 'c':
                    res.append(str)
            print(res)
            res.clear()
        elif choice == '-1':
            break
        
        else:
            print('invalid input')


def sort(conversions):
    
    while True:
        res = []
        choice = int(input('1 - display conversions prompting user for from value 2 - display conversions prompting user for to value 3 - exit '))

        if choice == 1:
            fromConversions(res)
        elif choice == 2:
            toConversions(res)
            
        elif choice == 3:
            break
        else:
            print('invalid option entered')


if __name__ == '__main__':
    conversions = doConversion()
    print('conversions performed: {}'.format(conversions))
    
    sort(conversions)