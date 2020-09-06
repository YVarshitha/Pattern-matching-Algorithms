import time

def shift_table(txt, pat):
    m = len(pat)
    n = len(txt)
    dict = {}
    for i in range(n):
        dict[txt[i]] = m  # initialize all characters of text to length of text in shift table

    for j in range(m - 1):
        dict[pat[j]] = m - 1 - j  # update the characters of pattern in shift table
    return dict


def horspool(txt, pat):
    # create shift table
    table1 = shift_table(txt, pat)
    n = len(txt)  # length of text
    m = len(pat)  # length of pattern
    comparisions = 0  # total number of comparisions
    i = m - 1  # compare from right to left
    while i <= n:
        k = 0
        while k < m and pat[m - 1 - k] == txt[i - k]:
            k = k + 1
            comparisions += 1
        if k == m:  # print result if pattern is found in text
            print('Pattern found at index : ', i - m + 1)
            i = i + k if i<n else 1
        else:
            i = i + table1[txt[i]]  # find the length to be shifted based on value in shift table
            comparisions += 1

    print('Number of comparisions :', comparisions)
    print()

    return False


start = time.time()

print("Case 1")
txt = "CRACK!!  CRACK!!  CRACK!!  CRACK!!"
pat = "CRACK"

horspool(txt, pat)

print("Case 2")

txt1 = "Venice is city of water.Venice is one of the beautiful cities across the world."
pat1 = "Venice"

horspool(txt1, pat1)

print("Case 3")

txt2 = "Venice is city of water.Venice is one of the beautiful cities across the world."
pat2 = "beautiful"

horspool(txt2, pat2)

print("Case 4")

txt3 = "Venice"
pat3 = "Venice"

horspool(txt3, pat3)

print("Case 5")

txt4 = "CRACK!!  CRACK!!  CRACK!!"
pat4 = "CRA"

horspool(txt4, pat4)

print("Case 6")

txt5 = "CRACK!!  CRACK!!  CRACK!!  CRACK!!"
pat5 = "RACK!!"

horspool(txt5, pat5)

print("Case 7")

txt6 = "Venice is city of water.Venice is one of the beautiful cities across the world."
pat6 = "world"

horspool(txt6, pat6)

print("Case 8")

txt7 = "onlinetextmessaging"
pat7 = "mess"

horspool(txt7, pat7)

print("Case 9")

txt8 = "indiaismycountry"
pat8 = "india"

horspool(txt8, pat8)

print("Case 10")

txt9 = "Liveincharlotte"
pat9 = "char"

horspool(txt9, pat9)

end = time.time()

timetaken = end - start

print('Total time taken')
print(timetaken)
