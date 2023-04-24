def describe_city(city_name, country_name='China'):
    """接受一座城市的名字以及该城市所属的国家"""
    print(f'{city_name} is in {country_name}')
    
describe_city('shenzhen')
describe_city('NewYork', 'USA')
describe_city('beijing')