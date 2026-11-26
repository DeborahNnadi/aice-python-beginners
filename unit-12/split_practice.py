african_countries = "Nigeria, Liberia, Senegal, Ghana, Libya"
date = "25/10/1986"

print(african_countries)
print(date)

countries_list = african_countries.split(",")

print(countries_list)

# Splitting on a slash

date_parts = date.split("/")
day = date_parts[0]
month = date_parts[1]
year = date_parts[2]

print(f"Day: {day}, Month: {month}, Year: {year}")



