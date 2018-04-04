#!/usr/bin/python3
import urwid as ur

from rhetoric import Rhetoric
import sys

def unhandled_input(key):
    if key in ['Q', 'q', 'esc']:
        raise ur.ExitMainLoop()
    elif key in ['n', 'space']:
        main.contents['body'] = (getbody(), None)
        #.original_widget.original_widget.contents
    else:
        pass
    return True

def getterm(term=''):
    r = Rhetoric()

    term,gloss,examples = r.term()
    content = [ ur.Text(''),
               ur.Text(('term', term), align = 'center'),
            ur.Text(''),
            ur.Text(('gloss', gloss), align = 'center'),
            ur.Text('') ] + [ ur.Text(('ex', ex + '\n'), align = 'left') for ex in examples ]
    return content

def getbody():
    return ur.Filler( ur.Padding( ur.LineBox(ur.Pile( getterm()) ), left=10, right=10))

body = getbody()

palette = [ ('body',     'light cyan',  'default',  'standout' ),
            ('header',   'white',       'dark red', 'bold'),
            ('term',     'light blue',  'black' ),
            ('gloss',    'yellow',      'black' ),
            ('ex',       'white',      '') ]

main = ur.Frame(body=body) #, footer=footer)
screen=ur.raw_display.Screen()

loop = ur.MainLoop(main,
                   palette,
                   unhandled_input = unhandled_input,
                   screen=screen)
loop.run()

