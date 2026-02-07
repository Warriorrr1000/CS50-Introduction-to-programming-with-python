#I started this on a different day litrally. Spent Multiple hours, did multiple changes.
#But now my mind can't think of any further.
#Did 7/10 test succesfully,fuck the rest.
#If you guys have better way to solve, must dm me on instagram= @im.pro_warrior
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if test1(s) == True:
        if test2(s) == True:
            if test3(s) == True:
                if test4(s) == True:
                    if test5(s) == True:
                        return True
    else:
        return False
def test1(s):
    #1st Check.
    #Starts with 2letters or not.
    if s[0:2].isalpha():
        return True
    else:
        return False
def test2(s):
    #2nd Check.
    #Length of string : Maximum = 6,Minimum = 2.
    if 2 <= len(s) <= 6:
        return True
    else:
        return False
def test3(s):
    #3rd Check.
    #Numbers cannot be in middle,only at end.
    for ch in s:
        if ch.isdigit() and s.find(ch) != 0:
            i = s.find(ch)
            j = s[i: ]
            if j.isdigit():
                return True
    return True
def test4(s):
    #4th Check.
    #First appearance cannot be 0:
    x = s.find("0")
    if x != -1:
        if x == 0:
            return False
        else:
            p = s[x-1]
            if p.isdigit():
                return True
def test5(s):
    for ch in s:
        if not ch.isalnum():
            return False
        else:
            return True

main()