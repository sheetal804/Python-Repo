'''
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

BANANA FRIES: Quantity bought: 1, Price:12
Net Price:12
POTATO CHIPS: Quantity bought:2 , Price:30
Net Price:30
APPLE JUICE: Quantity bought: 2, Price:10
Net Price:20
CANDY: Quantity bought:4 , Price:5
Net Price: 20
'''
from collections import OrderedDict
ordered_dictionary = OrderedDict()
for _ in range(int(input())):
    data=input().split()
    ordered_dictionary[' '.join(data[0:(len(data)-1)])]=ordered_dictionary.get(' '.join(data[0:(len(data)-1)]),0)+int(data[len(data)-1])
for x,y in ordered_dictionary.items():
    print(x, y)