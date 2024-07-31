'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Calculate Part-Time Wage of Employee


'''

def calculate_part_time_wage_of_employee():

    """

    Description:
        Function to calculate the wage of an employee for part-time work.
        This assumes a fixed part-time wage for 4 hours of work.

    Returns:
        int: The total wage for part-time work, calculated as 4 hours * $20/hour.
    
    """
    
    return 4 * 20  # Wage for 4 hours of work at $20 per hour

def main():
    print(calculate_part_time_wage_of_employee())  # Print the calculated part-time wage

if __name__ == '__main__':
    main()
