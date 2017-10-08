Word = input("Enter string:\n")
word = list(Word)
Upp = ''
Low = ''
Num = ''
Sym = ''
for i in word:
    if i.isalnum():
        if i.isalpha():
            if i.isupper():
                Upp += i
            else:
                Low += i
        else:
            Num += i
    else:
        Sym += i
print("So these are the characters inputted and the classes they belong to:")
print("-Symbols:", Sym)
print("-Numbers:", Num)
print("-Uppercase letters:", Upp)
print("-Lowercase letters:", Low)
