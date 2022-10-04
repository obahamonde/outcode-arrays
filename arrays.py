from typing import *

class FooBarArray:
  def __init__(self, foo:List[int]):
    self.foo = foo

  @property
  def first(self):
    return self.foo[1]

  @property
  def length(self):
    return len(self.foo)

  def reverse(self):
    return (self.foo[2::] + self.foo[0:2]) if self.first<self.length else (self.foo[1::]+self.foo[0:1])
    

def ArrayChallenge(arr):
  a = FooBarArray(arr)
  return a.reverse()



# keep this function call here   

def raw_input():
    ... # Test Cases

print(ArrayChallenge(raw_input()))