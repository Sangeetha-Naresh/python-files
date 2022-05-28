data_columns =["CLIENTNUM","Attrition_Flag","Customer_Age","Gender","Dependent_count",
"Education_Level","Marital_Status","Income_Category","Card_Category","Months_on_book",
"Total_Relationship_Count","Months_Inactive_12_mon","Contacts_Count_12_mon","Credit_Limit",
"Total_Revolving_Bal","Avg_Open_To_Buy","Total_Amt_Chng_Q4_Q1","Total_Trans_Amt",
"Total_Trans_Ct","Total_Ct_Chng_Q4_Q1","Avg_Utilization_Ratio"]

credit_card_data1 = ["768805383","Existing Customer","45","M","3","High School","Married",
"$60K -$80K","Blue","39","5","1","3","12691","777","11914","1.335","1144","42","1.625","0.061"]

credit_card_data2 = ["818770008","Existing Customer","49","F","5","Graduate","Single",
"Less than $40K","Blue","44","6","1","2","8256","864","7392","1.541","1291","33","3.714","0.105"]

credit_card_data3 = ["713982108","Existing Customer","51","M","3","Graduate","Married",
"$80K -$120K","Blue","36","4","1","0","3418","0","3418","2.594","1887","20","2.333","0"]

credit_card_data4 = ["769911858","Existing Customer","40","F","4","High School","Unknown",
"Less than $40K","Blue","34","3","4","1","3313","2517","796","1.405","1171","20","2.333","0.76"]

credit_card_data5 = ["709106358","Existing Customer","40","M","3","Uneducated","Married",
"$60K -$80K","Blue","21","5","1","0","4716","0","4716","2.175","816","28","2.5","0"]

credit_card_data6 = ["713061558","Existing Customer","44","M","2","Graduate","Married",
"$40K -$60K","Blue","36","3","1","2","4010","1247","2763","1.376","1088","24","0.846",
"0.311"]


# function to convert a list into a tuple
def convert(list):
    return tuple(list)
  
# function calls which converts the respective lists
tuple_columns=convert(data_columns)

tuple1=convert(credit_card_data1)
tuple2=convert(credit_card_data2)
tuple3=convert(credit_card_data3)
tuple4=convert(credit_card_data4)
tuple5=convert(credit_card_data5)
tuple6=convert(credit_card_data6)

# creating an empty list to add the tuples
list_of_tuples = []

# using the apped function to add the independent tuples into the end of the list
list_of_tuples.append(tuple_columns)
list_of_tuples.append(tuple1)
list_of_tuples.append(tuple2)
list_of_tuples.append(tuple3)
list_of_tuples.append(tuple4)
list_of_tuples.append(tuple5)
list_of_tuples.append(tuple6)

#displaying the list
print("---------------------------------------------------------------------------------------------")
print("the final list!!")
print("---------------------------------------------------------------------------------------------")
print(list_of_tuples)
print("##############################################################################################")

#displaying the tuples within the list of tuples
print("---------------------------------------------------------------------------------------------")
print("tuples within the list of tuples")
print("---------------------------------------------------------------------------------------------")
for i in list_of_tuples:    
    print(i)