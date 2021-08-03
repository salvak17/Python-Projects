
# Create a parent class
class Patient:
    fname = "Unknown"
    lname = "Unknown"
    species = "Unknown"
    gender = "Unknown"
    age = 0
    # Method
    def getInfo(self):
        msg = "\nFirst Name: {}\nLast Name: {}\nSpecies: {}\nGender: {}\nAge: {}".format(self.fname,self.lname,self.species,self.gender,self.age)
        return msg

# Create a child class
class Dog(Patient):
    fname = "Kala"
    lname = "Salva"
    species = "Canine"
    gender = "Spayed"
    age = 4
    # Two own attributes
    dogBreed = "Chihuahua Mix"
    dogSize = "Medium"
    # Polymorphism on the parent class method
    def getInfo(self):
        msg = "\nFirst Name: {}\nLast Name: {}\nSpecies: {}\nGender: {}\nAge: {}\nDog Breed: {}\nDog Size: {}".format(self.fname,self.lname,self.species,self.gender,self.age,self.dogBreed,self.dogSize)
        return msg

# Create another child class
class Cat(Patient):
    fname = "Smelly"
    lname = "Cat"
    species = "Feline"
    gender = "Spayed"
    age = 0
    # Two own attributes
    catBreed = "Medium Short Haired"
    catSize = "Medium"
    # Polymorphism on the parent class method
    def getInfo(self):
        msg = "\nFirst Name: {}\nLast Name: {}\nSpecies: {}\nGender: {}\nAge: {}\nCat Breed: {}\nCat Size: {}".format(self.fname,self.lname,self.species,self.gender,self.age,self.catBreed,self.catSize)
        return msg

# Invoke the methods inside each class for Patient, Dog, and Cat
if __name__ == "__main__":
    patient1 = Dog()
    print(patient1.getInfo())

    patient2 = Cat()
    print(patient2.getInfo())
