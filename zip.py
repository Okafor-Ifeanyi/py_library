from itertools import zip_longest

# Lists
countries = ['Nigeria', 'Cameroon', 'Niger', "SA", "Egypt"]
capitals = ['Abuja', 'Enugu', 'Delta', 'Freetown', 'Bayelsa']
cities = ['Gwara', 'Ind layout', 'warri']
countries_and_capitals = zip(countries, capitals, cities)
c_a = zip_longest(countries, capitals, cities)
c_a_null = zip_longest(countries, capitals, cities, fillvalue='NULL')


print(list(c_a_null))
# countries_and_capitals.__next__()
# print(list(countries_and_capitals))

# for country, capital in countries_and_capitals:
    # print(country, capital)



# Dictionaries

products = {'apple': 0.5, 'pineapple': 0.7}
tech_products = {'iphone': 1000, 'Windows': 600}
join = zip(products.values(), tech_products)

print(list(join))


# TUPLES

countries = ('Nigeria', 'Cameroon', 'Niger', "SA", "Egypt")
capitals = ('Abuja', 'Enugu', 'Delta', 'Freetown', 'Bayelsa')
cities = ('Gwara', 'Ind layout', 'warri')

pairs = zip(countries, capitals, cities)
print(list(pairs))


# STRINGS

country = 'Nigeria'
capital = 'Abuja'
merge = zip(country, capital)
print(list(merge))