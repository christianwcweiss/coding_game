# CodingGame

## Description

## Local Setup
### Brew
If not already installed, get the package manager here: https://brew.sh/
``` shell script
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Python
Install [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
``` shell
brew install pyenv
brew install pyenv-virtualenv
```
Make sure to properly configure your terminal so that `which python` points to some `pyenv` shim file.
Probably you need to add the following two lines to your `~/.bashrc`/`~/.zshrc` file:
``` shell
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Activate your terminal config:
```source ~/.zshrc``` or ```source ~/.bashrc```

In the project root folder execute:
``` shell
make clean_setup
```
