import sympy as sym
        
class model_manual:
    def __init__(self, no_equation):
        self.no_equation = no_equation
        self.variables = []
        self.operation = []
        self.equations = []
        self.char2id = {}
        
    def add_variables(self, var):
        for i in var:
            self.variables.append(i)
    def add_operations(self, operations):
        self.operation.append('=')
        for i in operations:
            if i not in self.operation:
                self.operation.append(i)
    def add_equations(self, equation):
        new_list = []
        for i in self.equations:
            new_list.append(i)
        if len(equation)==1:
            equation = [equation]
        for i in equation:
            if i not in self.equations: 
                new_list.append(i)
        self.equations = new_list
    def get_operations(self):
        return self.operation[1:]
    def get_equations(self):
        return self.equations
    def get_variables(self):
        return self.variables
    def remove_operation(self, operation):
        self.new_list = []
        for i in self.operation:
            if i != operation:
                self.new_list.append(i)
        self.operation = self.new_list
    def remove_variable(self, variable):
        self.new_list = []
        for i in self.variables:
            if i != variable:
                self.new_list.append(i)
        self.variables = self.new_list
        
    def remove_equation(self, no = None, equation = None):
        self.new_list = []
        if no == None:
            for i in self.equations:
                if i != equation:
                    self.new_list.append(i)
            self.equations = self.new_list
        else:
            no  = int(no) -1
            for i,l in enumerate(self.equations):
                if no != i:
                    self.new_list.append(l)
            self.equations = self.new_list
            
    def find_index(self,a, x):
        index = 0
        for i in x[0]:
            if i == a:
                return index
            else:
                index += 1
            
    def result(self):
        print("Equations: ")
        for i in self.equations:
            print(i)
        print("-----------------------")
        
        print("Variables: ")
        for i in self.variables:
            print(i)
        print("-----------------------")
        
        print("Operations: ")
        for i in self.operation[1:]:
            print(i)
        print("-----------------------")  
        
        for i, c in enumerate(self.variables):
            self.char2id[i] = c
            
        sy =[]
        add_sy = ''
        for i in self.variables:
            add_sy += i+','
        if len(self.variables)>1:
            sy.append(sym.symbols(add_sy[:-1]))
        else:
            sy.append(sym.symbol(add_sy[:-1]))
        
        
        order_var_1 = []
        order_op_1 = []
        coeff_1 = []
        for i in self.equations:
            order_var = []
            order_op = []
            coeff = []
            eq = i[0]
            count = 0
            while(count < len(eq)):
                t = ''
                v = eq[count]
                while(v not in self.operation):
                    t += v
                    count += 1
                    if count < len(eq):
                        v = eq[count]
                    else:
                        break  
                count += 1
#                 if not t.isdigit():
#                     order_var.append(t)
                try:
                    t = int(t)
                    t_new = str(t)
                except:
                    co = ''
                    t_new = ''
                    status = True
                    for c in t:
                        if c.isdigit() and status:
                            co += c
                            status = False
                        else:
                            t_new += c
                            status = False
                    if not co:
                        co = '1'
                    coeff.append(co)
                
                order_var.append(t_new)
                
                if v in self.operation:
                    order_op.append(v)
            coeff_1.append(coeff)    
            order_var_1.append(order_var)
            order_op_1.append(order_op)
        print(order_var_1)
        print()
        print(order_op_1)
        print()
        print(coeff_1)
        print('-------------------------------------')
        print('Variable_created: ')
        print(sy)
        
        
        
        # Add equation
        # for var, op, coe in zip(order_var_1, order_op_1, coeff_1):
        # incomplete

