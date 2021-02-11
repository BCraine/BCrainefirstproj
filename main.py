#Brandon Craine


import requests
import secrets
import sqlite3
from typing import Tuple


def get_data(url: str):
    all_data = []

    for page in range(0,160):
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
    college_url TEXT PRIMARY KEY,
    college_name TEXT NOT NULL,
    college_city TEXT NOT NULL,
    college_state TEXT NOT NULL,
    student_size_2018 INTEGER DEFAULT 0,
    student_size_2017 INTEGER DEFAULT 0,
    earnings_3yrs_after_completion_overall_count_over_poverty_line_2017 INTEGER DEFAULT 0,
    repayment_3_yr_repayment_overall_2016 INTEGER DEFAULT 0
    );''')



def main():
    conn, cursor = open_db("bcrainedb.sqlite")
    print(type(conn))
    setup_db(cursor)
    close_db(conn)

    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2," \
          "3&fields=id,school.school_url,school.state,school.city,school.name,2018.student.size," \
          "2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size,"
    all_data = get_data(url)

    #outfile = open('schooldata.txt', 'w')
    #datastring = ','.join([str(i) for i in all_data])
    #outfile.write(datastring)
    #outfile.close()

    for item in all_data:
        print(item)




if __name__ == '__main__':
    main()