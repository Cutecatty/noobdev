# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../00_card.ipynb 4
from fastcore.utils import *
from fastcore.test import *

# %% ../00_card.ipynb 5
suits =[ "♣","♦","♥","♠"]
ranks=[None,"A"]+[str(x) for x in range(2,11)] + ["J","Q","K"]

# %% ../00_card.ipynb 11
class Card: 
    "A playing card created from passing a rank from rank and suit from suit"
    def __init__(self,
                 suit:int,  # An index into suits
                 rank:int): # An index into ranks

        self.suit,self.rank = suit,rank
    def __str__(self):return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__ = __str__
   

# %% ../00_card.ipynb 12
@patch
def __eq__(self:Card,a:Card):return (self.suit,self.rank) == (a.suit,a.rank)

# %% ../00_card.ipynb 13
@patch
def __lt__(self:Card,a:Card):return (self.suit,self.rank) < (a.suit,a.rank)

# %% ../00_card.ipynb 14
@patch
def __gt__(self:Card,a:Card):return (self.suit,self.rank) > (a.suit,a.rank)
