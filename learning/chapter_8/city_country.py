def city_country(city, country):
    """接受城市的名称及其所在的国家"""
    full_city_country = f'{city}, {country}'
    return full_city_country.title()

city = city_country('beijing', 'china')

print(city)