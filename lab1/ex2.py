from math import *

def euclid_algo(x, y, verbose=False):
	if x < y: # We want x >= y
		return euclid_algo(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print('gcd is %s' % x) 
	return x


class Fraction:
    def __init__(self, x, y):
        self.numerator = x
        self.denominator = y
        
    
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        
        
        
    def reduce(self):
        divider = euclid_algo(self.numerator, self.denominator)
        self.numerator = int(self.numerator/ divider)
        self.denominator = int(self.denominator / divider)
        
        
        