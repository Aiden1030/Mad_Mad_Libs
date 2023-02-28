Aiden Sanghyeop Hyun
#260974945
 
 
 
def capitalize_sentences(string):
    '''(string) -> string
 
takes a string as input containing a number
of sentences, and returns the
string with the first letter of each sentence capitalized
 
>>> capitalize_sentences("i  really understand why they \
        explain things so vaguely. so happy about it. ")
 
"I  really understand why they explain things so vaguely. \
So happy about it. "
 
>>>>>> capitalize_sentences("comp202.")
'comp202.'
 
>>>capitalize_sentences("hello. hello! hello???? hi!")
'Hello. Hello! Hello???? hi!'
 
'''
    
    empty_string = ''
    
    punctuation_list = ['!','?','.']
    
    last_letter = ''
    
    count =0
    
    new_sentence = ''
    
    final_string  = ''
    
    first_letter_count = 0
    
    same_case_word = ''
    
    #goes through letter by letter
    
    for i in string:
        
        # if the first sentence is a one letter word with an empty string and a mark. 
        
        if count == 0 and i == ' ' and last_letter in punctuation_list:
            
            same_case_word = ''
            
            empty_string += i
            
            count +=1
        
            first_letter = empty_string[0]
            
            #checks whether the first letter is a punctuation or a string
            
            while first_letter in punctuation_list or first_letter == ' ':
                
                first_letter_count += 1
                
                first_letter = empty_string[first_letter_count]
            
            #finds correct first_letter if the string didn't start with a letter
                
            if first_letter_count > 0:
                
                capitalized_sentence = empty_string[0:first_letter_count]+first_letter.capitalize() \
                                       + empty_string[first_letter_count+1:]
            
            #if not, just capitalize it
            else:
                capitalized_sentence = first_letter.capitalize() + empty_string[1+first_letter_count:]
            
            
            #add the sentence in the result
                
            final_string += capitalized_sentence
            
            #To check the last_letter in the next iteration
            last_letter = i
            
        #When it is more than two letters and not the first sentence
            
        #when the sentence starts with empty spaces or punctuation
            
        elif count > 0 and i == ' ' and last_letter in punctuation_list:
            
            same_case_word = ''
            
            new_sentence += i 
            
            #finds the first_letter using index that has been recorded
            
            first_letter = new_sentence[first_letter_count]
            
            #when it catch an invalid string
            
            while first_letter in punctuation_list or first_letter == ' ':
                
                first_letter_count += 1
                
                first_letter = new_sentence[first_letter_count]
                
            #make a capitalized sentence
                
            if first_letter_count >0:
                
                capitalized_sentence = new_sentence[0:first_letter_count]+first_letter.capitalize() \
                                       + new_sentence[first_letter_count+1:]
            
            else:
                capitalized_sentence = first_letter.capitalize() + new_sentence[1+first_letter_count:]
            
            #save and reset the values for the next iteration
                
            final_string += capitalized_sentence
            
            new_sentence =''
            
            last_letter = i
            
            first_letter_count = 0
            
        # if not a special case, record the word
        elif count > 0 :
            
            new_sentence += i
            
            last_letter = i
            
            same_case_word += i     #Here, I don't know why but if I make these into 
                                                    # one else statement the result changes
        
        else:
            
            empty_string += i
            
            last_letter = i
            
            same_case_word += i
 
            
    #if it was a one word special case:
        
    if final_string == '':
        
        len_same_case_word = len(same_case_word)
        
        return same_case_word
    
    elif final_string != '' and same_case_word != '':
        
        final_string += same_case_word
    
    return final_string
 
 
def check_punctuation_in(grid):
    '''(list)-> bool
 
checks if the list contains any punctuation mark
and return False if it doesn't
 
grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], \
["but", "they", "are", "not!", "ok,", "this"], ["one", "is."]]
 
check_punctuation_in(grid)
 
True
 
grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], \
["but", "they", "are", "not", "ok,", "this"], ["one", "is"]]
 
check_punctuation_in(grid)
 
False'''
    
    punctuation_list = ['!','?','.']
    for i in grid:
        
        for word in i:
            
            for letter in word:
                
                if letter in punctuation_list:
                    
                    return True
    return False
    
                    
 
    
    
def capitalize_sentence_grid(grid):
    '''(list)-> list
 
It takes a nested list that contains words,
capitalize the beginning of the sentence and
return the same list
 
#last sentence doesn't have a punctuation so should not be capitalized
 
>>> grid=[['hi', 'my', 'name', 'is' ,'aiden.', 'hyun.'],['hey. how are you']]
 
>>>capitalize_sentence_grid(grid)   #when it doesn't end with a punctuation mark 
 
[['Hi', 'my', 'name', 'is', 'aiden.', 'Hyun.'], ['Hey. how are you']]
 
>>> capitalize_sentence_grid(grid)     #when it does end with a punctuation mark 
 
[['Hi', 'my', 'na!me', 'Is!', 'Aiden.', 'Hyun.'], ['Hey. how are you!!']]
 
>>> grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], \
["but", "they", "are", "not!", "ok,", "this"], ["one", "is."]]
 
>>> capitalize_sentence_grid(grid)
[['You', 'might', 'think'], ['these', 'are', 'separate', 'sentences'],
['but', 'they', 'are', 'not!', 'Ok,', 'this'], ['one', 'is.']]
 
'''
    import random
    
    #deep copy the list
    
    y = []
    
    for i in grid:
        
        x=[]
        
        for obj in i:
            
            x.append(obj)
        
        y.append(x)
    
    
    new_list = []
    
    result_list = []
    
    punctuation_list = ['!','?','.']
    
    #check if the list even contains a punctuation mark
    
    if not check_punctuation_in(grid):
        
        return grid
    
    list_count = -1
    
    capitalize = 1
    
    for i in y:
        
        list_count += 1
        
        new_list = i
        
        index_count = -1
        
        for word in new_list:
            
            index_count +=1    #enumerate function inapplicable
            
            #capitalize(very first word is always)
            
            if capitalize == 1:
                
                
                first_letter = word[0]
                 
                capitalized_letter = first_letter.capitalize()
                 
                capitalized_word = capitalized_letter +word[1:]
                
                new_list[index_count] = capitalized_word
                
                last_index_count = index_count
                
                
                last_list_count = list_count
                
                #reset
                
                capitalize = 0
            
            #check whether to capitalize the next word
                
            for letter in word:
                
                if letter in punctuation_list:
                    
                    capitalize = 1
        
        #reset the string index
                    
        index_count = -1
        
        #add the word to the result list
        
        result_list += [new_list]
        
    #when it is the end of the list, but without a punctuation
    
    #capitalize here
    
    if capitalize == 0:
        
        uncapitalize  = result_list[last_list_count][last_index_count]
        
        
        the_first_letter = uncapitalize[0]
        
        uncapitalized_word = the_first_letter.lower() + uncapitalize[1:]
        
        result_list[last_list_count][last_index_count] = uncapitalized_word
        
    #return the result
 
    return result_list
                    
 
 
<strong id=line-328 class="highlight-1125964 highlight-1125965 highlight-1125969 highlight-1125971">def fill_in_madlib(mad_lib, d):
    
    '''(string, dict)-> str
 
 
>>> random.seed(9004)
>>> d = {'COLOR': ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', \
'sportscar', 'electric bike', 'starship']}
>>> fill_in_madlib("Wow! Is that a [COLOR] [VEHICLE]?", d)
'Wow! Is that a glowing green starship?'
 
 
a = {'COLOR': ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', \
'sportscar', 'electric bike', 'starship']}
fill_in_madlib("[ADJECTIVE][COLOR_1][COLOR_2]", a)
 
 
Traceback (most recent call last):
  File "/Users/aidenhyun/Desktop/winter 2022/comp 202/winter 2022/\
  comp 202 assignment 3/A3 part2/madlibs.py", line 357, in fill_in_madlib
    variable_list_len = len(mad_lib_dict[key_variable])
KeyError: 'ADJECTIVE'
 
During handling of the above exception, another exception occurred:
 
Traceback (most recent call last):
  File "<pyshell>", line 3, in <module>
  File "/Users/aidenhyun/Desktop/winter 2022/comp 202/winter 2022/co\
  mp 202 assignment 3/A3 part2/madlibs.py", line 359, in fill_in_madlib
    raise AssertionError('The madlib string is not included in the dictionary')
 
AssertionError: The madlib string is not included in the dictionary
 
 
 
>>> a = {123: ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', \
'sportscar', 'electric bike', 'starship']}
fill_in_madlib("[ADJECTIVE][COLOR_1][COLOR_2]", a)
Traceback (most recent call last):
  File "<pyshell>", line 3, in <module>
  File "/Users/aidenhyun/Desktop/winter 2022/comp 202/winter 2022\
  /comp 202 assignment 3/A3 part2/madlibs.py", line 297, in fill_in_madlib
    raise AssertionError('The values in the dictionary must be a list type')
 
AssertionError: The values in the dictionary must be a list type
 
>>> a = {123: ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', \
'sportscar', 'electric bike', 'starship']}
fill_in_madlib("[ADJECTIVE][COLOR_1][COLOR_2]", a)
Traceback (most recent call last):
  File "<pyshell>", line 3, in <module>
  File "/Users/aidenhyun/Desktop/winter 2022/comp 202/winter 2022\
  /comp 202 assignment 3/A3 part2/madlibs.py", line 297, in fill_in_madlib
    raise AssertionError('Dictionary keys must be a string')
 
AssertionError: Dictionary keys must be a string
 
>>> a = {123: ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', \
'sportscar', 'electric bike', 'starship']}
fill_in_madlib(123, a)
Traceback (most recent call last):
  File "<pyshell>", line 3, in <module>
  File "/Users/aidenhyun/Desktop/winter 2022/comp 202/winter 2022\
  /comp 202 assignment 3/A3 part2/madlibs.py", line 297, in fill_in_madlib
    raise AssertionError('The first parameter must be a string type')
 
AssertionError: The first parameter must be a string type
 
>>> a = {123: ['yellow', 'glowing green', 'red'], 'VEHICLE': []}
fill_in_madlib("[ADJECTIVE][COLOR_1][COLOR_2]", a)
Traceback (most recent call last):
  File "<pyshell>", line 3, in <module>
  File "/Users/aidenhyun/Desktop/winter 2022/comp 202/winter 2022\
  /comp 202 assignment 3/A3 part2/madlibs.py", line 297, in fill_in_madlib
    raise AssertionError(Dictionary key ',key,' contains an empty list)
 
AssertionError: Dictionary key ',key,' contains an empty list
>>> 
'''
    import random
    
    for key in d:
        
        if type(key) != type(str()):
            print(type(key))
            
            raise AssertionError('Dictionary keys must be a string')
        
        if type(d[key]) != type(list()):
            
            raise AssertionError('The values in the dictionary must be a list type')
        
        if len(d[key]) == 0:
            
            raise AssertionError('Dictionary key ',key,' contains an empty list')
            
    if type(mad_lib) != type(str()):
        
        raise AssertionError('The first parameter must be a string type')
        
    if '[' not in mad_lib or ']' not in mad_lib:
        
        raise AssertionError('The string does not have a madlib string')
 
    variable_list = []
    used_word_list = []
    new_string = ''
    record = 0
    result = mad_lib
    mad_lib_dict = d
    
    #goes through the string and a madlib blank
    #comes up starts recording the word
    
    for i in mad_lib:
        
        if record == 1 and i != ']':
            new_string += i
        
        if i == '[':
            record = 1
            new_string = i
        elif i ==']':
            new_string += i
            record = 0
            variable_list += [new_string]
            
    
    last_key_variable = 'last_key_variable'
    
    # goes through the dictionary keys
    
    for a in variable_list:
        
        #strip extra numbers and brackets
        
        key_variable = a.strip('1234567890][_')
        
        #look up dictionary and randomly choose a word
        
        last_key_variable = key_variable
        
        #raises a keyError if madlib does not exists
        
        try:
            
            variable_list_len = len(mad_lib_dict[key_variable])
        
        except KeyError:
            
            raise AssertionError('The madlib string is not included in the dictionary')
        
        
            
        while 1==1:
            
            randomly_chosen_word = random.choice(mad_lib_dict[key_variable])
            
            #Since the same word cannot be used, record them and skips
            
            if randomly_chosen_word not in used_word_list:
                
                used_word_list += [randomly_chosen_word]
                
                result = result.replace(a, randomly_chosen_word)
                
                break
        
        
            
    
    return result
                
 
        
        
        
def load_and_process_madlib(filename):
    ''' (string) -> none
 
It takes a name of file and fill in the madlib words
from the given dictionary "word_dict.pkl".
 
>>> random.seed(2022)
>>> load_and_process_madlib('madlib1.txt')
>>> f = open('madlib1_filled.txt', 'r')
>>> s = f.read()
>>> s
'Once upon a midnight dreamy, while I pondered, weak and dreamy,'
 
 
>>> load_and_process_madlib('madlib1.txt')
>>> f = open('madlib1_filled.txt', 'r')
>>> s = f.read()
>>> s
'Once upon a midnight weary, while I snoozled, lazy and starry,'
 
 
>>> load_and_process_madlib('madlib1.txt')
>>> f = open('madlib1_filled.txt', 'r')
>>> s = f.read()
>>> s
'Once upon a midnight lazy, while I studied, starry and dreamy,'
'''
    
    import pickle
    
    #import the dictionary and sentences
    
    madlib_file_r = open(filename, 'r')
    
    madlib_text = madlib_file_r.read()
    
    madlib_file_r.close()
    
    dict_file_rb = open('word_dict.pkl', 'rb')
    
    d = pickle.load(dict_file_rb)
    
    dict_file_rb.close() 
    
    #fill in the empty words
    
    filled_text = fill_in_madlib(madlib_text, d)
    
    #erase that ".txt" and add a new name in a new file
    
    file_name = filename[0:-4]
    
    new_file_w = open(file_name+'_filled.txt', 'w')
    
    new_file_w.write(filled_text)
    
    new_file_w.close()
 
 
 
def generate_comment():
    ''' () -> string
It takes no input and returns the text in
madlibk.txt where the number k is randomly
chosen.
 
generate_comment():
 
I saw the-president last night and the-president was so kind.
I changed my mind to love the-president instead.
 
generate_comment():
 
I don't see anyone qualified in the list. The-candidate is inadequate,
Bug-er is worse,the-president is unsatisfactory,Thonny is overrated and bad.
 
generate_comment():
 
Thonny is genius but The-candidate is overrated, although my dad like
The-candidate. So they awesomeeee!!!! pick on Thonny.  DON'T go The-candidate!
 
'''
    
    import random
    
    #randomly choose a script
    
    k = random.randint(1,10)
    
    filename = 'madlib'+str(k)+'.txt'
    
    load_and_process_madlib(filename)
    
    #open, fill the words and return the text
    
    f_filled = open('madlib'+str(k)+'_filled.txt', 'r')
    
    f_filled_text = f_filled.read()
    
    f_filled.close()
    
    return f_filled_text
    
    
    
 
