# Programming Assignment #7

## Description
Process credit card data in a file and produce a report
## Instructions
1. Write a program to read through a file of unknown length, i.e., use a sentinel-controlled while loop. The data in the file contains credit card numbers. You must identify whether or not the number is a valid credit card number. If it is a valid number, identify what type of credit it is. If it is invalid, simply state such.

	Credit card numbers follow certain patterns. It must be between 13 and 16 digits. It also must begin with:
	- 4 for Visa cards
	- 5 for MasterCard cards
	- 37 for American Express cards
	- 6 for Discover cards
	 
	Read the data one line at a time. Stop reading when a credit card of “99999” is read.
The name of the input file must be “pa7.cards”

	In addition to length and beginning numbers, there is an algorithm for determining whether a card is valid.
It is described below:

	1. Double every second digit from right to left. If this “doubling” results in a two-digit number, add the two-digit number to get a single digit. For example, in the first credit card number in the file below, you would double the numbers: 2 2 4 1 6 5 8 4 The 6, 5 and 8 cause you to do the second step of adding digits. This means you would add: 4 4 8 2 3 1 7 8
	2. Now, add all of the single digit numbers from step 1.
	3. Add all digits in the odd places from right to left. For example, in the first credit card number in the file below, you would add the numbers: 6 6 0 8 0 7 8 3
	4. Sum the results from steps 2 and 3. The sum of #2 should be 37; sum of #3 should be 38. Total is 75.
	5. If the result from step 4 is evenly divisible by 10, the credit card number is valid; otherwise it is invalid. Since 75 is not evenly divisible by 10, the first entry in this file is an invalid credit card number.

2. Required Functions

	You must have a minimum of five(5) programmer-defined functions, in addition to **main()**.
	
	Some suggestions are:
	
	**CheckLen(num):**
This function is passed one(1) parameter, which is the credit card number. It will check the length of the credit card number and return True if it is a valid length; False otherwise.

	**DetermineType(num):**
This function is passed one(1) parameter, which is the credit card number. It will determine what type of credit card it is (Visa/MC/AmEx/Disc) and return that type. You can decide how that type is returned; as a string or as a numeric.

	You think of some others :-)

## Sample Run
	Number Valid/Invalid Type
	-----------------------------------------------------
	4388576018402626 Invalid
	4388576018410707 Valid Visa
	37271983 Invalid
	5190828258102121 Valid MasterCard