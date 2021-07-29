import random is r
import string
length = 6
otp = ' '
charecters=string.ascii_letters + string.digits
for i in range(length):
otp=otp+r.choice(charecters)
print("OTP : ",otp)
