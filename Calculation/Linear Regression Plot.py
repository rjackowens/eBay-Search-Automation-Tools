import matplotlib.pyplot as plt 

# Define Independent and Dependent Variables; This is a test data set for curta calculators
            
x = 873 # Average Sold Price
y = 950 # Average Active Price  
 

# Set Default Figure Size
plt.rcParams["figure.figsize"] = (10,5) 

plt.plot(x, label="Independent Variable")
plt.plot(y, label="Dependent Variable")
plt.ylabel("Value in $")
plt.legend()
plt.show()      