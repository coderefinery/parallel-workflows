import time


# Load the city data
def load_cities(filename):
    with open(filename, "r") as f:
        cities = []
        countries = []
        for line in f.readlines()[1:]:
            entries = line.split(",")
            cities.append(entries[0])
            countries.append(entries[1])
        return cities, countries


# We will assume, that this function is runnning for a  long time.
def solve_long_problem(cities, countries, targetcountry):
    time.sleep(60)  # simulate a runtime of a minute
    country_cities = []
    for i in range(len(countries)):
        if countries[i] == targetcountry:
            country_cities.append(cities[i])
    return country_cities


file_path = "cities.csv"  # Update with your actual file path
cities, countries = load_cities(file_path)

# set will make the countries unique
for country in set(countries):
    # get the cities for this country
    current_cities = solve_long_problem(cities, countries, country)
    with open(f"{country}.txt", "w") as f:
        f.write("\n".join(current_cities))
