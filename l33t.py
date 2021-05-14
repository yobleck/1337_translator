#https://en.wikipedia.org/wiki/Leet
#https://stackoverflow.com/questions/9090079/in-python-how-to-import-filename-starts-with-a-number
dic = { #[easy,med,hard]
    "A":["4","@","/-\\"],
    "B":["B","13","|3"],
    "C":["C","(","<"],
    "D":["D","[)","I>"],
    "E":["3","[-","|=-"],
    "F":["F","ph","|="],
    "G":["G","9","6"],
    "H":["H","|-|","#"],
    "I":["I","!","|"],
    "J":["J",".]","_)"],
    "K":["K","|<","|{"],
    "L":["1","[","|_"],
    "M":["M","|Y|","//\\\\//\\\\"],
    "N":["N","/V","|\\|"],
    "O":["0","()","{}"],
    "P":["P","|>","|*"],
    "Q":["Q","0,","(_,)"],
    "R":["R","|2","|?"],
    "S":["$","5","z"],
    "T":["7","+","-|-"],
    "U":["U","[_]","\\_/"],
    "V":["V","\\/","\\\\//"],
    "W":["W","\\v/","\\/\\/"],
    "X":["X","><","}{"],
    "Y":["Y","j","'/"],
    "Z":["Z","2","7_"],
    "ck":["X"],
    };
#TODO:
#randomly remove some vowels
#flip some vowel consonant pairs
#suffix = ["xor","age","ness","ed","z"];

def eng_to_1337(text, dif=0):
    out = "";
    for x in text:
        if x.upper() in dic:
            out += dic[x.upper()][dif];
        else:
            out += x;
    return out;

#TODO: def 1337_to_eng():

""" TODO: run from cmd
if __name__ == "__main__":
    eng_to_1337();
"""
