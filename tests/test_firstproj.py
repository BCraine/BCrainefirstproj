import main
import pytest


def test_get_data():
    result = main.get_data(url="https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,"
                               "3&fields=id,school.state,school.city,school.name,2018.student.size,2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size")
    count = 0
    for element in result:
        count +=1
        return count

    assert count > 1000



def test_database():
   conn, cursor = main.open_db("db_test.sqlite")
   print(type(conn))
   main.setup_db(cursor)
   all_data = []

   for item in all_data:
       main.make_database_data(cursor, "test_school",
                               "test_city",
                               "test_state",
                               "test_2018_size",
                               "test_2017_size",
                               "test_2017_poverty",
                               "test_2016_repayment")
       assert all_data[0] == "test_school"







   main.close_db(conn)

