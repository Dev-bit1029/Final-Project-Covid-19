import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

print("====================")
print("COVID-19 REPORT")
print("====================")

print("1. Explore Data ")
print("2. Clear Data ")
print("3. Perfirm Data Analysis ")
print("4. Visualization Data ")
print("5. Data Analysis Report ")

choice = int(input("Enter The Number Between (1-5) :- "))

print("===== Load Data ===== ")

data = input("Enter The File Name Eg(covid.csv) :- ")
data = pd.read_csv(data)
print("Data Added Seccessfully ! ")


if choice == 1 :
    
    print("====== Explore Data ======")
    print("1. Top 5 Entry ")
    print("2. Last 5 Entry ")
    print("3. Information About Covid 19")
    print("4. Check Datatype ")
    
    choice = int(input("Enter The Number Between (1-4) :- "))
    
    if choice == 1:
        print(data.head(5))
    elif choice == 2 :
        print(data.tail(5))
    elif choice == 3 :
        print(data.info())
    elif choice == 4:
        print(data.dtypes)
    else:
        print("Invalid Choice Between (1-4) ")
        
         
elif choice == 2 :
    print("===== Clear Data =====") 
    print("1. Check Miss Data ")
    print("2. Handal Missing Data ")
    print("3. Show Dulicate Data ")
    
    choice = int(input("Enter The Number Between (1-3) :- "))
    
    if choice == 1 :
        data = data.isnull().sum()
        print("All Data Here ")
        print(data)
        
    elif choice == 2:
        
        print("===== Handal Missing Data ")
        print("1. Deleted All Missing Data ")
        print("2. Fill All Missing Data ")
        
        choice = int(input("Enter The Number between (1-2) :- "))
        
        if choice == 1 :
            data = data.dropna().sum()
            print("Deleted All Entry Seccessfully !")
            print(data)
        elif choice == 2 :
            fill = input("Enter The Word/Number To Fill All Entry :-  ")
            data = data.fillna(fill)
            print("All Entry Fill Seccessfully !")
            print(data)
        else :
            print("Invalid Choice Between (1-2) !")
            
    elif choice == 3:
            print(data.duplicated())
        
    else :
        print("invalid Choice Between (1-3) ! ")
        
       
elif choice == 3:
    print("===== Data Analysis =====")
    print("1. Total Deaths (Per Days) ")
    print("2. Average Deaths  (Per Days) ")
    print("3. Maximum Deaths (Per Days) ")
    print("4. Minimum Deaths (Per Days) ")
    
    chioce = int(input("Enter The Number Between (1-5) :- "))
    
    if choice == 1 :
        print(data["Deaths"].sum())
    elif choice == 2 :
        print(data["Deaths"].mean())
    elif choice == 3 :
        print(data["Deaths"].max())
    elif choice == 4 :
        print(data["Deaths"].min())

    else:
        print("Invalid Choice Between (1-5) ! ")
        
    
elif choice == 4 :
    print("===== Visualization Data =====")
    print("1. Bar Graph (Per Days) ")
    print("2. Line Graph (Per Days) ")
    print("3. Pie Graph (Per Days) ")
    print("4. Histogram Graph (Per Days) ")
    print("5. Scatter Graph (Per Days) ")
    
    choice = int(input("Enter The Number Between (1-5) :- "))
    
    if choice == 1:
        data.head(10).plot.bar(x="Country_Region" , y="Deaths")
        plt.show()
    
    elif choice == 2 :
        data.head(10).plot.line(x="Country_Region" , y="Deaths")
        plt.show()
    
    elif choice == 3:
        data.head(10).plot.pie(y="Deaths", labels=data["Country_Region"])
        plt.show()
        
    elif choice == 4:
        data.head(10).plot.hist(y="Deaths")
        plt.show()
        
    elif choice == 5:
        data.head(10).plot.scatter(x="Country_Region" , y="Deaths")
        plt.show()
        
    else :
        print("Invalid Choice Between (1-5) ! ")
        

elif choice == 5 :
    print("===== DATA ANALYSIS REPORT =====")
    print("1. Total Deaths :- ",data["Deaths"].sum())
    print("2. Average Deaths :- ",data["Deaths"].mean())
    print("3. Maximum Deaths :- ",data["Deaths"].max())
    print("4. Minimum Deaths :- ",data["Deaths"].min())
    
else :
    print("Invalid Choice Between (1-5) ! ")
