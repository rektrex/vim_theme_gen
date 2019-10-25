# name of the colorscheme. The resultant colorscheme is written to {name}.vim
name = 'truelove'

import utils

with open(f'{name}.vim', 'w') as f:
    f.write(utils.init(name))
