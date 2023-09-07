import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

# print(gas['Year'])

plt.title('Gas prices over Time (in USD)')

# plt.plot(gas['Year'].values, gas['USA'].values, label='USA')

countries = ['USA', 'South Korea', 'Australia', 'Canada']

for country in countries:
    plt.plot(gas['Year'].values, gas[country].values, label=country)

plt.xticks(gas.Year[::3].tolist())
plt.legend()

plt.xlabel('Year')
plt.ylabel('US Dollars/Galon')

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()