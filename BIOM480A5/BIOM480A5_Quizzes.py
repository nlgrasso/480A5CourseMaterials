import random
from IPython.display import clear_output
import time
def multiple_choice(optionsDict, questionTemplate, action, num2win):
    tryagain = True
    # clear text from output and print the next question.
    num_correct = 0

    while tryagain:
        clear_output(wait=True)

        answers = list(set(optionsDict.values()))
        var = random.choice(list(optionsDict.keys()))
        type_var = optionsDict[var]
        
        question = questionTemplate.replace('XXX', var)
        print(question)

        options = random.sample(answers, 5)
        options.append(type_var)
        random.shuffle(options)
        options = list(set(options))

        for i in range(len(options)):
            print(f"{i}: {options[i]}")
        
        answer = None
        while not answer:
            answer = input(f"Choose the correct answer (0-{len(options)-1}). If you want to quit, type 'q': ")
            if answer == 'q':
                print(f"You answered {num_correct} questions correctly. Goodbye!") 
                tryagain = False
                return
            if not answer.isdigit() or int(answer) not in range(len(options)):
                print(f"Please enter a number between 0 and {len(options)-1}.")
                answer = None
        if options[int(answer)] == type_var:
            num_correct += 1
            print(f"Yay - good job! You have {num_correct} correct answers. Get {num2win} correct answers to win the game.")
            if num_correct >= num2win:
                print('\nYou won the game!\n')
                print(action)
                print('\nPlease keep going if you want to practice more.')

        else:
            print(f"I'm sorry, the correct answer is {type_var}")

        time.sleep(1)
        tryagain = input("Do you want to try again? ([y]/n): ") != 'n'
    print("Goodbye!")

def multiple_choice_quiz(quizName):
    match quizName.lower():
        case "types":
            optionsDict = {'A = 1':'int', 'B = 2.0':'float', 'C = "3"':'string', 'D = True':'bool', 'E = [1,2,3]':'list',  'F = (1,2,3)':'tuple', 'G = {1,2,3}':'set', 'H = {"a":1,"b":2,"c":3}':'dict', 'I = None':'NoneType', 'J = 1+2j':'complex', 
                    'K = 1.3':'float', 'L = 5-2j':'complex', 'M = {1:2, 3:4}':'dict', "N = {'a','b','c'}":'set', 'O = "hello"':'string', "P = ['x','y','z']":'list', "Q = ('q','r','s')":'tuple', 'R = False':'bool', 'S = None':'NoneType'}
            question = "What is the type of the following variable: XXX ?"
            action = "You got 5 right - place your left hand on your head."
            num2win = 5
        case "slicing":
            question = "How would you index or slice the the list 'x' to get XXX ?"
            optionsDict = {'the first element':'x[0]', 
                        'the last element':'x[-1]', 
                        'a list with the first 3 elements':'x[:3]', 
                        'a list with the last 3 elements':'x[-3:]', 
                        'a list with the second to the fourth element':'x[1:4]', 
                        'a list with the second to the last element':'x[1:-1]', 
                        'a list with the first element and the last element':'[x[0], x[-1]]', 
                        'a list with the last element and the second to the last element':'x[-1], x[-2]', 
                        'a list with the first 3 elements and the last 3 elements':'[x[:3], x[-3:]]', 
                        'a list with every third element starting with the first element':'x[::3]',
                        'a list with every third element starting with the second element':'x[1::3]',
                        'a reversed list with every third element starting with the last element':'x[-1::-3]',
                        'a list of every string in the list that has the letter "a"':'[i for i in x if "a" in i]',
                        'a list of every string in the list that has the letter "a" in the second position':'[i for i in x if len(i)>1 and i[1]=="a"]'}
            action = "You got 8 right - touch your nose with your right hand."
            num2win = 8
        case "list_operations":
            question = "Which command would you use to perform the following operation on the lists x, y and z:\n XXX ?"
            optionsDict = {'concatenate the lists to form a longer list':'x + y + z',
                        'repeat the list x 5 times':'x*5',
                        'remove repeated elements from the list x':'list(set(x))',
                        'sort the list x':'sorted(x)',
                        'reverse the list x':'x[::-1]',
                        'add the element 5 to the end of the list x':'x.append(5)',
                        'remove the first element from the list x':'x.pop(0)',
                        'sum the elements of the list x':'sum(x)',
                        "find the first index of the element 'abc' in the list x":'x.index("abc")',
                        'count the number of times the element 5 appears in the list x':'x.count(5)',
                        'create a new list with the summed elements of the lists x and y':'[i+j for i,j in zip(x,y)]',
                        'create a tuple with the elements of the list x':'tuple(x)',
                        'create a set with the elements of the list x':'set(x)',
                        'create a dictionary with the elements of the list x':'dict(enumerate(x))',
                        'find the intersection of the lists x and y':'list(set(x) & set(y))',
                        'find the union of the lists x and y':'list(set(x) | set(y))',
                        'find the difference of the lists x and y':'list(set(x) - set(y))',
                        'find the symmetric difference of the lists x and y':'list(set(x) ^ set(y))',
                        'check if the element 5 is in the list x':'if 5 in x',
                        'check if the element 5 is not in the list x':'if 5 not in x',
                        'check if the list x is empty':'if not x',
                        'check if the list x is not empty':'if x',
                        'check if the list x is equal to the list y':'if x==y',
                        'check if the list x is not equal to the list y':'if x!=y',
                        'check if maxiumum element of the list x is greater than 5':'if max(x)>5',
                        'check if minimum element of the list x is less than 5':'if min(x)<5',
                        'check if all elements of the list x are greater than 5':'if all(i>5 for i in x)',
                        'check if any element of the list x is greater than 5':'if any(i>5 for i in x)',
                        'check if all elements of the list x are strings':'if all(isinstance(i, str) for i in x)',
                        'check if any element of the list x is a string':'if any(isinstance(i, str) for i in x)',
                        'check if all elements of the list x are unique':'if len(x)==len(set(x))'}  
            action = "You got 12 right - look up and smile."
            num2win = 12
            
        case "dictionary_operations":
            question = "Which command would you use to perform the following operation on the lists X, Y, and Z dictionaries a, b and c:\n XXX ?"  
            optionsDict = {'create a new dictionary called using X as the keys and Y as the values':'a = dict(zip(X,Y))',
                        'extract the value of the key "abc" from the dictionary a':'a["abc"]',
                        'add the key "abc" with the value 5 to the dictionary a':'a["abc"] = 5',
                        'remove the key "abc" from the dictionary a':'a.pop("abc")',
                        'remove all elements from the dictionary a':'a.clear()',
                        'create a subset of the dictionary a with the keys in the list X':'{k:a[k] for k in X}',
                        'create a subset of the dictionary a with the values in the list Y':'{k:v for k,v in a.items() if v in Y}',
                        'create a subset of the dictionary a with the keys that contain the letter "a"':'{k:v for k,v in a.items() if "a" in k}',
                        'create a subset of the dictionary a with the values that are greater than 5':'{k:v for k,v in a.items() if v>5}',
                        'get a list of all the keys in the dictionary a':'list(a.keys())',
                        'get a list of all the values in the dictionary a':'list(a.values())',
                        'get a list of all unique values in the dictionary a':'list(set(a.values()))',
                        'get a list of all key-value pairs in the dictionary a':'list(a.items())',
                        'check if the key "abc" is in the dictionary a':'if "abc" in a',
                        'check if the key "abc" is not in the dictionary a':'if "abc" not in a',
                        'check if the value 5 is in the dictionary a':'if 5 in a.values()',
                        'check if the value 5 is not in the dictionary a':'if 5 not in a.values()',
                        'check if the dictionary a is empty':'if not a',
                        'check if the dictionary a is not empty':'if a',
                        'check if the dictionary a is equal to the dictionary b':'if a==b',
                        'check if the dictionary a is not equal to the dictionary b':'if a!=b',
                        'check if the dictionary a has the key "abc"':'if "abc" in a.keys()',
                        'check how many key-value pairs are in the dictionary a':'len(a)'}
            num2win = 10            
            action = f"You got 10 right - cough three times."

                        
        case "string_operations":
            question = "Which command would you use to perform the following operation on the strings X and/or Y:\n XXX ?"
            optionsDict = {'get the first character of the string X':'X[0]',
                        'get the last character of the string X':'X[-1]',
                        'get the first 3 characters of the string X':'X[:3]',
                        'get the last 3 characters of the string X':'X[-3:]',
                        'split the string X into a list of words separaed by spaces':'X.split()',
                        'split the string X into a list of phrases separated by commas':'X.split(",")',
                        'split the string X into a list of characters':'list(X)',
                        'join the a list Y containing words into a single string separated by spaces':'" ".join(Z)',
                        'join the a list Y containing words into a single string separated by commas':'",".join(Z)',
                        'concatenate the strings X and Y':'X + Y',
                        'count the number of times the letter "a" appears in the string X':'X.count("a")',
                        'change the string X to uppercase':'X.upper()',
                        'change the string X to lowercase':'X.lower()',
                        'change an integer x to a string':'str(x)',
                        'change a string x to an integer':'int(x)',
                        'change a string x to a float':'float(x)',
                        'count how many times the letters "aa" appear in the string X':'sum(1 for i in range(len(X)-1) if X[i:i+2]=="aa")',
                        'replace the letter "a" with the letter "b" in the string X':'X.replace("a","b")',
                        'check if the string X is equal to the string Y':'if X==Y',
                        'check if the string X is not equal to the string Y':'if X!=Y',
                        'check if the string X is in the string Y':'if X in Y',
                        'check if the string X is not in the string Y':'if X not in Y',
                        'check if the string X is empty':'if not X',
                        'check if the string X is not empty':'if X',
                        'check if the string X is a palindrome':'if X==X[::-1]',
                        'flip the order of the words in the string X':'" ".join(X.split()[::-1])',
                        'get a list of all unique words in the string X':'list(set(X.split()))',
                        'get the length of the string X':'len(X)',
                        'get the length of the string X without counting spaces':'len(X.replace(" ",""))',
                        'create a random string of length 10':'"".join(random.choices(string.ascii_letters + string.digits, k=10))',
                        'create a random string of length 10 with only letters':'"".join(random.choices(string.ascii_letters, k=10))'}
            action = "You got 15 right - knock twice on the table."
            num2win = 15
        case _:
            print("Quiz not found")
            return
    multiple_choice(optionsDict, question, action, num2win)
