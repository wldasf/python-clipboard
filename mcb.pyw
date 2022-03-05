#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py mcb.pyw <keyword> - Loads keyword to clipboard.
#        py mcb.pyw list - Loads all keywords to clipboard.
#        py mcb.pyw delete <keyword> - Deletes keyword in mcb file.
#        py mcb.pyw clear - Clears the entire clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:    
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'clear':
        for key in mcbShelf:
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
mcbShelf.close()