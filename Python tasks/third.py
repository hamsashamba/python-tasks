from collections import Counter

def most_frequent(l):
    c = Counter(l)  
    return c.most_common(1)[0][0]  


l = input('Enter the list of elements: ')
lst=l.split()
print(f"The most frequent element is: {most_frequent(lst)}")