import re

class Polynomial:
    """Represents a polynomial.

    Takes as input a polynomial in standart algebraic
    notation or as a dict instance and constructs its class-based 
    representation.

    polynomial    a string representing a polynomial 
                  in standard algebraic notation
                  (e.g. '2*x^2 + 3*x - 2')
    """

    pattern = (r"\s*(?P<sign>[-+]?)\s*(?P<factor>\d*\.?\d*)\s*"
               r"\*?\s*(?P<variable>[a-z]?)\s*(\^\s*(?P<power>(-[1-9])?[1-9]*\d*))?")
    regex = re.compile(pattern)

    def __init__(self, polynomial):
        if isinstance(polynomial, str):
            self.variable = None
            self._dict_repr = {}
        
            matches = self.regex.finditer(polynomial)
            for match in matches:
                member = match.groupdict()
                if member["power"] is None:
                    member["power"] = ""
                
                if self.variable is None and member["variable"]:
                    self.variable = member["variable"]
                
                if not member["sign"] + member["factor"] + member["power"]:
                    continue
            
                member["factor"] = member["factor"] if member["factor"] else 1
                if not member["power"]:
                    if member["variable"]:
                        member["power"] = 1
                    else:
                        member["power"] = 0
                self._dict_repr[float(member["power"])] = float(f"{member['sign']}{member['factor']}")
        elif isinstance(polynomial, dict):
            self._dict_repr = polynomial
            self.variable = "x"

    @staticmethod        
    def _to_str(dict_, variable):
        polynomial = ""
        for power in sorted(dict_.keys(), reverse=True):
            
            sign = "+ " if dict_[power] > 0 else "- "
            polynomial += sign

            factor = abs(dict_[power])
            if factor == 1:
                if power == 0:
                    polynomial += "1 "
                elif power == 1:
                    polynomial += f"{variable} "
                else:
                    polynomial += f"{variable}^{power} "
            else:
                if power == 0:
                    polynomial += f"{factor} "
                elif power == 1:
                    polynomial += f"{factor}*{variable} "
                else:
                    polynomial +=  f"{factor}*{variable}^{power} "
        if polynomial[0] == "-":
            minus = True
        else:
            minus = False
        polynomial = polynomial.strip("+- ")
        if minus:
            polynomial = "-" + polynomial
        return polynomial

    def __str__(self):
        return self._to_str(self._dict_repr, self.variable)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__str__()}')"
    
    def get_derivative(self):
        derivative_dict = {power - 1 : power * factor for power, factor
                           in self._dict_repr.items() if power != 0}
        return self.__class__(self._to_str(derivative_dict, self.variable))


if __name__ == "__main__":
    poly = Polynomial("-10.0*a^6.0 + 7.0*a^5.0 - 4.0*a^3.0 - 2.0*a^2.0 + a - 1")
    print("polynomial: ", poly)
    print("derivative: ", poly.get_derivative())
    poly = Polynomial({5: 4, 4: 5, 3: -1, 2: 0, 1: 1, 0: 5})
    print("dict_polynomial: ", poly)
    print(poly.get_derivative())
