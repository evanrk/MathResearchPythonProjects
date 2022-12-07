class Coef():
    def __init__(self, coef, expression):
        self.coef = coef
        self.expression = expression

def simplifyMultiplication(expression):  # helper function
    if type(expression.expression) == list:
        scaledList = []
        for element in expression.expression:
            simplifiedElement = simplifyMultiplication(element)
            scaledElement = Coef(simplifiedElement.coef *
                                 expression.coef, simplifiedElement.expression)
            scaledList.append(scaledElement)
        return scaledList
    elif type(expression.expression) == Coef:
        expression.expression.coef *= expression.coef
        return simplifyMultiplication(expression.expression)
    else:
        return expression


# def simplifyMultiplication(expression):  # helper function
#     if type(expression) == list:
#         scaledList = []
#         for element in expression.expression:
#             scaledList.append(simplifyMultiplication(element))
#         return scaledList
#     elif type(expression.expression) == Coef:
#         expression.expression.coef *= expression.coef
#         return simplifyMultiplication(expression.expression)
#     else:
#         return expression


# def simplifyMultiplication(expression):
#     if type(expression.expression) == list:



def simplify(expression):
    multiplicationSimplified = simplifyMultiplication(expression)
    return multiplicationSimplified


def toList(expression):
    if type(expression) == list:
        return [(toList(element) if type(element) != int else [element]) for element in expression]
    elif type(expression.expression) == Coef:
        return [expression.coef, toList(expression.expression)]
    else:
        return [expression.coef, expression.expression]


# testExpression1 = Coef(5, Coef(2, Coef(1, Coef(3, "x"))))
testExpression1 = Coef(5, [Coef(1, [
    Coef(2, Coef(7, "x")),
    Coef(4, [
        Coef(7, "x"),
        Coef(5, "x")
    ])
])])
# 5 * ( 1 * ( 2 * (7y + 4x)))
print(toList(simplify(testExpression1)))
