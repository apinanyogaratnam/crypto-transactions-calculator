columns = None

data = []
with open('newton.csv') as f:
    columns = f.readline().strip().split(',')

    for line in f:
        data.append(line)

# newton aggregation
total_btc_bought = 0
total_price_paid_btc = 0
total_btc_sold = 0
total_price_paid_sold = 0
for item in data:
    important_data = item.strip().split(',')
    important_data = important_data[1:5]
    if '' in important_data: continue

    _to = important_data[1]
    _to_amount = float(important_data[0])
    _from = important_data[3]
    _from_amount = float(important_data[2])

    if _to == 'BTC' and _from == 'CAD':
        total_btc_bought += _to_amount
        total_price_paid_btc += _from_amount

    if _to == 'CAD' and _from == 'BTC':
        total_btc_sold += _to_amount
        total_price_paid_sold += _from_amount


columns = None
data = []
with open('shakepay.csv') as f:
    columns = f.readline().strip().split(',')

    for line in f:
        data.append(line)

# shakepay aggregation
for item in data:
    print(item)
