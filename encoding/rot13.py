#!/bin/usr/env python

def rot13_encode(phrase):
    phrase = str.lower(phrase)
    print  "[+] Start to encode '" + phrase + "'"

    cipher_map = {'a':'N', 'b':'O', 'c':'P', 'd':'Q', 'e':'R', 'f':'S', 'g':'T', 'h':'U', 'i':'V', 'j':'W', 'k':'X', 'l':'Y', 
    'm':'Z', 'n':'A', 'o':'B', 'p':'C', 'q':'D', 'r':'E', 's':'F', 't':'G', 'u':'H', 'v':'I', 'w':'J', 'x':'K', 'y':'L', 'z':'M'}

    cipher_word = ""

    for letter in range(len(phrase)):    
        if ' ' in phrase[letter]:
            cipher_word += ' '
        else:
            cipher_word += cipher_map[phrase[letter]]
    print "[+] Phrase '%s' => '%s' " % (phrase,cipher_word)

def rot13_decode(phrase):
    phrase = str.upper(phrase)
    print  "[+]  Starting to decode '"+ phrase +"'"

    cipher_map = {'N':'a', 'O':'b', 'P':'c', 'Q':'d', 'R':'e', 'S':'f', 'T':'g', 'U':'h', 'V':'i', 'W':'j', 'X':'k', 'Y':'l', 
    'Z':'m', 'A':'n', 'B':'o', 'C':'p', 'D':'q', 'E':'r', 'F':'s', 'G':'t', 'H':'u', 'I':'v', 'J':'w', 'K':'x', 'L':'y', 'M':'z'}
    
    word_dec = ""

    for letter in range(len(phrase)):
        if ' ' in phrase[letter]:
            word_dec += ' '
        else:
            word_dec += cipher_map[phrase[letter]]    
    print "[+] Phrase '%s' => '%s' " % (phrase,word_dec)


def main():
    method = str(raw_input("[?] Do you wnat encode or decode? "))
    phrase = str(raw_input("[+] Enter the phrase You want to " + method + ": "))

    if method == "encode":
        rot13_encode(phrase)

    elif method == "decode":
        rot13_decode(phrase)
    
if __name__ == '__main__':
    main()