import matplotlib.pyplot as plt
import geopandas as gpd

print("Welcome to the Shapefiles and Maps!\n\nChoose a city for which you want to plot the map: ")
print("\n1. Delhi\n2. Mumbai\n3. Chandigarh\n4. Tokyo\n5. London\n")
choice = input("Enter your Choice: ")

if choice == "1" or choice.lower() == "delhi":
    city_name = "Delhi"
elif choice == "2" or choice.lower() == "mumbai":
    city_name = "Mumbai"
elif choice == "3" or choice.lower() == "chandigarh":
    city_name = "Chandigarh"
elif choice == "4" or choice.lower() == "tokyo":
    city_name = "Tokyo"
elif choice == "5" or choice.lower() == "london":
    city_name = "London"
else:
    print("Wrong Choice Entered, Exiting the Program.....")
    exit()

print("\nWhat would you like to plot for",city_name)
print("\n1. Buildings\n2. LandUse\n3. Natural\n4. Places\n5. Railways\n6. Roads\n7. Waterways\n")
choice = input("Enter your Choice (Separated by Comma): ")

shape_type = ['0','buildings.shp','landuse.shp','natural.shp','places.shp','railways.shp','roads.shp','waterways.shp']

type_list = list(choice.split(","))
fp = "Cities/"+ city_name + "/shape/"+shape_type[int(type_list[0])]
data = gpd.read_file(fp)
ax = data.plot()
for i in range(1,len(type_list)) :
    fp = "Cities/" + city_name  + "/shape/" + shape_type[int(type_list[i])]
    data = gpd.read_file(fp)
    data.plot(ax = ax)
title = "Map of " + city_name
plt.title(title)
plt.show()