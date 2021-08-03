# Create a class
class Appliance:
    #Define the attributes of the class
    name = "No name provided"
    brand = ""
    model = ""
'''
    Did not know if we had to provide this info for the assignment
    as it only specified creating a class and two child classes
    
    #Define the methods of the class
    def search(self):
        entry_brand = input("Enter your appliance brand: ")
        entry_model = input("Enter your appliance model: ")
        if (entry_brand == self.brand and entry_model == self.model):
            print("Your appliance name: {}".format(self.name))
        else:
            print("Your appliance cannot be found.")
# Create an instance of the Appliance class
new_appliance = Appliance()
# Call the seach method using the new object
new_appliance.search()
'''



# Create two child classes that have at least two of their own attributes
class Kitchen(Appliance):
    forFoodOrNoFood = ""
    dryOrWetFood = ""
class Laundry(Appliance):
    forWashingOrDrying = ""
    washerOrDryer = ""
