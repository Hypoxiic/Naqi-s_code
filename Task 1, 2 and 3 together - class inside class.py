from multiprocessing import connection
import random  # This is the import random command.
import sys
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


def main():
    test()
main()


class Databases:

    class Class1:

        file = open("Class 1.csv", "r")

        connection = lite.connect("scores1.database")


        def table(self, file=None):
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


        def normal_scores(self):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Scores_1")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)


        def highscore(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Scores_1 ORDER BY Score DESC")
                rows = cursor.fetchall()
          
                for row in rows:
                    print(row)

            file.close()


        def individual_highscore(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Name, MAX(Score) AS HighScore FROM Scores_1 GROUP BY Name")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def average(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Name, AVG (Score) AS ScoreAverage FROM Scores_1 GROUP BY Name")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def alphabetical(self, cursor=None, file=None):
            with connection:
                cursor.execute("SELECT * FROM Scores_1 ORDER BY (Name)")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


    class Class2:

        file = open("Class 2.csv", "r")

        connection = lite.connect("scores2.database")


        def table(self, file=None):
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


        def normal_scores(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * from Scores_2")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def highscore(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Scores_2 ORDER BY Score DESC")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def individual_highscore(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Name, MAX(Score) AS HighScore FROM Scores_2 GROUP BY Name")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def average(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Name, AVG (Score) AS ScoreAverage FROM Scores_2 GROUP BY Name")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def alphabetical(self, cursor=None, file=None):
            with connection:
                cursor.execute("SELECT * FROM Scores_1 ORDER BY (Name)")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()

    class Class3:

        file = open("Class 3.csv", "r")

        connection = lite.connect('scores3.database')


        def table(self, file=None):
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


        def normal_scores(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * from Scores_3")
                rows = cursor.fetchall()

                for row in rows:
                        print(row)

            file.close()


        def highscore(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Scores_3 ORDER BY Score DESC")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def individual_highscore(self):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Name, MAX(Score) AS HighScore FROM Scores_3 GROUP BY Name")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

        file.close()


        def average(self, file=None):
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Name, AVG (Score) AS ScoreAverage FROM Scores_3 GROUP BY Name")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()


        def alphabetical(self, cursor=None, file=None):
            with connection:
                cursor.execute("SELECT * FROM Scores_1 ORDER BY (Name)")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

            file.close()

x = Databases.Class1
y = Databases.Class2
z = Databases.Class3


def option_scores_():

    option_scores = input("Which class would you like to view the data for? ")

    if option_scores == '1':
        Databases.Class1.normal_scores()
    elif option_scores == '2':
        Databases.Class2.normal_scores()
    elif option_scores == '3':
        Databases.Class3.normal_scores()


def option_highscores_():

    option_highscores = input("Which class would you like to view the data for? ")

    if option_highscores == '1':
        Databases.Class1.highscore()
    elif option_highscores == '2':
        Databases.Class2.highscore()
    elif option_highscores == '3':
        Databases.Class3.highscore()


def option_individual_highscores_():

    option_individual_highscore = input("Which class would you like to view the data for? ")

    if option_individual_highscore == '1':
        Databases.Class1.individual_highscore()
    elif option_individual_highscore == '2':
        Databases.Class2.inidividual_highscore()
    elif option_individual_highscore == '3':
        Databases.Class3.individual_highscore()


def option_average_():

    option_average = input("Which class would you like to view the data for? ")

    if option_average == '1':
        Databases.Class1.average()
    elif option_average == '2':
        Databases.Class2.average()
    elif option_average == '3':
        Databases.Class3.average()


def option_alphabetical_():

    option_alphabetical = input("Which class would you like to view the data for? ")

    if option_alphabetical == '1':
        Databases.Class1.alphabetical()
    elif option_alphabetical == '2':
        Databases.Class2.alphabetical()
    elif option_alphabetical == '3':
        Databases.Class3.alphabetical()


print("If you would like to do the test again type 'run'. ")
print("If you would like to end the program  type 'exit'. ")
print("If you would like to view the scores for a certain class type 'scores'. ")
print("If you would like to view the highscores for a certain class type 'highscores'. ")
print("If you would like to view the individual highscores for a certain class type 'individual highscores'. ")
print("If you would like to view the averages for everyone in the class type 'average'. ")
ending_options = input("Please enter which option you would like to choose: ")

if ending_options == 'run':
    test()
elif ending_options == 'exit':
    sys.exit(0)
elif ending_options == 'scores':
    option_scores_()
elif ending_options == 'highscores':
    option_highscores_()
elif ending_options == 'individual highscores':
    option_individual_highscores_()
elif ending_options == 'average':
    option_average_()
elif ending_options == 'alphabetical':
    option_alphabetical_()