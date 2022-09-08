# Functional Programmming a programming prodigy that states that computations should be treated by the
# evaluation of mathematical funcitons
# lambda func us the lambda keywords, they arent named 

add = lambda x: x+5
# print(add(7))

lambda_func = [lambda x: x+j for j in range(3)] 
first_lambda = lambda_func[0]
print(first_lambda(5))

multiply = lambda a,b,c: a*b*c
print(multiply(11,22,44))
