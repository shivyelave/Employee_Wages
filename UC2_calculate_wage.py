from UC1_attendance import employee_attendance
from UC3_part_time_wages import calculate_part_time_wage_of_employee
def calculate_wage_of_employee():
    attendance = employee_attendance()
    if attendance == 0:
        return 0
    if attendance == 2:
        return 20*8
    if attendance == 1:
        return calculate_part_time_wage_of_employee()

def main():
    print(calculate_wage_of_employee())
if __name__ == '__main__':
    main()