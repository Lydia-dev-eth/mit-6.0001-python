# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    list_of_text=[]
    word="" # a word i can add to the list
    for char in input_text:
        if char in ("\n" ,'\r'," "):
            if word!= "":
                list_of_text.append(word)
                word=""
        else:
            word+=char
    if word!= "":
        list_of_text.append(word)

    return list_of_text 


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    dictionary_freq={} # the frequency of each word 
    for word in input_iterable:
        if word in dictionary_freq:
            dictionary_freq[word]+=1
        else:
            dictionary_freq[word]=1
    return dictionary_freq


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    dictionary_freq={} # the frequency of each word 
    for char in word:
        if char in dictionary_freq:
            dictionary_freq[char]+=1
        else:
            dictionary_freq[char]=1
    return dictionary_freq

    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    pass


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    list_of_all_keys=[]
    for key in freq_dict1:
        if key not in list_of_all_keys:
            list_of_all_keys.append(key)
    for key in freq_dict2:
        if key not in list_of_all_keys:
            list_of_all_keys.append(key)  
    
    count_e_in_L1=0
    count_e_in_L2=0
    delta_e=0
    sigma_e=0

    for e in list_of_all_keys:
        if e in freq_dict1:
            count_e_in_L1=freq_dict1[e] 
        else:
            count_e_in_L1=0

        if e in freq_dict2:
            count_e_in_L2=freq_dict2[e]
        else:
            count_e_in_L2=0
        delta_e += abs(count_e_in_L1-count_e_in_L2) 
        sigma_e += abs(count_e_in_L1+count_e_in_L2)        
    similarity= 1-(delta_e/sigma_e)
    return round(similarity,2)



### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    list_of_all_keys=[]
    for key in freq_dict1:
        if key not in list_of_all_keys:
            list_of_all_keys.append(key)
    for key in freq_dict2:
        if key not in list_of_all_keys:
            list_of_all_keys.append(key)
    list_most_freq=[]
    max_value1=0
    max_value2=0
    word1="" 
    word2=""
    
     
    for key in list_of_all_keys:
        if key in freq_dict1:
            if  freq_dict1[key]> max_value1:
                max_value1= freq_dict1[key]
                word1= key  
        if key in freq_dict2:
            if  freq_dict2[key]> max_value2:
                max_value2= freq_dict2[key]
                word2=key
    if freq_dict2[word2] > freq_dict1[word1]:
        list_most_freq.append(word2)
    elif  freq_dict2[word2] < freq_dict1[word1]:
        list_most_freq.append(word1) 
    else:
        list_most_freq.extend([word1,word2])
    return list_most_freq   


          

     


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    text=load_file(file_path)
    list_text=text_to_list(text)
    dic_freq=get_frequencies(list_text)
    total_num_words= sum(dic_freq.values())
    for key in dic_freq:
        TP= dic_freq[key]/total_num_words
        dic_freq[key]=TP
    return dic_freq
        





def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    list_documents=[]
    
    for  files in file_paths:
        text=load_file(files)
        list_text=text_to_list(text)
        list_documents.append(list_text)
    
    n=len(list_documents)
    expand=[]
    dictionary={}
    for list1 in list_documents:
        expand.extend(list1)
    uniq_list=[]  # i want to get the unique words that can exist in every document

    for word in expand:
        if  word not in uniq_list:
            uniq_list.append(word)
    for word in uniq_list:
        count=0
        for file in list_documents:
            if word in file:
                count+=1
        
        
        IDF= math.log10(n/count)
        if count==0:
            IDF = 0.0
        
        
    
        dictionary[word]=IDF
    return dictionary    
    
        


    

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    TF_dic=  get_tf(tf_file_path)
    IDF_dic= get_idf( idf_file_paths)
    tdidf={}
    for key in TF_dic:
        tfidf= TF_dic[key] * IDF_dic[key]
        tdidf[key]=tfidf
    sorted_valu= sorted(tdidf.items(), key=lambda item: (item[1], item[0]))
    return sorted_valu  

    


if __name__ == "__main__":
     
     ###############################################################
     ## Uncomment the following lines to test your implementation ##
     ###############################################################

     ## Tests Problem 0: Prep Data
     test_directory = "tests/student_tests/"
     hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
     world, friend = text_to_list(hello_world), text_to_list(hello_friend)
     print(world)      # should print ['hello', 'world', 'hello']
     print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
     test_directory = "tests/student_tests/"
     hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
     world, friend = text_to_list(hello_world), text_to_list(hello_friend)
     world_word_freq = get_frequencies(world)
     friend_word_freq = get_frequencies(friend)
     print(world_word_freq)    # should print {'hello': 2, 'world': 1}
     print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
     freq1 = get_letter_frequencies('hello')
     freq2 = get_letter_frequencies('that')
     print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
     print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
     test_directory = "tests/student_tests/"
     hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
     world, friend = text_to_list(hello_world), text_to_list(hello_friend)
     world_word_freq = get_frequencies(world)
     friend_word_freq = get_frequencies(friend)
     word1_freq = get_letter_frequencies('toes')
     word2_freq = get_letter_frequencies('that')
     word3_freq = get_frequencies('nah')
     word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
     word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
     word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
     word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
     print(word_similarity1)       # should print 1.0
     print(word_similarity2)       # should print 0.25
     print(word_similarity3)       # should print 0.0
     print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
     freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
     most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
     print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
     tf_text_file = 'tests/student_tests/hello_world.txt'
     idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
     tf = get_tf(tf_text_file)
     idf = get_idf(idf_text_files)
     tf_idf = get_tfidf(tf_text_file, idf_text_files)
     print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
     print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
     print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
