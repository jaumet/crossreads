import difflib as dl

a = file('2.txt').read()
b = file('4.txt').read()

sim = dl.get_close_matches

s = 0
wa = a.split()
wb = b.split()

for i in wa:
    if sim(i, wb):
        s += 1

n = float(s) / float(len(wa))
print '%d%% similarity' % int(n * 100)
