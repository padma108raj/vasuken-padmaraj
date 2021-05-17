# WAP to find number of occurrences of each letter present in a word

word=input("Enter a word:")
d={}
for letter in word:
  d[letter]=d.get(letter,0)+1

for k,v in d.items():
  print(k,":",v)
