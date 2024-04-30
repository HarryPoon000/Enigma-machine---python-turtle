# Enigma-machine---python-turtle
A module to recreate a digital enigma machine with a working UI and the ability to setup the machine to encrypt/decrypt any messages
---

# Usage: enigma.py

The `machine` class holds all the functions to recreate an enigma machine with an arbitary number of rotors

## `machine(rotors = None)`
`rotors`: a list of strings, each of length 26 representing the mapping from each rotor's input character to the output character
> For a rotor with mapping `'dmtwsilruyqnkfejcazbpgxohv'` at position 0, `a` will be mapped to `d`, `b` will be mapped to `m`, and so on.


## `compute(msg, reset = False)`
`msg`: the input message to be encrypted/decrypted
`reset`: if `reset` is set to `True`, the rotors will be reset to position 0 after execution

## `plugboard_config(board)`
`board`: a string of length 26 which represents the plugboard mapping. Two letters must map to each other
> passing `dbcaefghijklmnopqrstuvwxyz` will configure the plugboard to swap `a` and `d`

## `set_rotor_position(rot = [], pos = [])`
`rot`: list of indicies of rotors for which we want to change the position
`pos`: list of new positions for each corresponding rotor in `rot`
***NOTE:*** `rot` and `pos` must be of the same length

> `set_rotor_position([1],[1])` will set the rotor at index 1 to position 1

---

# Usage: turtle - enigma machine.py

After the script is ran, a `turtle` graphics window will show up. It takes keyboard input from the device and processes it. The encrypted/decrypted characters will show on the screen.

## resetting
To reset, press the grey square near the bottom

## plugboard
This implementation currently does not support plugboard editing
