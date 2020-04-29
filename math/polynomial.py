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

    pattern = (r"\s*(?P<sign>[-+]?)\s*(?P<coefficient>\d*\.?\d*)\s*"
               r"\*?\s*(?P<variable>[a-z]?)\s*(\^\s*(?P<power>(-[1-9])?[1-9]*\d*))?")
    regex = re.compile(pattern)

    def __init__(self, polynomial, variable_name=None):
        if isinstance(polynomial, str):
            self.variable = variable_name
            self._dict_repr = {}
        
            matches = self.regex.finditer(polynomial)
            for match in matches:
                member = match.groupdict()
                if member["power"] is None:
                    member["power"] = ""
                
                if self.variable is None and member["variable"]:
                    self.variable = member["variable"]
                
                if not member["sign"] + member["coefficient"] + member["power"]:
                    continue
            
                member["coefficient"] = member["coefficient"] if member["coefficient"] else 1
                if not member["power"]:
                    if member["variable"]:
                        member["power"] = 1
                    else:
                        member["power"] = 0
        
                self._dict_repr[int(member["power"])] = float(
                    f"{member['sign']}{member['coefficient']}"
                )
                
        elif isinstance(polynomial, dict):
            self._dict_repr = polynomial
            self.variable = "x" if variable_name is None else variable_name

        self.normalize()

    def normalize(self):
        """If some power is missed inserts this power in a dict with a value of 0."""

        self.power = max(self._dict_repr.keys())
        for power in range(self.power + 1):
            self._dict_repr.setdefault(power, 0)

    def __str__(self):
        """Transforms dict_ into a polynomial string representation."""
        
        polynomial = ""
        for power in sorted(self._dict_repr.keys(), reverse=True):
            
            sign = "+ " if self._dict_repr[power] > 0 else "- "
            polynomial += sign

            coefficient = abs(self._dict_repr[power])
            if coefficient == 1:
                if power == 0:
                    polynomial += "1 "
                elif power == 1:
                    polynomial += f"{self.variable} "
                else:
                    polynomial += f"{self.variable}^{power} "
            else:
                if power == 0:
                    polynomial += f"{coefficient} "
                elif power == 1:
                    polynomial += f"{coefficient}*{self.variable} "
                else:
                    polynomial +=  f"{coefficient}*{self.variable}^{power} "
        if polynomial[0] == "-":
            minus = True
        else:
            minus = False
        polynomial = polynomial.strip("+- ")
        if minus:
            polynomial = "-" + polynomial
        return polynomial

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._dict_repr}')"
    
    def get_derivative(self):
        """Calculates the derivative of the polynomial."""
        
        derivative_dict = {power - 1 : power * coefficient for power, coefficient
                           in self._dict_repr.items() if power != 0}
        if -1 in derivative_dict:
            del derivative_dict[-1]
        return self.__class__(derivative_dict, self.variable)

    def __call__(self, x):
        """Computes the value of the polynomial at x."""
        result = 0
        power = self.power
        while power > 0:
            result = (result + self._dict_repr[power]) * x
            power -= 1
        result = result + self._dict_repr[0]
        return result

        
        


if __name__ == "__main__":
    poly = Polynomial("-10.0*a^6.0 + 7.0*a^5.0 - 4.0*a^3.0 - 2.0*a^2.0 + a - 1")
    print("polynomial: ", poly)
    print("derivative: ", poly.get_derivative())
    poly = Polynomial({5: 4, 4: 5, 3: -1, 2: 0, 1: 1, 0: 5})
    print("dict_polynomial: ", poly)
    print(poly.get_derivative())
    poly = Polynomial("x^2 + x + 1")
    print(poly(0))
    print(poly(1))
