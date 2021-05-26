from openpyxl import load_workbook #package to open .xlsx file
import numpy as np
from matplotlib import pyplot as plt
import os

# Before running program, needs
# Python 3 installed
# pip install openpyxl
# pip install numpy
# pip install matplotlib

# Person object that will hold the data for each SubID
class person:
    def __init__(self, subID, ratings, gender, age, height, weight):
        self.subId = subID
        self.ratings = ratings #list of the ratings 
        self.gender = gender
        self.age = int(age)
        self.height = height
        self.heightInches = self.height_to_inches(height)
        self.weight = int(weight)
        self.bmi = self.body_mass_index()
    
    # Question 1
    def body_mass_index(self):
        return (self.weight/self.heightInches**2) * 703

# function to take a height and convert it to inches
    def height_to_inches(self, height):
        seperator = height.split("'")
        feet = float(seperator[0])
        inches = float(seperator[1])
        return feet*12 + inches

    def __str__(self):
        return "SubID: " + str(self.subId) + " Ratings: " + str(self.ratings) + " Gender: " + self.gender + " Age: " + str(self.age) + " Height: " + self.height + " Weight: " + str(self.weight) + " BMI: " + str(self.bmi)
# end class person



# Question 2
def q2(people):
    question2 = [] # Will hold a list of people that meet criteria of Q2
    for p in people:
        ratings_count = 0
        for rating in p.ratings:
            if rating is not None:
                ratings_count += 1
            if ratings_count > 2:
                break  
        if p.age >= 21 and ratings_count >= 3:
            question2.append(p)
    return question2

# Question 3
def q3(people):
    question3 = {} # Will be a dictionary of the averages of each rating
    for i in range(1, 10):
        temp = []
        for p in people:
            value = p.ratings[i-1]
            if value is None: # math is hard when some of the values are empty, so this temporarily sets empty values to 0
                value = 0
            temp.append(value)
        question3['Img_rating_' + str(i)] = np.average(temp)
    return question3

# Question 4
def q4(people):
    pass

# Question 5
def q5(people):
    for p in people:
        plt.scatter(p.age, p.heightInches, color = "#010000" )
    plt.title("Correlation Graph")
    plt.xlabel("Age")
    plt.ylabel('Height in Inches')
    # Uncomment the line below to show the graph
    # plt.show()

# Question 6
def q6(people):
    men = []
    women = []
    # Seperates by gender
    for p in people:
        if p.gender == "Male":
            men.append(p)
        elif p.gender == "Female":
            women.append(p)
        else:
            print("Invalid Gender")
    sortedMen = sorted(men, key=lambda x: x.age, reverse=False) # Sorts the Men by age ascending
    sortedWomen = sorted(women, key=lambda x: x.age, reverse=False) # Sorts the Women by age ascending
    filename = "Q6_Output_"+ str(len(os.listdir())) + ".txt"
    # Writing to the .txt file
    f = open(filename, "w+")
    f.write("---Men---"+"\n")
    for m in sortedMen:
        f.write(str(m)+"\n")
    f.write("---Women---"+"\n")
    for w in sortedWomen:
        f.write(str(w)+"\n")
        


if __name__ == "__main__":
    data = load_workbook(r"Mock_Qualtrics_Data (1).xlsx") #loads in the .xlsx file
    sheet = data.active
    rows = sheet.rows
    headers = [cell.value for cell in next(rows)]
    
    all_rows = [] # Will be a list of all the rows in the file
    people = [] # Will be a list of each person

    for row in rows:
        data = {}
        for title, cell in zip(headers, row):
            data[title] = cell.value
        all_rows.append(data)
    
    for row in all_rows: # For each loop that skips the first row since the first row is the headers
        ratings = []
        for x in range(1, 10):
            ratings.append(row['Img_rating_' + str(x)])
        people.append(person(row['SubID'], ratings, row['Gender'], row['Age'], row['Height'], row['Weight'])) # Person object that holds the information of each column

    # people is a Python list of all the people or SubIDs 
    # So for example if you want to see SubID 1 you do people[0] Python uses Zero based indexing
    # Question 2 shows how to loop through people
    # To see SubID 1's Gender, do print(people[0].gender)

    #functions above
    print("-----Data-----")
    for p in people:
        print(p)
    print("-----Question 2-----")
    question2 = q2(people) # Holds a list of people that meet the criteria for question 2
    for p in question2:
        print(p)
    print("-----Question3-----")
    question3 = q3(people) # Holds a dictionary of the ratings that hold the average for each rating
    print(question3)
    q5(people)
    q6(people)
    
    
   

