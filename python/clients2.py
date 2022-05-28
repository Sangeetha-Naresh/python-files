credit_util_dict = {"768805383": 0.061,
                    "818770008" :0.105,
                    "713982108" : 0,
                    "769911858" : 0.76,
                    "709106358": 0,
                    "713061558":0.311
                    }

dict_list=credit_util_dict.values()


max=0
for n in dict_list:

    if n > max:
        max=n

print(" The highest Avg_Utilization_Ratio is : ")
print(max)
print("------------------------------------------------------")
print(" ")
print("CLIENTNUM with the highest Avg_Utilization_Ratio is : ")
for c in credit_util_dict:   
    if credit_util_dict[c] == max: 
        print(c) 
    

