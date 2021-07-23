zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

zoo_new = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo', len(zoo_new))
print('All animals in the new zoo are', zoo_new)
print('Animals brought from old zoo are', zoo_new[2])
print('Last animal brought from old zoo is', zoo_new[2][2])
print('Number of animals in the new zoo is', len(zoo_new) - 1 + len(zoo))
