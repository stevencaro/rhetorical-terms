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
    r = Rhetoric()
    term, gloss, examples = r.term()
    return term, gloss, examples

def show_prev_term():
    if seen_terms.is_empty():
        pass
    else:
        t, g, e = seen_terms.pop()
        main.contents['body'] = (getbody(t, g, e), None)

def getbody( term, gloss, examples ):
    global curr_term_g
    curr_term_g = (term, gloss, examples)
    content = [ ur.Text(''),
                ur.Text(('term', term), align = 'center'),
                ur.Text(''),
                ur.Text(('gloss', gloss), align = 'center'),
                ur.Text('') ] + [ ur.Text(('ex', ex + '\n'), align = 'left') for ex in examples ]

    return ur.Filler( ur.Padding( ur.LineBox(ur.Pile( content ) ), left=10, right=10))

def show_next_term():
    prev_term_g = curr_term_g
    seen_terms.push( prev_term_g )
    main.contents['body'] = (getbody(*getterm()), None)

def unhandled_input(key):
    if key in ['Q', 'q', 'esc']:
        raise ur.ExitMainLoop()
    elif key in ['n', 'space']:
        show_next_term()
    elif key in ['p']:
        show_prev_term()

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

### shows usage information on command line
parser = argparse.ArgumentParser(description="Shows rhetorical terms and their definitions. Press 'n' to show the next term. Press 'p' to show previous term.")
args   = parser.parse_args()

### Runs main application
loop.run()

