cities=[]
census={}

def check_revenue(number):
    if number>1500:
        return True
    return False

cont=0
while cont<4:
    cont+=1
    try:
        city = input("Enter the city name: ")
        population = int(input("Enter the annual population: "))
    except ValueError as e:
        print("Invalid input. Enter a valid number.")
        population = int(input("Enter the annual population: "))

    try:
        citizen_income=float(input("Input the population income: "))
        average_income=population/citizen_income
        if check_revenue(average_income):
            cities.append(city)
            census[city] = [population, average_income]
            print("City added!")
        else:
            print("City not added because monthly revenue is less than $1500.")
    except ValueError as e:
        print("Invalid input. Enter a valid number.")

print("Registered cities:")
for city in cities:
    print(f"- ", city)

print(census)
total_cities=len(cities)


top_revenue=0
weighted_ave=0
index=0

print(f"\n===Summary: ===")
if len(cities) > 0:
    pop_total = sum([census[i][0] for i in sorted(census.keys())])
    print(f"\nTotal population: ", pop_total)
    ave_total_income = sum([census[i][1] for i in sorted(census.keys())])
    print(f"Sum of the total average income: {ave_total_income:.0f}")
    for x in census:
        index += 1
        weighted_ave += census[x][0] * index
        if top_revenue<census[x][1]:
            top_revenue = census[x][1]
            city_top_revenue=x
    weighted_average = weighted_ave / index
    print(f"The weighted average revenue per citizen: {weighted_average:.0f}")
    print(f"City with the largest income: '{city_top_revenue}' with income {top_revenue:.0f}")
else:
    print("No city has been registered for analysis. ")

top_revenue2=0
weighted_ave2=0
index=0
remove = input("\nWould you like to remove any City? (Y/N): ").strip().lower()

if remove == "y":
    remove_city = input("Enter the name of the city you wish to remove: ").strip()
    if remove_city in cities:
        cities.remove(remove_city)
        if remove_city in census:
            del census[remove_city]
        print(f"The city '{remove_city}' was successfully removed!")
    else:
        print("The city entered is not on the list.")

    total_cities2 = len(cities)
    print("\n=== Updated summary ===")
    print("Registered cities:")

    for c in census:
        print(" -", c)
    print(f"\nTotal number of cities added: {total_cities2}")

    if total_cities2 > 0:
        pop_total = sum([census[i][0] for i in sorted(census.keys())])
        print(f"\nTotal population: ", pop_total)
        ave_total_income = sum([census[i][1] for i in sorted(census.keys())])
        print(f"Aggregated total average income: {ave_total_income:.0f}")
        for x in census:
            index += 1
            weighted_ave2 += census[x][0] * index
            if top_revenue2 < census[x][1]:
                top_revenue2 = census[x][1]
                city_top_revenue2 = x
        weighted_average2 = weighted_ave2 / index
        print(f"The weighted average revenue per citizen: {weighted_average2:.0f}")
        print(f"City with the largest income: '{city_top_revenue2}' with income {top_revenue2:.0f}")
    else:
        print("There are not enough cities for analysis after removal.")
else:
    print("\nNo removal was performed. Program finished.")
