#First accepting the string
str= input('Please enter a string ')
def most_frequent(string):
   #now using dictionary function 
    a = dict()
    for key in string:
      #now giving the condition
        if key not in a:
            a[key] = 1
        else:
            a[key] += 1
            #returning the value
    return a

print (most_frequent(str))
