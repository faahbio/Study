questions = [
    {
        "Question": "How much is 2 + 2?",
        "Options": ["10", "22", "3", "4", "5"],
        "Answer": "4"
    },
    {
        "Question": "How much is 5 * 5?",
        "Options": ["5", "10", "55", "25", "15"],
        "Answer": "25"
    },
    {
        "Question": "How much is 10 / 2?",
        "Options": ["10", "2", "22", "102", "5"],
        "Answer": "5"
    },
]

correct_answers = 0

for question in questions:
    
    print("Question: ", question["Question"])
    print()
    
    for i, option in enumerate(question["Options"]):
        
        print( f"{i+1})", option)
        
    print()
    
    while True:
        
        guess = input("Your guess is: ")
        
        try:
            
            guess = (guess)
            
            if guess == question["Answer"]:
                
                print("You're correct! ✅")
                print()
                correct_answers += 1
        
            else:
            
                print("You're wrong! ❌")
                print()
            
            break
        
        except:
            
            print("Type only numbers!")
        
print()
print("You've had", correct_answers, "out of", len(questions[1]), "correct answers")
print()
