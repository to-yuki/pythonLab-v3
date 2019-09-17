import BMI

#-- Main-Satrt --#
def main():
	weight = 75.0
	height = 1.75
	bmi_val = BMI.bmi(weight,height)

	print(bmi_val)
#-- Main-End --#

if __name__ == '__main__':
	main()
