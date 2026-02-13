# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    value = 0
    years = 0
    years = int(input("What are the number of years you want: "))
    for i in range (years):
        for x in range (12):
            rainfall = int(input("What was the average inches of rainfall this month?: "))
            value += rainfall
    months = years * 12
    print("Total inches of rainfall is", value)
    print("The amount of months is", months)
    print("The average inches of rainfall per month is", value / months)

if __name__ == '__main__':
    main()
