#Brandon Craine


import requests
import secrets
import sqlite3
from typing import Tuple


def get_data(url: str):
    all_data = []

    for page in range(0,161):
        full_url = f"{url}&api_key={secrets.api_key}&page={page}"


        response = requests.get(full_url)

        if response.status_code != 200:
            print(response.text)
            return []
        json_data = response.json()


        results = json_data['results']

        all_data.extend(results)

    return all_data

def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)#connect to existing DB or create new one
    cursor = db_connection.cursor()#get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS college(
    college_name TEXT NOT NULL,
    college_city TEXT NOT NULL,
    college_state TEXT NOT NULL,
    student_size_2018 INTEGER DEFAULT 0,
    student_size_2017 INTEGER DEFAULT 0,
    earnings_3yrs_after_completion_overall_count_over_poverty_line_2017 INTEGER DEFAULT 0,
    repayment_3_yr_repayment_overall_2016 INTEGER DEFAULT 0,
    PRIMARY KEY(college_name, college_city, college_state)
    );''')



def make_database_data(cursor: sqlite3.Cursor,name,city,state,size_2018,size_2017,earnings_2017,repayment_2016):

    if earnings_2017 == None:
        earnings_2017 = 0

    if repayment_2016 == None:
        repayment_2016 = 0

    if size_2017 == None:
        size_2017 = 0

    if size_2018 == None:
        size_2018 = 0

    cursor.execute('''INSERT INTO college (college_name,college_city,college_state,
    student_size_2018,student_size_2017,earnings_3yrs_after_completion_overall_count_over_poverty_line_2017,
    repayment_3_yr_repayment_overall_2016)
    VALUES(?,?,?,?,?,?,?)''',( name,city,state,size_2018,size_2017,earnings_2017,repayment_2016))




def main():

    try:

        conn, cursor = open_db("bcrainedb.sqlite")
        print(type(conn))
        setup_db(cursor)



        url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2," \
              "3&fields=id,school.state,school.city,school.name,2018.student.size," \
              "2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size"




        all_data = get_data(url)

        outfile = open('schooldata.txt', 'w')
        datastring = ','.join([str(i) for i in all_data])
        outfile.write(datastring)
        outfile.close()

        for item in all_data:
            make_database_data(cursor, item['school.name'], item['school.city'], item['school.state'],
                               item['2018.student.size'],
                               item['2017.student.size'],
                               item['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line'],
                               item['2016.repayment.3_yr_repayment.overall'])


            print(item)

        close_db(conn)




    except:
        print("delete database before running again!")








if __name__ == '__main__':
    main()