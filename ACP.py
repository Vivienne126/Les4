num=int(input("Enter the number"))
str_num=str(num)
length=len(str_num)
print(f"There are {length} digits in the number {num}")
total=0

for i in str_num:
    total=total+int(i)**length

if total==num:
    print(f"{num} is an amstrong number")
else:
    print(f"{num} is not an amstrong number")

