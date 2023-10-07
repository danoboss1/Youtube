WORLD_POPULATION = 8 * 10^9

def get_input():
    your_city = int(input('Enter your city population: '))
    percentage_in_country = float(input('Enter the percentage of your city in the country: '))
    country = int(input('Enter the population of the country: '))

    return your_city, percentage_in_country, country

def main():
    your_city, percentage_in_country, country = get_input()

    numerator = your_city * percentage_in_country
    denominator = country
    
    conditional_probability = numerator / denominator

    print(f'The probability of people living in the city with condition people living in the country is {conditional_probability}')


main()