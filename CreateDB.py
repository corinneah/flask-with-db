import sqlite3
# import packages

connect = sqlite3.connect('patients.db')
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            city CHAR(25) NOT NULL,
            insurance CHAR(25) NOT NULL,
        ); """

db.execute(table) 
connect.commit() 

#insert data into table 
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance,) values('13456', 'Cindy', 'Harrison', 'F', '06/01/2003', 'Bronx', 'United Healthcare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance,) values('78567', 'Jessica', 'Robins', 'F', '07/28/2005','New York', 'United Healthcare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance,) values('23487', 'Dean', 'Woody', 'M', '12/25/2005','Brooklyn', 'BlueCross')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance,) values('65429', 'Harry', 'Will', 'M', '03/07/2010','New York', 'Fidelis')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance,) values('47894', 'Jane', 'Doe', 'F', '10/21/2000','New York', 'Health First')")

connect.commit()


# close the connection
connect.close()
