# by using generator
def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    a,b = b,a+b

for item in fib(21):
  print(item)

# by using list

def fib2(num):
  result = [0,1]
  for i in range(2,num):
    result[i] = result[i-1]+result[i-2]
    result.append(result[i])
  return result

print(fib2(21))