'''
Viachaslau Kalatsei
Date: July6th, 2015
The program calculate the total 
number of times each word has been tweeted.
'''


def tweeted_words():
    dictionary={}  #set up an empty dictionary
    read_file=open(r'tweet_input\tweets.txt','r')  # program open the text file for reading later and assign to the object
    write_file=open(r'tweet_output\ft1.txt','w')   # set up object(write_file) for writing to the text file
    text=read_file.read() # all what the object read from the text file assign to the object "text"
    words=text.split() # separate text into words by space delimiter
    
    
    for input_word in words: # looping through words
        if input_word not in dictionary: # if word is not in the dictionary
            dictionary[input_word]=1     # assign value 1 to the word(key)
        else:
            dictionary[input_word]+=1    # if a word already in dictionary then increment value by 1   

    wordsList=[(v,k) for v, k in dictionary.items()] # 'transfer' dictionary to list
    wordsList.sort() # sort the list by word (which is key) in alphabetic order 
    for word in wordsList:  # looping through list  
        write_file.write("%25s:%4d"%(word[0],word[1])+'\n')  # write output to the text file in formated order 
                                                             #(first key(word) and then his  value)
    write_file.close()    # close text file for writing 
    read_file.close()     # close text file for reading
    
    
        
tweeted_words() # initiate program run
