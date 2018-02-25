def gen_squares(nums):
	print("begin generator")
	for num in nums:
		yield num * num
		print("After yield")

def main():
	squares = gen_squares([1,2,3])
	print("made generator")
	for square in squares:
		print("control in caller")
		print(square)
		
main()
print("Git checking")