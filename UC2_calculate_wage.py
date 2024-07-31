'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Calculate Wage of Employee


'''

from UC1_attendance import employee_attendance
from UC3_part_time_wages import calculate_part_time_wage_of_employee

def calculate_wage_of_employee():
    
    """

    Description:
        Function to calculate the wage of an employee based on their attendance.

    Returns:
        int: The wage of the employee based on their attendance:
            - 0 for no attendance
            - 20*8 for full day attendance
            - Part-time wage for half-day attendance
    
    """
    
    attendance = employee_attendance()  # Get attendance status from employee_attendance function

    if attendance == 0:
        return 0  # No attendance, no wage

    if attendance == 2:
        return 20 * 8  # Full-day attendance, wage for 8 hours at $20/hour

    if attendance == 1:
        return calculate_part_time_wage_of_employee()  # Half-day attendance, part-time wage

def main():
    print(calculate_wage_of_employee())  # Print the calculated wage of the employee

if __name__ == '__main__':
    main()
