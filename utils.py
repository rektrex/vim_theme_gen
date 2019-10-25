def init(name):
    out = ""
    out += \
f"""hi clear

if exists('syntax_on')
    syntax reset
endif

let g:colors_name='{name}'

"""

    return out
