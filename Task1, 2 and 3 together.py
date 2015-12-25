import random  # This is the import random command.
import sys
import os.path
import sqlite3 as lite 


def test():
    name_check = False
    while name_check == False:
        name = input("What is your name? ")  #This is an input command asking the user for their name
        if name.isalpha():
            name_check = True
        else:
            print("This is not a letter, please enter a valid name.")
    print("Welcome", name + "!")  #This is the print command. It prints the user's name.
    print("You will have 10 questions, good luck. ")  #Print command.

    test_score = 0 #This is assigning the variable 'test_score'.
    test_start = 0 #This is assigning the variable 'testStart'.
    test_end = 10  #This is assigning the variable 'testEnd'.

    while test_start < test_end:  #This is a while loop that will run so as long as the 'testStart' is smaller than the 'testEnd'.
        test_start +=  1  #This line dictates how the while loop runs.
    #It starts off at the variable 'testStart' and then goes by 1 each time the loop runs.

        operations = ("+", "-", "*")  #This line contains the three mathematical operations (+, -, *) that i assigned to this variable.
        a = random.randrange(1, 11)  #This line is one of the two variables in the arithmetic questions.
        #This number is always randomly generated using the 'random.randrange' function. It is from 1, 11 because using the 'random.randrange' function means you need to put the y value one higher than you actually desire (where (1,11) is (x,y)).
        b = random.randrange(1, 11)  #This is doing the same but for the variable 'b'.
        operator = random.choice(operations)  #I use the 'random.choice' function to take a random result from the mathematical operations and assign it to
        #the variable 'operator'.

        if operator == "*":  #Beginning of 'if' statement.
            ans = a * b  #This is the mathematical calculation that will happen if the 'if' statement is fulfilled. Meaning if the 'operator' is a multiplication.
        elif operator == "-":  #This is an 'else if' statement (elif), if the 'if' statement isn't fulfilled then it will go to the elif statement.
            ans = a - b  #Another mathematical calculation that will happen if the 'operator' is a subtraction.
        elif operator == "+":  #Another 'elif' statement.
            ans = a + b

        print("{}{}{}".format(a, operator, b))  #This is telling the program to print in the curly brackets according to the format.
        x = (ans)
        ans_check = True
        while ans_check == True:
            try:
                y = int(input("Please enter your answer here: "))
                ans_check = False
            except ValueError:
                print("This is not an integer!")
        if x == y:  #This 'if' statement is saying that if the answer (x) is equal to y, the tell the user that they got it correct.
            print("Correct!")
            test_score = test_score + 1  #This is adding one to the overall score every time the user gets an answer correct.
        else:  #This 'else' statement is executed if the 'if' statement is not fulfilled.
            print("Wrong!")  #Another print command...

    print("Your score is",test_score, "out of 10.")  #This is telling the user at the end of the game what their score is using the print command.
    print("Thank you for taking the test.")  #Another print command...

    class_1_file = open("Class 1.csv", "a")
    class_2_file = open("Class 2.csv", "a")
    class_3_file = open("Class 3.csv", "a")
    student_name = name
    score = test_score
    class_check = False
    while class_check == False:
        class_number = input("What class are you in? ")
        if class_number == "1" or class_number == '2' or class_number == "3":
            class_check = True
        else:
            print("This is not an integer, nor between 1-3. Please enter a number from 1-3.")

    if class_number == "1":
        class_1_file.write(student_name + "," + str(score) + "\n")
    elif class_number == "2":
        class_2_file.write(student_name + "," + str(score) + "\n")
    elif class_number == "3":
        class_3_file.write(student_name + "," + str(score) + "\n")

    class_1_file.close()
    class_2_file.close()
    class_3_file.close()


class Databases:
    def class_1():

        file = open("Class 1.csv", "r")

        connection = lite.connect("scores.database")

        with connection:
            cursor = connection.cursor()
            #cursor.execute('CREATE TABLE Scores_1 (Name TEXT, Score INT)')
            cursor.execute("DROP TABLE Scores_1")
            cursor.execute("CREATE TABLE Scores_1 (Name TEXT, Score INT)")
            

            for line in file:
                columns = line.split(",")
                name = columns[0]
                score = columns[1]

                cursor.execute("INSERT INTO Scores_1 (Name, Score) VALUES ('"+name+"', "+score+")")

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Scores_1")
            rows = cursor.fetchall()    

            for row in rows:
                print(row)

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Scores_1 ORDER BY Score DESC")
            rows = cursor.fetchall()
          
            for row in rows:
                print(row)

        file.close()
        
    def class_2():
        file = open("Class 2.csv", "r")

        connection = lite.connect("scores.database")

        with connection:
            cursor = connection.cursor()
            #cursor.execute('CREATE TABLE Scores_2 (Name TEXT, Score INT)')
            cursor.execute("DROP TABLE Scores_2")
            cursor.execute('CREATE TABLE Scores_2 (Name TEXT, Score INT)')
            

            for line in file:
                columns = line.split(",")
                name = columns[0]
                score = columns[1]

                cursor.execute("INSERT INTO Scores_2 (Name, Score) VALUES ('"+name+"', "+score+")")

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Scores_2")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

        file.close()

    def class_3():
        file = open("Class 3.csv", "r")

        connection = lite.connect('scores.database')

        with connection:
            cursor = connection.cursor()
            #cursor.execute('CREATE TABLE Scores_3 (Name TEXT, Score INT)')
            cursor.execute("DROP TABLE Scores_3")
            cursor.execute('CREATE TABLE Scores_3 (Name TEXT, Score INT)')
            

            for line in file:
                columns = line.split(",")
                name = columns[0]
                score = columns[1]

        file.close()


    #option = input('Which class would you like to view the data for? ')
    #if option == '1':
      #  class_1()
   # elif option == '2':
    #    class_2()
   # elif option == '3':
    #    class_3()


    def ending_options():

        print("If you would like to do the test again type 'run'.")
        print("Or if you would like to end the program now type 'exit'.")
        print("Or if you would like to view the scores for a certain class, input its respective number.")
        options = input("Please input the option you would like to run: ")

        if options == 'run':
            test()
        elif options == 'exit':
            sys.exit(0)
        elif options == '1':
            Databases.class_1()
        elif options == '2':
            Databases.class_2()
        elif options == '3':
            Databases.class_3()


def main():
    test()
    Databases.ending_options()
main()
