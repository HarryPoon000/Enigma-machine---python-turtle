class bad_rotor(Exception):
    pass

class bad_plugboard(Exception):
    pass

class error(Exception):
    pass

class machine():
    alph = [_ for _ in 'abcdefghijklmnopqrstuvwxyz']
    reflector = [_ for _ in 'zyxwvutsrqponmlkjihgfedcba']
    def __init__(self, rotors = None):
        self.plugboard = self.alph.copy()
        if rotors == None: # default rotors
            r1 = [_ for _ in 'dmtwsilruyqnkfejcazbpgxohv']
            r2 = [_ for _ in 'hqzgpjtmoblncifdyawveusrkx']
            r3 = [_ for _ in 'uqntlszfmrehdpxkibvygjcwoa']
            self.rotors = [r1,r2,r3]
        elif len(rotors) != 0: # check manually added rotors
            for i in rotors:
                if len(i) == 26:
                    continue
                for t in i:
                    if i.count(t) != 1:
                        raise bad_rotor('bad rotor: no duplicates allowed')
                raise bad_rotor("bad rotor: not enough mappings")
            self.rotors = rotors.copy()
        else:
            raise bad_rotor("not enough rotors")
        self.ref = []
        for _ in self.rotors: # reference for each rotor
            self.ref.append(self.alph.copy())

    def compute(self, msg, reset = False):
        def single(letter):
            # step the rotors
            carry = False
            for i in range(len(self.rotors)+1):
                if i == 0:
                    continue
                if -i == -1:
                    carry = True
                if carry:
                    if self.ref[-i].index('a') != 25:
                        carry = False
                    self.ref[-i].insert(0,self.ref[-i].pop(-1))
                    self.rotors[-i].insert(0,self.rotors[-i].pop(-1))
            # compute a single word
            inp = self.plugboard.index(letter)
            for i in range(len(self.rotors)+1): # right to left
                if i == 0:
                    continue
                inp = self.ref[-i].index(self.rotors[-i][inp])
                
            inp = self.reflector.index(self.alph[inp]) # reflector
            
            for i in range(len(self.rotors)): # left to right
                inp = self.rotors[i].index(self.ref[i][inp])
                
            out = self.plugboard[inp] # final letter
            return out
        
        out_lst = []
        for x in msg:
            if x not in self.alph:
                out_lst.append(x)
                continue
            out_lst.append(single(x))
        
        if reset:
            for n,i in enumerate(self.ref): # step each rotor forwards until it returns to original pos
                while i[0] != 'a':
                    i.insert(0, i.pop(-1))
                    self.rotors[n].insert(0, self.rotors[n].pop(-1))
                    
        self.pos = [i.index('a') for i in self.ref] # stores rotor positions
        return ''.join(out_lst)
    
    def plugboard_config(self, board):
        if len(board) == 26:
            if type(board) == str:
                board = [_ for _ in board]
            for n,i in enumerate(board):
                if i != self.alph[board.index(self.alph[n])]:
                    raise bad_plugboard('bad plugboard setup: two letters must map to each other (e.g. a->c, c->a)')
                elif board.count(i) != 1:
                    raise bad_plugboard('duplicate letter')
            else:
                self.plugboard = board    
        else:
            raise bad_plugboard('bad plugboard length')

    def set_rotor_pos(self, rot = [], pos = []): # change the rotor positions (list, list)
        if type(rot) != list:
            raise TypeError('expected type "list" for variable rot')
        if type(pos) != list:
            raise TypeError('expected type "list" for variable pos')
        if len(rot) != len(pos):
            raise error('number of rotors does not equal number of positions ')
        for nps,n in enumerate(rot):
            while self.ref[n].index('a') != pos[nps]:
                self.ref[n].insert(0, self.ref[n].pop(-1))
                self.rotors[n].insert(0, self.rotors[n].pop(-1))

        self.pos = [i.index('a') for i in self.ref] # stores rotor positions



def main():
    eng = machine()
    ##eng.plugboard_config('zecdbfghijklmnopqrstuvwxya')
    eng.set_rotor_pos([1],[1])
    print(eng.compute('test', reset = False))
    print(eng.pos)

if __name__ == '__main__':
    main()
    
