fields = "12345.25,6789.50"

leftNumber = fields.split(",")[0]
rightNumber = fields.split(",")[1]

try:
    result = float(rightNumber) * -1
except ValueError:
    result = float(leftNumber)

print result