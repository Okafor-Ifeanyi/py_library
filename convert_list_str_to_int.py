# eval function to convert str to int

num = ['1','2','3','4','5']

convert = list()

convert = [eval(i) for i in num]
print(convert)