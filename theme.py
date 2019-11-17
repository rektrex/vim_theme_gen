import utils

name                = 'truelove'
style               = 'dark'

# colors
cursor              = '#c8c8c8'
background          = '#212121'
foreground          = '#dfdfdf'
foregroundFaded     = '#6f6f6f'
brown               = 'BROWN'
yellow              = '#dfc56d'
gray                = '#373737'
green               = '#88c563'
red                 = '#e76d6d'
accent              = '#ff6188'

highlightGroups = [
        ('_new', 'basic'),

        ('Normal', {'bg': background, 'fg': foreground}),
        ('Cursor', {'bg': cursor}),
        ('Title', {'fg': foreground, 'gui': 'BOLDUNDERLINE'}),
        ('Comment', {'fg': foregroundFaded, 'gui': 'ITALIC'}),
        ('SpecialComment', {'fg': brown, 'gui': 'ITALIC'}),
        ('Todo', {'fg': brown, 'gui': 'UNDERLINE'}),
        ('Directory', {'fg': yellow}),
        ('LineNR', {'fg': foregroundFaded}),
        ('CursorLineNr', {'fg': brown}),
        ('SignColumn', {}),
        ('Underlined', {'gui': 'UNDERLINE'}),
        ('Visual', {'bg': background, 'fg': foregroundFaded, 'gui': 'UNDERLINE'}),
        ('VisualNOS', {'gui': 'UNDERLINE'}),
        ('MatchParen', {'gui': 'BOLD'}),
        ('IncSearch', {'bg': yellow, 'fg': background}),
        ('Search', {'bg': yellow, 'fg': background}),
        ('CursorColumn', {}),
        ('CursorLine', {'bg': gray}),
        ('VertSplit', {'fg': foreground, 'gui': 'BOLD'}),
        ('WildMenu', {'fg': green, 'gui': 'BOLDUNDERLINE'}),
        ('DiffAdd', {'fg': green}),
        ('DiffDelete', {'fg': red}),
        ('DiffChange', {'fg': yellow}),
        ('DiffText', {'fg': yellow}),
        ('Pmenu', {'bg': gray, 'fg': foreground}),
        ('PmenuSel', {'bg': gray, 'fg': accent}),
        ('PmenuSbar', {'bg': gray, 'fg': green}),
        ('PmenuThumb', {'bg': accent, 'fg': foreground}),
        ('SpellBad', {'fg': red, 'gui': 'UNDERCURL'}),
        ('SpellCap', {'fg': yellow, 'gui': 'UNDERCURL'}),
        ('SpellLocal', {'fg': yellow, 'gui': 'UNDERCURL'}),
        ('SpellRare', {'fg': yellow, 'gui': 'UNDERCURL'}),
        ('ErrorMsg', {'fg': red}),
        ('WarningMsg', {'fg': yellow}),
        ('MoreMsg', {'fg': yellow}),
        ('Question', {'fg': yellow}),
        ('Error', {'fg': red, 'gui': 'REVERSE'}),
        ('Ignore', {}),
        ('EndOfBuffer', {'fg': background}),
        ('NonText', {'fg': red}),
        ('SpecialKey', {'fg': red, 'gui': 'UNDERCURL'}),
        ('Statusline', {'bg': gray}),
        ('StatuslineNC', {'bg': gray}),
        ('NormalColor', {'bg': yellow, 'fg': background}),
        ('InsertColor', {'bg': green, 'fg': background}),
        ('VisualColor', {'bg': foregroundFaded, 'fg': background}),
        ('ReplaceColor', {'bg': red, 'fg': background}),

        ('_new', 'clear & override'),
        ('_clear', 'Constant'),
        ('_clear', 'Statement'),
        ('_clear', 'Type'),
        ('_clear', 'Function'),
        ('_clear', 'PreProc'),
        ('_clear', 'Special'),
        ('_clear', 'Identifier'),
        ('Constant', {'fg': accent}),
        ('Tag', {'gui': 'UNDERLINE'}),

        ('_new', 'Help'),
        ('helpHyperTextJump', {'gui': 'UNDERLINE'}),

        ('_new', 'typeScript'),
        ('_link', ('typeScriptParens', 'Delimiter')),

        ('_new', 'vimscript'),
        ('_link', ('vimUserFunc', 'Function')),

        ('_new', 'javaScript'),
        ('_link', ('javaScriptValue', 'Constant')),
        ('_link', ('javaScriptNumber', 'javaScriptValue')),
        ('_link', ('javaScriptNull', 'javaScriptValue')),

        # ('_new', 'statusline'), # keep statusline as the last item.
]

with open(f'{name}.vim', 'w') as f:
    f.write(utils.init(name, style))

    for name, group in highlightGroups:
        if name == '_new':
            f.write('\n\n' + utils.addNewSection(group) + '\n')
            continue

        if name == '_clear':
            f.write('\n' + f'hi clear {group}')
            continue

        if name == '_link':
            f.write('\n' + f'hi link {group[0]} {group[1]}')
            continue

        bg = group.get('bg', 'NONE')
        fg = group.get('fg', 'NONE')
        gui = group.get('gui', 'NONE')

        f.write('\n' + utils.setHighlight(name, bg, fg, gui))

    # f.write('\n' + utils.statusline)
