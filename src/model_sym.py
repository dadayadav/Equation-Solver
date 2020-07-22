import sympy as sym
from sympy import sympify
from sympy.parsing.sympy_parser import parse_expr
class equation:
    def __init__(self):
        import sympy as sym
        from sympy import sympify
        from sympy.parsing.sympy_parser import parse_expr
        sym.init_printing()
        self.symbol = []
        self.static = []
        self.equation =[]
    
    def add_variable(self, string):
        self.symbol.append(sym.symbols(string))
    
    def add_static_variable(self, string):
        self.static.append(sym.Symbol(string))
    
    def add_equation(self, eq):
        eq = eq.split('=')
        a = parse_expr(eq[0], evaluate=False)
        b = parse_expr(eq[1], evaluate=False)
        self.equation.append(sym.Eq(a,b))
        
    def get_equation(self):
        return self.equation
    
    def get_evaluate_variable(self):
        return self.symbol
    
    def get_static_variable(self):
        return self.static
    
    def get_all_variable(self):
        all_var = {}
        all_var['Static Variables'] = self.static
        all_var['Evaluate Variables'] = self.symbol
        return all_var
    
    def summary(self):
        print('****************************************')
        print()
        print('Equations: ')
        print('--------------------------------------')
        for i in self.equation:
            print(i)
        print('--------------------------------------')
        print()
        print('Variables:')
        if len(self.static)>0:
            print('          Static Variables:')
            for i in self.static:
                print('                       {}'.format(i))
        print('--------------------------------------')
        print('          Evaluate Variables:')
        for i in self.symbol:
            print('                       {}'.format(i))
        print('--------------------------------------')
        print()
        print('****************************************')
        
        
        
    def solution(self):
        return sym.solve(self.equation, self.symbol[0], dict=True)