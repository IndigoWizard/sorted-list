from operator import attrgetter

# mutant_power.py
# mutants power level hirarchy
# the smaller the number the higher the hirarchy

class mutants:
  def __init__(self, a, m, x):
    self.name = a
    self.power = m
    self.rank = x
  
  def __repr__(self):
    return self.name + ": " + self.power + " Level "

krakoa = [
  mutants('Sinister', 'Omega', 2),
  mutants('Rogue', 'Alpha', 3),
  mutants('Wolverine', 'Beta', 4),
  mutants('Magneto', 'Beyond Omega', 1),
  mutants('Artie Maddicks', 'Epsilon', 5)
]

for mutants in sorted(krakoa, key=attrgetter('rank')):
  print(mutants)
