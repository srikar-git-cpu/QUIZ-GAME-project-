score = 0

print("question1: what is capital of india")
answer1 = input("your answer: ")
if answer1.lower() == "new delhi" :
    print("correct")
    score += 1
else :
    print("wrong")
    
print("question2: what is national bird")
answer2 = input("your answer: ")
if answer2.lower() == "peacock" :
    print("correct")
    score += 1
else:
    print("wrong")

print('question3: what is national tree')
answer3 = input("your answer: ")
if answer3.lower() == "banyan tree" :
    print("correct")
    score += 1
else : 
    print("wrong")

print("your score is" , score , "out of 3")


