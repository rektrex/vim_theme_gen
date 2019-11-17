def init(name, background = 'dark'):
    out = ""
    out += \
f"""hi clear

if exists('syntax_on')
    syntax reset
endif

let g:colors_name='{name}'
set background={background}
"""

    return out

statusline =\
"""hi link statuscolor NormalColor

set statusline=
set statusline+=%#statuscolor#
set statusline+=\ %{StatuslineMode()}\ 
set statusline+=%#Statusline#
set statusline+=%=
set statusline+=%#statuscolor#
set statusline+=\ %t
set statusline+=%m
set statusline+=%r\ 
set statusline+=%#Statusline#
set laststatus=2

function! StatuslineMode()
    let l:mode=mode()
    if l:mode==#"n"
        hi link statuscolor NormalColor
        return "NORMAL"
    elseif l:mode==?"v"
        hi link statuscolor VisualColor
        return "VISUAL"
    elseif l:mode==#"i"
        hi link statuscolor InsertColor
        return "INSERT"
    elseif l:mode==#"R"
        hi link statuscolor ReplaceColor
        return "REPLACE"
    elseif l:mode==?"s"
        hi link statuscolor VisualColor
        return "SELECT"
    elseif l:mode==#"t"
        hi link statuscolor NormalColor
        return "TERMINAL"
    elseif l:mode==#"c"
        hi link statuscolor NormalColor
        return "COMMAND"
    elseif l:mode==#"!"
        hi link statuscolor NormalColor
        return "SHELL"
    endif
endfunction
"""


def setHighlight(name , bg, fg, gui):
    return f'hi {name} guibg={bg} guifg={fg} gui={gui}'


def addNewSection(group):
    return '" ' + group.ljust(75, '-')
