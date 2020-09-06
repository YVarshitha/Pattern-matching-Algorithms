import time
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M
    j = 0

    computeLPSArray(pat, M, lps)

    i = 0
    count = 0;
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            count = count + 1;
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]


        elif i < N and pat[j] != txt[i]:

            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    print('Number of comparisons');
    print(count);

def computeLPSArray(pat, M, lps):
    len = 0

    lps[0]
    i = 1


    while i < M:
        if pat[i]== pat[len]:

            len += 1
            lps[i] = len
            i += 1
        else:

            if len != 0:
                len = lps[len-1]

            else:
                lps[i] = 0
                i += 1
start=time.time()
print("Case 1")
txt = "CRACK!!  CRACK!!  CRACK!!  CRACK!!"
pat = "CRACK"

KMPSearch(pat, txt)

print("Case 2")

txt1 = "Venice is city of water.Venice is one of the beautiful cities across the world."
pat1 = "Venice"

KMPSearch(pat1,txt1)

print("Case 3")

txt2 = "Venice is city of water.Venice is one of the beautiful cities across the world."
pat2 = "beautiful"

KMPSearch(pat2,txt2)

print("Case 4")

txt3 = "Venice"
pat3 = "Venice"

KMPSearch(pat3,txt3)

print("Case 5")

txt4 = "CRACK!!  CRACK!!  CRACK!!"
pat4 = "CRA"

KMPSearch(pat4,txt4)

print("Case 6")

txt5 = "CRACK!!  CRACK!!  CRACK!!  CRACK!!"
pat5 = "RACK!!"

KMPSearch(pat5,txt5)

print("Case 7")

txt6 = "Venice is city of water.Venice is one of the beautiful cities across the world."
pat6 = "world"

KMPSearch(pat6,txt6)

print("Case 8")

txt7 = "onlinetextmessaging"
pat7 = "mess"

KMPSearch(pat7,txt7)

print("Case 9")


txt8 = "indiaismycountry"
pat8 = "india"

KMPSearch(pat8,txt8)

print("Case 10")

txt9 = "Liveincharlotte"
pat9 = "char"

KMPSearch(pat9,txt9)

end = time.time();
timetaken=end-start
print('Total time taken')
print(timetaken);


