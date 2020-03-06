def getCityNameandCountry(city,country,population=''):
    cityName = f"{city}, {country}"
    if population:
        population = f" - population {population}"
        return cityName.title() + population
    else:
        return cityName.title()