import socket
import operator

# Define possible math symbols and assign appropriate operation 
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "%": operator.mod}

# Define host/port variables - given to us in the problem
host = "204.48.18.4"
port = 40000

# Honestly not entirely sure what this does, but it lets us connect to our defined host/port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    res = s.recv(1024).decode("utf-8")
    print(res)

# If it finds CYHI in the last line, stop and print the line
    if "CYHI{" in res:
        print("Flag found:", res)
        break
# Else, if it finds "Expression, strip out everything after ": " (the equation) and perform and print the math
    if "Expression" in res:
        expression = res.split(": ")[1].strip()
        nums = expression.split(' ')
        result = ops[nums[1]](int(nums[0]), int(nums[2]))
        print(result)
# Send the math result back to the server so it will then send a new problem
        s.send((str(result) + "\n").encode("utf-8"))
