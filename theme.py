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
        ('Normal', {'bg': background, 'fg': foreground}),
        ('_new', 'statusline'),
]

with open(f'{name}.vim', 'w') as f:
    f.write(utils.init(name, style))

    for name, group in highlightGroups:
        if name == '_new':
            f.write('\n\n' + utils.addNewSection(group) + '\n')
            continue

        bg = group.get('bg', 'NONE')
        fg = group.get('fg', 'NONE')
        gui = group.get('gui', 'NONE')

        f.write('\n' + utils.setHighlight(name, bg, fg, gui))

    f.write('\n' + utils.statusline)
