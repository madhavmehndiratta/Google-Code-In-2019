from matplotlib import pyplot as plt

x_axis = ["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100"]
y_axis = [0,0,0,0,0,0,0,0,0,0]

with open("data.txt", 'r') as Data:
	for data in Data.readlines():
		data = data.split(' ')
		for num in data:
			for number in x_axis:
				K = number.split("-")
				if(num != "" and int(num) >= int(K[0]) and int(num) <= int(K[1])):
					y_axis[int(number[0])]+=1

plt.title("Random Number Range", color = "black")
plt.bar(x_axis, y_axis, color = "lightblue")
plt.xlabel("Range Of Numbers", color = "black")
plt.ylabel("No. Of Numbers", color = "black")
plt.show()
