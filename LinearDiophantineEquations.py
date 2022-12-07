class Coef():
    def __init__(self, coef, expression):
        self.coef = coef
        self.expression = expression
    

def simplify(expression):
    if type(expression.expression) != int:
        simplify(expression.expression).coef += expression.coef
        print(toTuple(expression.expression))
        return expression.expression
    else:
        print(toTuple(expression))
        return expression


def toTuple(expression):
    if type(expression.expression) != int:
        return (expression.coef, toTuple(expression.expression))
    else:
        return (expression.coef, expression.expression)

testExpression1 = Coef(2, Coef(1, Coef(5, 5)))
testExpression2 = Coef(3, Coef(3, Coef(1, (5, (Coef(2, 5), Coef(2, 3))))))

print(toTuple(simplify(testExpression1)))