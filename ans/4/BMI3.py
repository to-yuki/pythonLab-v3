import BMI # BMIモジュールのインポート

def main():
	weight = 75.0
	height = 1.75
	bmi_val = BMI.bmi(weight,height) # BMIモジュールのbmi()関数呼び出し

	print(bmi_val)

if __name__ == '__main__':
	main()
