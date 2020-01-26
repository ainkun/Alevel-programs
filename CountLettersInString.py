str1 = input("Enter the string: ")
letter = input("Enter the letter: ")
count = 0
for i in range(len(str1)):
    if letter == str1[i] or letter.upper() == str1[i]:
        count = count + 1

print('Letter "',letter,'" is repeated "',count,'"times.')
