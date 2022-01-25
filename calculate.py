columns = None

data = []
with open('newton.csv') as f:
    columns = f.readline().strip().split(',')

    for line in f:
        data.append(line)

columns = None
data = []
with open('shakepay.csv') as f:
    columns = f.readline().strip().split(',')

    for line in f:
        data.append(line)
