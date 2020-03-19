import itertools

l = ['swagath', 'bhat', 'bailore']

# defining iterator
iterators = itertools.cycle(l)

# for in loop
for i in range(6):
    # Using next function
    print(next(iterators))