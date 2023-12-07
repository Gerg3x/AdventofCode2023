####    PART 1    ####

#Import the txt file
text = open("AdventofCode_ex1.txt", "r")
#We need to extract the first and last number of each line
#Then save it and sum it to the next number of next line and so on
count = 0 #The sum will be saved in count

for line in text:
    x = list()
    for s in line:
        if s.isdigit():
            x.append(s)
    print(x)
    #if len(x) > 1:
    primero = x[0]
    segundo = x[-1]
    total = primero + segundo
    total_num = float(total)
    count = count + total_num
    print(primero, segundo, count)
    #else:
     #   primero = x[0]
      #  total = primero
       # total_num = float(total)
        #count = count + total_num
        #print(primero, count)
print(count)


####    PART 2    ####

#Import the txt file
text = open("AdventofCode_ex1.txt", "r")
data = []
for line in text:
    if "one" or "two" or "three" or "four" or "five" or "six" or "seven" or "eight" or "nine" in line:
        line_one = line.replace("one", "o1ne")
        line_two = line_one.replace("two", "t2wo")
        line_three = line_two.replace("three", "t3hree")
        line_four = line_three.replace("four", "f4our")
        line_five = line_four.replace("five", "f5ive")
        line_six = line_five.replace("six", "s6ix")
        line_seven = line_six.replace("seven", "s7even")
        line_eight = line_seven.replace("eight", "e8ight")
        line_nine = line_eight.replace("nine", "n9ine")
        data.append(line_nine)
    else:
        data.append(line)

#data_fixed = "".join(data) #Data corrected with numbers into a text
#print(data_fixed)

#### After we converted it, we performed the calculations as Part 1
count = 0 #The sum will be saved in count

for line in data:
    x = list()
    for s in line:
        if s.isdigit():
            x.append(s)
    primero = x[0]
    segundo = x[-1]
    total = primero + segundo
    total_num = float(total)
    count = count + total_num
    print(primero, segundo, count)
print(count)
