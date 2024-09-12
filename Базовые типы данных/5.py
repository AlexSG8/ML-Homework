num=input()
if num.isdigit() or (num.find(".") != -1 and num[-1] != "."):
	print("True")
else:
	print("False")

