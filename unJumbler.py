# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:39:15 2015

@author: owendix

Small set of word unJumbler tools. For fun.

"""
import enchant
import copy
from itertools import permutations


def unJumble(jbl, nSols = 1):
    """
    Slow, brute force unjumbler of words dictionary, using PyEnchant

    Note: for thorough permutations, use
    import itertools
    perm = list("".join(string) for string in itertools.permutations("stack")
    perm = list(set(perm))
    """
    #jbl = 'nereco'
    #This particular unJumbler is only fast for
    #small words
    if nSols < 0:
        nSols = 0
    d = enchant.Dict('en_US')
    sols = []
    perms = set([''.join(p) for p in permutations(jbl)])
    n=0
    for aPerm in perms:
        if n >= nSols:
            break
        if d.check(aPerm):
            sols.append(aPerm)
            n += 1
    
    return sols
    
def visuallyUnJumble(jbl):
    
    
    """    
    Print permutations of first and last letter of a jumbled word

    Idea: the unjumbled word is easier to recognize if you see the
    first and last letter in place. The idea came to me from 
    observing the psychology demonstration that you can read a sentence 
    easily with olny the frist and lsat letetrs in plcae (intentional).
    
    Result/Analysis: this seems to confer only a slight advantage, at best. 
    Perhaps this argues that context within a sentence is important for this 
    effect.
    
    Note: for thorough permutations, use
    import itertools
    perm = list("".join(string) for string in itertools.permutations("stack")
    perm = list(set(perm))
    """
    
    #jbl = 'nereco'
    print('Original Jumble: ', jbl)
    perms = set()
    
    for i in range(0,len(jbl)):
        base_word = list(jbl)
        base_word[0]=jbl[i]
        base_word[i]=jbl[0]
        
        perms.add(''.join(base_word))
        for j in range(1,len(jbl)-1):
           #makes a copy, rather than points to original 
            word = copy.copy(base_word)  
            word[-1] = base_word[j]
            word[j] = base_word[-1]
            
            perms.add(''.join(word))
            
    for x in sorted(perms):
        print(x)



def myWord(jbl='nereco',nSols=1):
    
    """
    Run visuallyUnJumble to print word w/ all permutations of endcap letters

    userInput=False: take jumbled word from default
    
    """
    
    visuallyUnJumble(jbl)
    
    answer=str(input('Submit an answer: '))
    sols = unJumble(jbl,nSols)
    if answer in sols:
        print('Correct!')
    else:
        print('Fail! It is:',*sols)
        

