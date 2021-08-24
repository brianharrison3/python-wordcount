#open
def print_word_freq(file):
    file = open(file)
    lines = file.read().replace('\n', ' ')
#lowercase
    lines = lines.lower()
#replace punctution
    punctuation = ['.' , ',' , ':', "'" , '"']
    for occurance in punctuation:
        lines = lines.replace(occurance,"")
#replace stop words
    STOP_WORDS = [
    '—', ' an ', ' and ', ' are ', ' as ', ' at ', ' be ', ' by ', ' for ', ' from ', ' has ', ' he ',
    ' i ', ' in ', ' is ', ' it ', ' its ', ' of ', ' on ', ' that ', ' the ', ' to ', ' were ',
    ' will ' , ' with ' , ' a ' ]
    for word in STOP_WORDS:
        lines = lines.replace(word," ")
    #print(lines)
#string into list
    def Convert(text):
        list_poem = text.split(" ")
        return list_poem 
    lines = Convert(lines)
    #print(lines)
#wordcount empty dic
    wordcount = {};
#get rid of empty spaces
    empty = [" ", '', '']
    for word in lines:
        if word in empty:
            lines.remove(word)
#counts single words 
    for single_word in lines: 
        wordcount[single_word] = wordcount.get(single_word, 0) + 1
        
#printing
    sorted_wordcount = sorted(wordcount.items(), key=lambda seq: seq[1], reverse=True)
    for x in sorted_wordcount:
        print(x[0], x[1], "*"*(x[1]))

    








    #for single_word in wordcount:
        #output = (single_word, wordcount[single_word])
        #print(sorted(output))
    
        #print(wordcount[single_word], single_word)

  

#int
    print(type(wordcount[single_word]))
        



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

