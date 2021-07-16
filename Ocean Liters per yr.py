def ocean():
    ocean_level = 1.6
years = 25
    
for year in range(1, years +1):
    total = ocean_level * year 
    print(f'Year {year}: {total} millimeters')
    
    
ocean()