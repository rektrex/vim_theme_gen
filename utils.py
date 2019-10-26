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
 """set statusline=
set statusline+=\ %{StatuslineMode()}
set statusline+=%=
set statusline+=%{coc#status()}\ 
set statusline+=\ %t
set statusline+=%m
set statusline+=%r
set laststatus=2

function! StatuslineMode()
    let l:mode=mode()
    if l:mode==#"n"
        return "NORMAL"
    elseif l:mode==?"v"
        return "VISUAL"
    elseif l:mode==#"i"
        return "INSERT"
    elseif l:mode==#"R"
        return "REPLACE"
    elseif l:mode==?"s"
        return "SELECT"
    elseif l:mode==#"t"
        return "TERMINAL"
    elseif l:mode==#"c"
        return "COMMAND"
    elseif l:mode==#"!"
        return "SHELL"
    endif
endfunction
"""


def setHighlight(name , bg, fg, gui):
    return f'hi {name} guibg={bg} guifg={fg} gui={gui}'


def addNewSection(group):
    return '" ' + group.ljust(75, '-')
