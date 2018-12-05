from collections import defaultdict
import random


class CFG(object):
	def __init__(self):
		self.prod = defaultdict(list)

	def add_prod(self, lhs, rhs):
		""" Add production to the grammar. 'rhs' can
            be several productions separated by '|'.
            Each production is a sequence of symbols
            separated by whitespace.

            Usage:
                grammar.add_prod('NT', 'VP PP')
                grammar.add_prod('Digit', '1|2|3|4')
        """
		prods = rhs.split('|')
		for prod in prods:
			self.prod[lhs].append(tuple(prod.split()))

	def gen_random(self, symbol):
		""" Generate a random sentence from the
            grammar, starting with the given
            symbol.
        """
		sentence = ''

		# select one production of this symbol randomly
		rand_prod = random.choice(self.prod[symbol])

		for sym in rand_prod:
			# for non-terminals, recurse
			if sym in self.prod:
				sentence += self.gen_random(sym)
			else:
				sentence += sym + ' '

		return sentence


cfg1 = CFG()
cfg1.add_prod('WeatherP', 'VP CC Temp Loc | VP CC Temp | Loc VP CC Temp TimeP | VP Loc TimeP | VP CC Temp TimeP | VPF Loc TimeF')
cfg1.add_prod('VP', 'det är CondADJ | det CondVB')
cfg1.add_prod('VPF', 'det kommer CondFUT')
cfg1.add_prod('Temp', '26 grader | 30 grader')
cfg1.add_prod('CC', 'och')
cfg1.add_prod('Loc', 'LocI PlaceI | LocPÅ PlacePÅ')
cfg1.add_prod('LocI', 'i')
cfg1.add_prod('LocPÅ', 'på')
cfg1.add_prod('CondADJ', 'molnig | regnig')
cfg1.add_prod('CondVB', 'snöar')
cfg1.add_prod('CondFUT', 'snöa')
cfg1.add_prod('TimeP', 'akkurat nå')
cfg1.add_prod('TimeF', 'imorgon')
cfg1.add_prod('PlaceI', 'Bloomington | Stockholm')
cfg1.add_prod('PlacePÅ', 'Gotland | Färöarna')

for i in range(10):
	print(cfg1.gen_random('WeatherP'))