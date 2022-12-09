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