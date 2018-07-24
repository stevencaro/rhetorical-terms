#!/usr/bin/python3
import argparse
import sys

import urwid as ur

from ArrayStack import ArrayStack
from rhetoric import Rhetoric

seen_terms = ArrayStack()
prev_term_g = ()
curr_term_g = ()

def getterm():
    ### instantiates rhetoric object
    r = Rhetoric()

    term, gloss, examples = r.term()


    return term, gloss, examples

def prev_term():
    t, g, e = seen_terms.pop()
    return t,g,e

def getbody( term, gloss, examples ):
    global curr_term_g
    curr_term_g = (term, gloss, examples)
    content = [ ur.Text(''),
                ur.Text(('term', term), align = 'center'),
                ur.Text(''),
                ur.Text(('gloss', gloss), align = 'center'),
                ur.Text('') ] + [ ur.Text(('ex', ex + '\n'), align = 'left') for ex in examples ]

    return ur.Filler( ur.Padding( ur.LineBox(ur.Pile( content ) ), left=10, right=10))

def unhandled_input(key):
    #global prev_term, seen_terms, curr_term
    if key in ['Q', 'q', 'esc']:
        raise ur.ExitMainLoop()
    elif key in ['n', 'space']:
        prev_term_g = curr_term_g
        seen_terms.push( prev_term_g )
        main.contents['body'] = (getbody(*getterm()), None)
    elif key in ['p']:
        if seen_terms.is_empty():
            pass
        else:
            main.contents['body'] = (getbody(*prev_term()), None)
    else:
        pass
    return True
### Main application
if __name__ == '__main__':
    body = getbody(*getterm())

    palette = [ ('term',     'light blue',  'black' ),
                ('gloss',    'yellow',      'black' ),
                ('ex',       'white',      '') ]

    main   = ur.Frame(body=body) #, footer=footer)
    screen = ur.raw_display.Screen()
    loop   = ur.MainLoop(main,
                         palette,
                         unhandled_input = unhandled_input,
                         screen=screen)

### shows usage information on commandline
parser = argparse.ArgumentParser(description="Shows rhetorical terms and their definitions. Press 'n' to show the next term.")
args   = parser.parse_args()

### Runs main application
loop.run()

