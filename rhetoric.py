#!/usr/bin/python3
import sys
import textwrap

from json import load
from random import choice
#from align import *
#from termcolor import *

class Rhetoric:
    def __init__(self):
        rf = open('rhetoric.json', 'r')
        self.rhetoric = load(rf)
        rf.close()

    def term(self, term = ''):
        if not term:
            term = choice(list(self.rhetoric.keys()))
        gloss = self.rhetoric[term][0]
        try:
            example = self.rhetoric[term][1:]
        except IndexError:
            example = ''

        return (term, gloss, example)

    def format(self, term='', withex=True):
        term, gloss, example = self.term(term)

        output  = term + '\n\n' + '   ' + gloss + '\n'

        if withex and example:
            output += '\n'
            for example in self.rhetoric[term][1:]:
                #for line in align_paragraph(example,100):
                for line in textwrap.wrap(example,100):
                    output += '     ' + line + '\n'
                output += '\n'

        #output = output.rstrip()
        return output

    def show(self, term = ''):
        if term:
            print( self.format(term), end = '' )
        else:
            print(self.format(), end = '')

# erase last newline using ANSI escape sequence
# http://www.termsys.demon.co.uk/vtansi.htm  can't find the sequence [F in any docs.
#            sys.stdout.write("\033[F")

if __name__ == "__main__":
    r = Rhetoric()
    r.show()

