# freqkey

     _                   _             
    | |                 | |            
    | |  ,_    _   __,  | |   _        
    |/  /  |  |/  /  |  |/_) |/  |   | 
    |__/   |_/|__/\_/|_/| \_/|__/ \_/|/
    |\               |\ that's      /| 
    |/               |/ "freaky"    \| 


[![PyPI version](https://badge.fury.io/py/freqkey.svg)](https://badge.fury.io/py/freqkey)

## What do

Listens in on all your keypresses (without logging them consecutively, this is 
not a keylogger) and generates a count that looks somewhat like this:

    freqkey version 0.0.3
    Started: 2019-03-25 11:56:34.094453 (duration 22:59:03.310315)

    Modifiers:
      leftctrl                                                     717
      leftshift                                                    339
      leftmeta                                                     267
      leftalt                                                       99
      rightshift                                                    55
      leftctrl + leftshift                                          20
      leftalt + leftctrl                                             4

    Combos:
      leftctrl + backspace                                         126
      leftmeta + tab                                               123
      leftctrl + w                                                  86
      leftctrl + b                                                  74
      leftctrl + left                                               62
      leftshift + space                                             59
      leftmeta + 1                                                  56

    Singles:
      space                                                        622
      enter                                                        521
      j                                                            519
      e                                                            503
      backspace                                                    373
      t                                                            367
      ...

## Usage

    usage: freqkey [-h] [--out OUT] [--update UPDATE] [--version]

    optional arguments:
      -h, --help       show this help message and exit
      --out OUT        Output file, defaults to stdout
      --update UPDATE  Update frequency in seconds, defaults to 60
      --version        show program's version number and exit

## Problems

I've only tested this on an Ubuntu Linux system. It should be cross-platform
as it uses the [inputs](https://pypi.org/project/inputs) library to collect key
events. If you have issues running it, make sure your user is in the `input`
group or, if you must, run it as root.
