n = int(input())
s = input()

stack = []
for i in range(len(s)):
	c = s[i]
	if (c == '(' or c == '{' or c == '['):
		stack.append(c)
	elif (c == ')'):
		if stack and stack[-1] == '(':
			stack.pop()
		else:
			print(")",i)
	elif c == "}":
		if stack and stack[-1] == "{":
			stack.pop()
		else:
			print("}",i)
	elif c == "]":
		if stack and stack [-1] == "[":
			stack.pop()
		else:
			print("]",i)

else:
	print("ok so far")
