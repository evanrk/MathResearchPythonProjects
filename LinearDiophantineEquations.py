class Coef():
    def __init__(self, coef, expression):
        self.coef = coef
        self.expression = expression


# def simplify(expression):
#     print(toList(expression))
#     if type(expression) == list:
#         simplifiedList = []
#         for element in expression:

#         # return 
#         # return [simplify(element) for element in expression]
#     if type(expression.expression) == Coef:
#         expression.expression.coef *= expression.coef
#         return simplify(expression.expression)
#     else:
#         return expression

def simplify(expression):
    if type(expression.expression) == list:
        scaledList = []
        for element in expression.expression:
            simplifiedElement = simplify(element)
            scaledElement = Coef(simplifiedElement.coef * expression.coef, simplifiedElement.expression)
            scaledList.append(scaledElement)
        return scaledList
    elif type(expression.expression) == Coef:
        expression.expression.coef *= expression.coef
        return simplify(expression.expression)
    else:
        return expression


def toList(expression):
    if type(expression) == list:
        return [(toList(element) if type(element) != int else [element]) for element in expression]
    elif type(expression.expression) == Coef:
        return [expression.coef, toList(expression.expression)]
    else:
        return [expression.coef, expression.expression]


# testExpression1 = Coef(5, Coef(2, Coef(1, Coef(3, "x"))))
testExpression1 = Coef(5, Coef(1, [
    Coef(2, Coef(7, "y")),
    Coef(4, "x")
]))
# 5 * ( 1 * ( 2 * (7y + 4x)))
print(toList(simplify(testExpression1)))
