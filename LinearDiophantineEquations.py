class Coef():
    def __init__(self, coef, expression):
        self.coef = coef
        self.expression = expression

def replaceExpression(expression, searchTerm, replaceTerm):
    print(replaceTerm)
    if type(expression) == list:
        return [(replaceExpression(element, searchTerm, replaceTerm)) for element in expression]
        # for element in expression:
        #     return replaceExpression(element, searchTerm, replaceTerm)
    elif type(expression) == Coef:
        return Coef(expression.coef, replaceExpression(expression.expression, searchTerm, replaceTerm))
    else:
        if expression == searchTerm:
            return replaceTerm
        else:
            return expression

 
testExpression3 = Coef(2, [Coef(3, 1), Coef(3, 1)])

def simplifyMultiplied(expression):
    if type(expression.expression) == list:
        scaledList = []
        for element in expression.expression:
            simplifiedElement = simplifyMultiplied(element)
            if type(simplifiedElement) == list:
                for secondIter in simplifiedElement:
                    secondScaledElement = Coef(secondIter.coef * expression.coef, secondIter.expression)
                    scaledList.append(secondScaledElement)
            else:
                scaledElement = Coef(simplifiedElement.coef * expression.coef, simplifiedElement.expression)
                scaledList.append(scaledElement)
        return scaledList
    elif type(expression.expression) == Coef:
        expression.expression.coef *= expression.coef
        return simplifyMultiplied(expression.expression)
    else:
        return expression


def simplify(expression):
    additionSimplified = []
    multiplySimplified = simplifyMultiplied(expression)
    variables = []

    for i in multiplySimplified:
        variables.append(i.expression)

    for variable in set(variables):
        coefTotal = 0
        for expression in multiplySimplified:
            if variable == expression.expression:
                coefTotal += expression.coef
        additionSimplified.append(Coef(coefTotal, variable))

    return additionSimplified
                


# def toList(expression):
#     if type(expression) == list:
#         return [(toList(element) if type(element) != int else element) for element in expression]
#     elif type(expression.expression) == Coef:
#         return [expression.coef, toList(expression.expression)]
#     else:
#         return [expression.coef, expression.expression]


def toList(expression):
    print(expression)
    if type(expression) == list:
        return [(toList(element) if type(element) in (list, Coef) else element) for element in expression]
    elif type(expression.expression) == Coef:
        return [expression.coef, toList(expression.expression)]
    else:
        return [expression.coef, expression.expression]


# testExpression1 = Coef(5, Coef(2, Coef(1, Coef(3, "x"))))
testExpression1 = Coef(5, Coef(1, [
    Coef(2, [Coef(7, [Coef(3, "y"), Coef(1, "y")]), Coef(9, "y")]),
    Coef(4, "x")
]))

# print(toList(replaceExpression(testExpression3, 1, "x")))
print(toList(testExpression1))

import math # copied from earlier code

coef1 = int(input("Enter the first coefficient: ")) # gets the input for coef1
coef2 = int(input("Enter the second coefficient: ")) # gets the input for coef2
final = int(input("Enter the final number: ")) # gets the input for the final number

def findLinearDiophantineCoefficients(coef1, coef2, final):
    greatest_common_denominator = math.gcd(coef1, coef2) # finds the gcd
    if final%greatest_common_denominator != 0:
        return ""
    else:
        # since all numbers in the equation are divisible by a number, I can divide them all by that number to make it more efficient
        coef1 = coef1 // greatest_common_denominator
        coef2 = coef2 // greatest_common_denominator
        final = final // greatest_common_denominator
        for x in range(-final, final+1): # iterates for all values between negative final and positive final
            for y in range(-final, final+1):
                if coef1 * x + coef2 * y == final: 
                    # print the equations in the formula in terms of t, both coef1 and coef2 are already divided by the gcd earlier
                    return (
                        f"x = {x} + {-coef1}t",
                        f"y = {y} + {coef2}t"
                    )

print(findLinearDiophantineCoefficients(coef1, coef2, final))