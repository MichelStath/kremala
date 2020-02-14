import random


pic=['''               
  ___
 |   |
 | 
 |
 | 
 | 
 |________
 |        |
 |________|
''',

'''
  ___
 |   |
 |   0
 |
 | 
 | 
 |________
 |        |
 |________|
''',

'''
  ___
 |   |
 |   0
 |   |
 | 
 | 
 |________
 |        |
 |________|
''',
'''
  ___
 |   |
 |   0
 |   |
 |   |
 | 
 |________
 |        |
 |________|
''',

'''
  ___
 |   |
 | \ 0
 |   |
 |   |
 | 
 |________
 |        |
 |________|
''',

'''
  ___
 |   |
 | \ 0 /
 |   |
 |   |
 | 
 |________
 |        |
 |________|
''',

'''
  ___
 |   |
 | \ 0 /
 |   |
 |   |
 |  /
 |________
 |        |
 |________|
''',

'''
  ___
 |   |
 | \ 0 /
 |   |
 |   |
 |  / \
 |________
 |        |
 |________|
''']

allwords=['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort','bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes','fromhex', 'hex', 'is_integer', 'fromkeys', 'get', 'items', 'keys', 'popitem', 'setdefault', 'update', 'values','capitalize', 'casefold', 'center', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
words=1
score=0
highscore=0
while True:
    hiddenword=random.choice(allwords) # ΤΥΧΑΙΑ ΕΠΙΛΟΓΗ ΛΕΞΗΣ
    letters=list(hiddenword)           # ΔΙΑΧΩΡΙΣΜΟΣ ΓΡΑΜΜΑΤΩΝ
    word=['_ ']*len(hiddenword)          # ΔΗΜΙΟΥΡΓΙΑ ΠΑΥΛΩΝ
    print(hiddenword)

    tries=0    # ΜΕΤΡΗΣΗ ΠΡΟΣΠΑΘΙΩΝ
    wrongans=0 # ΜΕΤΡΗΣΗ ΛΑΘΟΣ ΑΠΑΝΤΗΣΕΩΝ
    rightans=0 # ΜΕΤΡΗΣΗ ΣΩΣΤΩΝ ΑΠΑΝΤΗΣΕΩΝ
    guessed=[]
    print (pic[0])
    print('Word#:',words) #ΕΜΦΑΝΙΣΗ ΑΡΙΘΜΟΥ ΤΡΕΧΟΥΣΑΣ ΛΕΞΗΣ
    print('Score:',score)  #ΕΜΦΑΝΙΣΗ ΤΡΕΧΟΝΤΟΣ SCORE
    print('Highscore:',highscore) #ΕΜΦΑΝΙΣΗ HIGHSCORE
    print(''.join(word))
    print("")
    
    while wrongans<7:
            z=input('Give a letter: ')   # ΕΛΕΓΟΣ ΕΓΚΥΡΟΤΗΤΑΣ ΓΡΑΜΜΑΤΟΣ
            print("")
            x= z.lower()
            position=0
            if guessed.count(x)==1:
                print('You have already entered this letter.',end="\n\n")
                continue
            if len(x)>1:
                print('Give only one letter',end="\n\n")
                continue
            if  len(x)<1:
                print ("You didn't gave any letter",end="\n\n")
                continue
            if not x.isalpha() and x!="_":
                print("Give a character from the English alphabet or '_'",end="\n\n")
                continue
            guessed.append(x)
            guessed.sort()            
            if letters.count(x)>0:
                for i in letters:
                    if i==x:
                        word[position]=i
                    position+=1
                rightans+=1
            else:
                wrongans+=1
            guessedletters=''.join(guessed)
            finalword=''.join(word)
            print('Your word:',finalword)
            print('Guessed letters:' ,guessedletters) #ΕΜΦΑΝΙΣΗ ΟΛΩΝ ΤΩΝ ΓΡΑΜΜΑΤΩΝ
            print (pic[wrongans])  #ΕΜΦΑΝΙΣΗ ΚΡΕΜΑΛΑΣ
            print('Word#:',words) #ΕΜΦΑΝΙΣΗ ΑΡΙΘΜΟΥ ΤΡΕΧΟΥΣΑΣ ΛΕΞΗΣ
            print('Score:',score)  #ΕΜΦΑΝΙΣΗ ΤΡΕΧΟΝΤΟΣ SCORE
            print('Highscore:',highscore) #ΕΜΦΑΝΙΣΗ HIGHSCORE
            print("")
            if word.count("_ ")==0:
                score+=1                  
                break
            if wrongans==7:
                score=0
                print("You lost :(")
                print("")
    words+=1
    if score>highscore:
        highscore=score
