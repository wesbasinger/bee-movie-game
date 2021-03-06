# -*- coding: utf-8 -*-
import random

class Game(object):
    
    def __init__(self):
                
        f = open("script.txt")
        raw = f.read()
        f.close()
        delim = raw.split(".")
        
        self.lines = delim
        
        
        g = open("red_herrings.txt")
        raw = g.read()
        raw = raw.split("\n")
            
        self.red_herrings = raw
        
    
    def get_line(self, ix):
        
        return self.lines[ix].replace("\n", " ")
        
    
    def scramble(self, ix):
        
        next_line = self.get_line(ix)
        
        delim = next_line.split(" ")
        
        candidate = None
        
        while not candidate:
            
            possible_word = random.choice(delim)
            if len(possible_word) > 1:
                candidate = possible_word.strip("?")
        
        choices_seed = random.sample(self.red_herrings, 2)
        choices_seed.append(candidate)
        random.shuffle(choices_seed)
        
        #return (next_line.replace(candidate, "---"), candidate)
        return {
                'display': next_line.replace(candidate, "---"),
                'missing_word': candidate,
                'choices': choices_seed,
                'line_number': ix
        }
        
        