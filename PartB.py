import fileinput
import sys
import tokenize
import time
import StringIO

##returns filenames from command line
def getFile():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[-1]
    return file_name1, file_name2
##counts the current ammount of tokens and stores in a dictionary
def countTokens(tokens, token_dict ):
    for t in tokens:
        if t in token_dict:
            token_dict[t] += 1
        else:
            token_dict[t] =1
    return token_dict

##tokenizes lines using tokenize python2 library
def tokens(file):
    results = []
    token_dict = {}
    for line in file:
        try:
            tokens  = tokenize.generate_tokens(StringIO.StringIO(line).readline)
            for toknum,tokval,_,_,_ in tokens: ## code used from https://docs.python.org/2/library/tokenize.html
                tokval = tokval.lower()
                if( toknum ==1 ):
                    results.append(tokval)
                    if( len(results) > 500): ## moves tokens to a dictionary to handle large input
                        token_dict = countTokens(results, token_dict)
                        del results[:]
        except tokenize.TokenError:
            pass
            
    return countTokens(results, token_dict)

            
def count_intersections(results1, results2):
    count = 0
    for tokval in results1.keys():
        if ( tokval in results2.keys()):
             count +=1
    return count


def main():
    results1= {}
    results2= {}

    sorter1= []
    sorter2= []

    file_name1, file_name2 = getFile()
    while True:
        try:
            if( file_name1.endswith('.txt') & file_name2.endswith('.txt')):
                file1 = open(file_name1,'r')
                file2 = open(file_name2,'r')
                break
            else:
                print('File type must be .txt')
                raise IOError
        except IOError:
            print ('Error opening file')
            file_name1 = str(raw_input('Enter valid file 1: '))
            file_name2 = str(raw_input('Enter valid file 2: '))

  
    results1 = tokens(file1)
    results2 = tokens(file2)
    count = count_intersections(results1, results2)
    print (count)
 
    file1.close()
    file2.close()
    
  
if __name__== "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    ##runs in linear time -> time doubles as inout doubles
    ##1st input file: 124,961 words 2nd input file:78,213 words runs in ~1.8s
    ## 1st inout file: 249,922 words 2nd input file: 156,426 words runs in ~2.5s
    ##without error handling (longer because waits for user to re-input a file name)


    
