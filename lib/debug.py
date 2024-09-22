from __init__ import CONN, CURSOR
from department import Department

import ipdb
ipdb> Department.get_all()
ipdb> Department.find_by_id(1)
ipdb> Department.find_by_name("Payroll")


def reset_database():
    Department.drop_table()
    Department.create_table()

    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

reset_database()
ipdb.set_trace()