# releasenote

[![CircleCI](https://circleci.com/gh/NivedhaSenthil/releasenote.svg?style=svg)](https://circleci.com/gh/NivedhaSenthil/releasenote)

Releasenote is a python library used to get change log between given two git commits linking the story card number specified in the commit message with agile tracker (eg. Mingle). It is a command line tool built using python click library. 

## Install

### From source code:

```
python setup.py install
```

### From the Pypi repository:

```
pip install releasenote
```

### Package available at: 
https://pypi.python.org/pypi/releasenote/1.0

Dependencies will be installed when installed using pip or setup.py

You can also clone the source from github,
git clone https://github.com/NivedhaSenthil/releasenote.git

## Commit Message Format
```
<story-number | Fix | Refactor> commit message
```
story-number has to be same as the one agile tracker

## Options

  -lc, --lastcommit TEXT  Commit hash of last release
  
  -ct, --committill TEXT  Commit hash of till which notes has to generated
  
  --project TEXT          Agile tracker(eg. mingle) project name
  
  --name TEXT             Agile tracker(eg. mingle) username
  
  --password TEXT         Agile tracker(eg.mingle) password

## Example

```
releasenote -ct ea66bda5
```
This will prompt for project name, user name and password of mingle account.
--lastcommit is optional, when not given the first commit of the repository will be taken by default.


