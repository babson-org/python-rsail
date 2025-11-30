'''
function move_zeros(lst) that in a given list moves 0's to the end of the list.
[1,0,1,2,0,6,0,0,8] -> [1,1,2,6,8,0,0,0,0]

Part A: create and return a new list
Part B: only modify the original list
'''

#Part A:
def move_zeros(lst):
    new_lst = []
    for l in lst:
        if l != 0:
            new_lst.append(l)
            
    while len(new_lst) != len(lst):
        new_lst.append(0)

    return new_lst

#Part B:

def move_zeros2(lst):
    cur_pos = 0
    for l in lst:
        if l != 0:
            lst[cur_pos] = l
            cur_pos += 1

    while cur_pos < len(lst):
        lst[cur_pos] = 0
        cur_pos += 1

'''
square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, 
because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 
because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

'''
def square_plus(num):
    lst = []
    while num:
        digit = num % 10
        lst.append(digit)
        num = num // 10

    lst.reverse()
    
    square_plus = lst[0] ** 2
    for idx in range(1, len(lst)):

        digits = len(str(lst[idx] ** 2))        
        square_plus = square_plus * (10 ** digits) + lst[idx] ** 2        

    return square_plus

'''
Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.
'''

def first_non_repeating_letter(txt):

    for t in txt:
        cnt = 0
        for l in txt:
            if t == l:
                cnt += 1
        if cnt == 1:
            return t 
    return ''





'''
Define a class called Lamp. It will have a string attribute for color and boolean attribute, on, 
that will refer to whether the lamp is on or not. Define your class constructor with a parameter 
for color and assign on as false on initialize.

Give the lamp an instance method called toggle_switch that will switch the value of the on attribute.
Define another instance method called state that will return "The lamp is on." if it's on and "The 
lamp is off." otherwise.
'''

class Lamp:
    def __init__(self, color, on = False):
        self.color = color
        self.on = on

    def toggle_switch(self):
        self.on = not self.on

    def state(self):
        if self.on: return 'The lamp is on'
        else: return 'The lamp is off'
    

'''
Write a function that  takes an input n (integer) and returns a string that is the decimal 
representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n <= 2147483647

Examples
       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
'''

def commas(num):
    
    str_num = str(num)
    coms = len(str_num) // 3

    if coms == 0: return str_num

    str_comma = ''
    start = len(str_num) - 1
    adj = (start // 3) * 3
    for idx  in range(start , start - adj, -3):
        print(idx)
        str_comma =    "," + str_num[idx - 2:idx+1]  +  str_comma 
        
    
    str_comma = str_num[0:start - adj + 1] + str_comma
    return str_comma
print(commas(355235235))


'''
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity 
to go for a short walk. The city provides its citizens with a Walk Generating App on their phones 
-- everytime you press the button it sends you an array of one-letter strings representing directions 
to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) 
and you know it takes you one minute to traverse one city block, so create a function that will return 
true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters 
('N', 'S', 'E', or 'W' only). It will never give you an empty array (that's not a walk, that's standing still!).

For example ['N', 'E','S','W'] takes 4 minutes and gets you back to the start

'''

def cartesia(lst):
    if len(lst) != 10: return False

    n = 0
    e = 0
    s = 0
    w = 0

    for l in lst:
        l = l.upper()
        if l == 'N': n += 1
        elif l == 'E': e += 1
        elif l == 'S': s += 1
        elif l == 'W': w += 1

    if n == s and e == w : return True

    return False