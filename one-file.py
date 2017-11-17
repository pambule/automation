import os
def function1():
    str="1100000f506f77657245646765204d363230"
    str1=str.decode("hex")
    print ''.join(ch for ch in str1 if ch.isalnum())

if __name__=="__main__":
    function1()
