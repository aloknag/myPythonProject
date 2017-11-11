import sys

n = int(raw_input().strip())  # N for NxN matrix
# values of right diagonal is 00, 11, 22, 33, NN ... value of left diagonal is 0N, 1N-2, 2N-2 .. N0
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)

# build primary diagonal and secondary diagonal
pd = []
sd = []
for x in xrange(n):
    pd.append(a[x][x])
    sd.append(a[[x][n - x]])

print pd
print sd