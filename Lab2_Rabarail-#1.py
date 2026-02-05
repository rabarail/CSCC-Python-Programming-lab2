"""Program name: Tip Calculator
AUthor: Rajani Baraili
Purpose: Calculate 15% and 20% tip suggestions and totals for dinner bill.
Starter code: None
Date:02/04/2026"""
print("Please, enter the total bill amount:")
bill = float(input())
tip15 = bill *.15
tip20 = bill *.20
total15=bill +tip15
total20 =bill+tip20
print(f"Suggested amount of tip for 15%: ${tip15}")
print(f"Suggested amount of tip for 20%: ${tip20}")