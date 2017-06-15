#!/usr/share/env python
#CTF

def hex_encode(phrase):
    phrase = str.upper(phrase)

    print "[+] Starting to encode %s " % phrase

    hex_map = {
        "A":"0x41",
        "B":"0x42",
        "C":"0x43",
        "D":"0x44",
        "E":"0x45",
        "F":"0x46",
        "G":"0x47",
        "H":"0x48",
        "I":"0x49",
        "J":"0x4A",
        "K":"0x4B",
        "L":"0x4C",
        "M":"0x4D",
        "N":"0x4E",
        "O":"0x4F",
        "P":"0x50",
        "Q":"0x51",
        "R":"0x52",
        "S":"0x53",
        "T":"0x54",
        "U":"0x55",
        "V":"0x56",
        "W":"0x57",
        "X":"0x58",
        "Y":"0x59",
        "Z":"0x5A",
    }

    hex_word = ''
    word_legnth = len(phrase)
    for letter_pos in range(word_legnth):
        if phrase[letter_pos] == ' ':
            hex_word += ' '
        else:
            hex_word += hex_map[phrase[letter_pos]]

    # hex_word = hex_word.replace("x", "")
    # hex_word = hex_word.replace("0", "")

    print "[+] Phrase %s => %s " % (phrase, hex_word)


def hex_decode(phrase):
    print "[+] Starting to decode %s " % phrase

    hex_map = {
        "x41":"A",
        "x42":"B",
        "x43":"C",
        "x44":"D",
        "x45":"E",
        "x46":"F",
        "x47":"G",
        "x48":"H",
        "x49":"I",
        "x4A":"J",
        "x4B":"K",
        "x4C":"L",
        "x4D":"M",
        "x4E":"N",
        "x4F":"O",
        "x50":"P",
        "x51":"Q",
        "x52":"R",
        "x53":"S",
        "x54":"T",
        "x55":"U",
        "x56":"V",
        "x57":"W",
        "x58":"X",
        "x59":"Y",
        "x5A":"Z",
    }
    decode_phrase = ''
    arr = phrase.rsplit('0')

    for obj in arr:
        if obj == '':
            pass
        else:
            decode_phrase += hex_map[obj]

    print "[+] Phrase %s => %s " % (phrase, decode_phrase)


def main():
    method = str(raw_input("[?] Do you want to encode or decode: "))
    phrase = str(raw_input("[?] Enter phrase you want to " + method + ": "))

    if str.lower(method) == "encode":
        hex_encode(phrase)

    if str.lower(method) == "decode":
        hex_decode(phrase)


main()
