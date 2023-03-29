# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))


# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))


# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())


# # Get data in columns
#
# print(data["condition"])
# print(data.condition)


# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# create a dataframe from scratch
# data_dict = {
#     "students": ["arman", "tashfin", "pranto"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# 2018 central park
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sguirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sguirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sguirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_sguirrels_count)
print(red_sguirrels_count)
print(black_sguirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sguirrels_count, red_sguirrels_count, black_sguirrels_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")