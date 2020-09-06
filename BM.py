NO_OF_CHARS = 256
import time
def badCharHeuristic(string, size):

    badChar = [-1]*NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i;

    return badChar

def search(txt, pat):
    count = 0;
    m = len(pat)
    n = len(txt)

    badChar = badCharHeuristic(pat, m)

    s = 0
    while(s <= n-m):
        j = m-1


        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
            count = count+1;
        if j<0:
            print("Pattern occur at shift = {}".format(s))

            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:

            s += max(1, j-badChar[ord(txt[s+j])])
    print("Total no of comparison is")
    print(count)

def main():
    start=time.time()
    print("Case 1")
    txt = "CRACK!!  CRACK!!  CRACK!!  CRACK!!"
    pat = "CRACK"

    search(txt, pat)

    print("Case 2")

    txt1 = "Venice is city of water.Venice is one of the beautiful cities across the world."
    pat1 = "Venice"

    search(txt1,pat1)

    print("Case 3")

    txt2 = "Venice is city of water.Venice is one of the beautiful cities across the world."
    pat2 = "beautiful"

    search(txt2,pat2)

    print("Case 4")

    txt3 = "Venice"
    pat3 = "Venice"

    search(txt3,pat3)

    print("Case 5")

    txt4 = "CRACK!!  CRACK!!  CRACK!!"
    pat4 = "CRA"

    search(txt4,pat4)

    print("Case 6")

    txt5 = "CRACK!!  CRACK!!  CRACK!!  CRACK!!"
    pat5 = "RACK!!"

    search(txt5,pat5)

    print("Case 7")

    txt6 = "Venice is city of water.Venice is one of the beautiful cities across the world."
    pat6 = "world"

    search(txt6,pat6)

    print("Case 8")

    txt7 = "onlinetextmessaging"
    pat7 = "mess"

    search(txt7,pat7)

    print("Case 9")


    txt8 = "indiaismycountry"
    pat8 = "india"

    search(txt8,pat8)

    print("Case 10")

    txt9 = "Liveincharlotte i hiu"
    pat9 = "char"

    search(txt9,pat9)

    end = time.time();
    timetaken=end-start
    print('Total time taken')
    print(timetaken);


if __name__ == '__main__':
    main()
