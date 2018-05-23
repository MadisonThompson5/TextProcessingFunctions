import fileinput
import sys
import tokenize
import time
import StringIO

##returns filename from command line
def getFile():
    file_name = sys.argv[-1]
    return file_name

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


def main():
    results= {}
    sorter= []
    file_name = getFile()
    while True:
        try:
            if( file_name.endswith('.txt')):
                file = open(file_name,'r')
                break
            else:
                print('File type must be .txt')
                raise IOError
        except IOError:
            print ('Error opening file')
            file_name = str(raw_input('Enter valid file: '))
    results = tokens(file)
    sorter= sorted(results.items(),key=lambda x: (-x[1],x[0]))
    for x in sorter:
        print (x[0] +' - ' +str( x[1]) )
        file.close()
 
    
  
if __name__== "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    ##runs in linear time -> time doubles as input doubles
    ##124,961 words runs in ~0.5s
    ## 249,922 words runs in ~0.9s
    ##without error handling (longer because waits for user to re-input a file name)

    


  
