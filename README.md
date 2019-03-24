     _                   _             
    | |                 | |            
    | |  ,_    _   __,  | |   _        
    |/  /  |  |/  /  |  |/_) |/  |   | 
    |__/   |_/|__/\_/|_/| \_/|__/ \_/|/
    |\               |\ that's      /| 
    |/               |/ "freaky"    \| 


# What do

Listens in on all your keypresses (without logging them consecutively, this is 
not a keylogger) and generates a count that looks somewhat like this:

    Started: 2019-03-24 19:05:54.123276 (duration 0:00:20.107664)

    Modifiers:
      leftmeta                                                       5
      leftctrl                                                       3
      leftalt                                                        1

    Combos:
      k                                                              6
      j                                                              4
      leftmeta + 1                                                   2
      leftmeta + tab                                                 2
      leftctrl + space                                               1
      h                                                              1
      b                                                              1
      leftmeta + 2                                                   1
      leftctrl + t                                                   1
      leftctrl + w                                                   1
      leftalt + 1                                                    1
      space                                                          1

# Usage

    usage: freqkey [-h] [--out OUT] [--update UPDATE]

    optional arguments:
      -h, --help       show this help message and exit
      --out OUT        Output file, defaults to stdout
      --update UPDATE  Update frequency in seconds, defaults to 60

# Problems

I've only tested this on an Ubuntu Linux system. It should be cross-platform
as it uses the [inputs](https://pypi.org/project/inputs) library to collect key
events. If you have issues running it, make sure your user is in the `input`
group or, if you must, run it as root.
