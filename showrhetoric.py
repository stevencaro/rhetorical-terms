#!/usr/bin/python3
import argparse
import sys

import urwid as ur

from rhetoric import Rhetoric

def unhandled_input(key):
    if key in ['Q', 'q', 'esc']:
        raise ur.ExitMainLoop()
    elif key in ['n', 'space']:
        main.contents['body'] = (getbody(), None)
    else:
        pass
    return True

def getterm(term=''):
    ### instantiates rhetoric object
    r = Rhetoric()

    term, gloss, examples = r.term()

    ### format content for display
    content = [ ur.Text(''),
                ur.Text(('term', term), align = 'center'),
                ur.Text(''),
                ur.Text(('gloss', gloss), align = 'center'),
                ur.Text('') ] + [ ur.Text(('ex', ex + '\n'), align = 'left') for ex in examples ]

    return content

def getbody():
    return ur.Filler( ur.Padding( ur.LineBox(ur.Pile( getterm()) ), left=10, right=10))

### Main application
if __name__ == '__main__':
    body = getbody()

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

