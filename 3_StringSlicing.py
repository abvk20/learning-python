s1 ="""you can ACHIEVE anything you want"""
s2 ="you can ACHIEVE anything you want"
s3 ='you can ACHIEVE anything you want'
print(len(s1))
print(s1[0:33:])
print(s2[::-1])
print(s3[-5:-1:])
"""
    ------------------------------Indexing from 0 to length-1--------------------------------
                            0   1   2   3   4   5   6
              word =        A   C   H   I   E   V   E
                            -7  -6  -5  -4  -3  -2  -1
                word[Start,Stop,Step]
                here Start and Step default to None 
                if Step is None then internal iterator of the Slice method runs till exhausted
    ______________________________Reverse Index is done as follows---------------------------
"""
word="ACHIEVE"
print(word[0:3])
print(word[-1:-8:-1])
print(word[None:None:1])

