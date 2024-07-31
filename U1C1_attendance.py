import random

def employee_attendance():
    attendance = random.choice([0,1,2])
    if attendance == 0:
        return 0
    if attendance == 1:
        return 1
    if attendance == 2:
        return 2
    
def main():
    print(employee_attendance())
if __name__ == '__main__':
    main()