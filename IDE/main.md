# Pycharm 
#### hot-keys:
```
ctrl+E          - recently opened files
ctrl+shift+F    - find strings in files in whole project
shift+shift     - find files, directories by name
ctrl+N          - find Class by name
ctrl+Q          - Show variable description
shift+F6        - refactoring
ctrl+Tab        - switch between last opened tabs
ctrl+shift+U    - toggle case
ctrl+shift+i    - Show class/function/method bodies
ctrl+"+"        - expand function
ctrl+"-"        - collapse function
ctrl+shift+"+"  - expand all functions
ctrl+shift+"-"  - collapse all functions
ctrl+alt+[ / ]  - next / prev project
ctrl+shift+(numUp|numDown) - moving code blocks up/down (e.g. class, function)
```

# TMUX
```bash 
tmux source-file ~/.tmux.conf
tmux new-session -s edxapp
tmux attach -t edxapp
tmux list-sessions
```
### Keys:
```
All commands with ctrl+b then key of command:
c - create new window (0 window, 1 window, etc)
0 - switch to window 0, 1 - switch to window 1, etc
% - split the window into two vertical ones
" - split the window into two horizontal ones
arrors (left, right, top, bottom) - navigate througt the window splits
d - detach from session (session continue existing)
{ - change windows splites places
```

### Copy-Paste
```
shift+mouse click -> select
ctrl+shift+C
ctrl+shift+V
```

### IN ~/.tmux.conf
```bash
# set-option -g prefix C-q 	# from ctrl+b to ctrl+q
set -g mouse on
echo 'set -g mouse on' > ~/.tmux.conf
```

# VIM
### line umbers
```bash
:set number
# Or run with "+set number"
vim "+set number" some_file_name.txt
```

### Unicode simbols
```
:set encoding=utf-8
```

### Go to line 444
```
:444
```

### VScode
#### To disable opening new file instead of perviously openned one
```bash
# settings located
# Global
/home/$USER/.config/Code/User/settings.json

# Workspace:
<proj_path>/.vscode/settings.json



disable the setting "enablePreviewFromQuickOpen"
also the "enablePreview" should be disabled as well
```

#### Enable type checking

```json
// Path to venv
{
    "python.envFile": "${workspaceFolder}/venv",
}

// Select check mode
{
    "python.analysis.typeCheckingMode": "basic"
}

// Enable django pylint
{
    "python.envFile": "${workspaceFolder}/venv",
    "python.analysis.typeCheckingMode": "basic",
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length=120"
    ],
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint_django"
    ],

    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "python.linting.mypyEnabled": true

}
```