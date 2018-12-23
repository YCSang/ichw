"""wcount.py: count words from an Internet file.

__author__ = 'Sang'
__pkuid__  = '1600017765'
__email__  = 'johnbirdsang@pku.edu.cn'
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    words = []
    counts = []
    wordtotal = lines.split()
    for w in wordtotal:
        word = ''.join(e for e in w if e.isalnum() or e in ["'",'-'])
        word = word.lower()
        if word not in words:
            words.append(word)
            counts.append(1)
        elif word in words:
            index = words.index(word)
            counts[index] += 1

    result = []
    for i in range(topn):
        maxindex = counts.index(max(counts))
        result.append((words.pop(maxindex), counts.pop(maxindex)))        
    return result

def u_open(doc):
    """Open the text link given.
    """
    docstr = doc.read().decode()
    doc.close()
    return docstr

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    elif len(sys.argv) > 3:
        print('ERROR: Too many parameters.\n')
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
        
    else:
        try:
            doc = urlopen(sys.argv[1])
        except:
            print('ERROR: The URL is wrong.\n')
            print('Usage: {} url [topn]'.format(sys.argv[0]))
            print('  url: URL of the txt file to analyze ')
            print('  topn: how many (words count) to output. If not given, will output top 10 words')
            sys.exit(0)

        if len(sys.argv) == 2:
            result = wcount(u_open(doc))
            print('Result:')
            print('-WORD-\t-COUNT-')
            for wc in result:
                print(wc[0], '\t', wc[1])
            sys.exit(1)

        elif len(sys.argv) == 3:
            result = wcount(u_open(doc), int(sys.argv[2]))
            print('Result:')
            print('-WORD-\t-COUNT-')
            for wc in result:
                print(wc[0], '\t', wc[1])
            sys.exit(1)
