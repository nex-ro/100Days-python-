# # import csv
# # with open("weather_data.csv") as dataFile:
# #     temperature=[]
# #     dataCsv=csv.reader(dataFile)
# #     for i in dataCsv:
# #         if(i[1]!='temp'):
# #             temperature.append(i[1])
# #     print(temperature)
#
import pandas
data=pandas.read_csv('weather_data.csv')
#
# data_dict=data.to_dict()
# temp_list=data['temp'].to_list()

# print(data_dict)
# # print(data[data.day=="Monday"])
# # print(data[data.temp==data.temp.max()])


import pandas
data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
list_fur=data['Highlight Fur Color'].to_list()
# print(list_fur.count("Cinnamon"))
# print(list_fur.count("nan")
# print(list_fur.count("White"))
# print(list_fur.count("Gray"))
# print(list_fur.count("Black"))
total={
    "Color":{
        "0":"Gray",
        "1":"White",
        "2":"Black",
        "3": "Cinnamon",
        "4": "nan",
    },
    "Total": {
        "0": list_fur.count("Gray"),
        "1": list_fur.count("White"),
        "2": list_fur.count("Black"),
        "3": list_fur.count("Cinnamon"),
        "4": list_fur.count("nan"),
    },

}
totalFrame=pandas.DataFrame.from_dict(total)
print(totalFrame)
totalFrame.to_csv("result.csv",)
# print(data[data.day=="Monday"])
