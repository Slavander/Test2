'''
Viachaslau Kalatsei
Date: July5th, 2015
The program calculate the median number 
of unique words per tweet, and updates 
this median as tweets come in.
'''
def unique_words():
    summary=0
    tweet_count=0
    Grand_Sum=0.0
    words_dict={}  #set up an empty dictionary
    read_file=open(r'tweet_input\tweets.txt','r') # open file for reading
    write_file=open(r'tweet_output\ft2.txt','w')  # open file for writing
    line_text=read_file.readlines() # read lines from the read file and holds all lines in the "line_text" object
    
    for line in line_text: # looping through lines
        for words in line.split(): # looping through each line and holds all words of the current line in the object "words" 
            if words not in words_dict: # looking for unique words
                    summary+=1 # collect unique words in each tweet
                    words_dict[words]=1 # fill up dictionary by unique words
        tweet_count+=1 # keep tracking of the tweets number
        Grand_Sum+=summary # collect all unique words
        write_file.write('%3.1f'%(Grand_Sum/tweet_count)+'\n')  #write the median number after each tweet in the file
        summary=0         # clean up the number of unique words of current tweet
        words_dict={}     # clean up current tweet dictionary of unique words
    write_file.close()    # close text file for writing 
    read_file.close()     # close text file for reading 
    
    
        
unique_words() # initiate program run