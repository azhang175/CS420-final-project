import re

# Define a set of math operators and comparison math_operators 
math_operators = {'*', '/', '%', '+', '-'}
comparison_operator = {"<",">", "!=", "==", ">=", "<="}

# A function to fetch value of a variable from a dictionary
def varmap(targetVar, state):
    if targetVar in state:
        return state[targetVar]
    else:
        raise ValueError("Error: Var not found")


# A Function to calculate math expression base on operators
def calculate(expression, state):
    result = 0 #Initialize Result

    # Check if the math operators is in expression
    for operator in math_operators:
        if operator in expression:
            #Split the expression in two values based on the operators
            value1, value2 = expression.split(operator)

            # Fetch from state if variable, else convert to float
            if value1.strip() in state:
                val1 = float(state[value1].strip())
            else:
                val1 = float(value1.strip())

            if value2.strip() in state:
                val2 = float(state[value2].strip())
            else:
                val2 = float(value2.strip())

            #Preform the calculation based on operators
            if operator == '*':
                result = val1 * val2
            elif operator =='/':
                if val2 == 0:
                    raise ValueError("Error! Not divisible by zero")
                result = val1 / val2
            elif operator == '%':
                result = val1 % val2
            elif operator =='+':
                result = val1 + val2
            elif operator == '-':
                result = val1 - val2
            break #ends the calculation

    return result #Return the calculated result


#A function to handle if statement with a given condition and block of code
def if_statement(condition, block, state):
    for op in comparison_operator:
        if op in condition:
            compare_op = op
            break
    
    # Split the condition into left hand side(lhs) and right hand side(rhs)
    lhs_expression, rhs_expression = condition.split(compare_op, 1)

    # Default boolean for lhs_expression_math_op_found, rhs_expression_math_op_found and condition_met
    lhs_expression_math_op_found = False
    rhs_expression_math_op_found = False
    condition_met = False

    #Check for there is an math operators in lhs_expression and rhs_expression
    for math_op in math_operators:
        if math_op in lhs_expression:
            lhs_expression_math_op_found = True
            break

    for math_op in math_operators:
        if math_op in rhs_expression:
            rhs_expression_math_op_found = True
            break
    
    # Evaluate the lhs and rhs expression
    if lhs_expression_math_op_found == True:        
        lhs_val = calculate(lhs_expression.strip(), state)
    else:
        try: 
            lhs_val = float(varmap(lhs_expression.strip(), state))
        except:
            lhs_val = lhs_expression.strip()
    
    
    if rhs_expression_math_op_found == True:        
        rhs_val = calculate(rhs_expression.strip(), state)
    else:
        try: 
            rhs_val = float(varmap(rhs_expression.strip(), state))
        except:
            rhs_val = float(rhs_expression.strip())

    # Check if the condition is met based on comparison operator
    if compare_op == "==":
        condition_met = lhs_val == rhs_val
    elif compare_op == "!=":
        condition_met = lhs_val != rhs_val
    elif compare_op == "<":
        condition_met = lhs_val < rhs_val
    elif compare_op == ">":
        condition_met = lhs_val > rhs_val
    elif compare_op == "<=":
        condition_met = lhs_val <= rhs_val
    elif compare_op == ">=":
        condition_met = lhs_val >= rhs_val

    #if the condition_met is true, execute the block code
    if condition_met is True:
        questCode(block, state)
    
    return condition_met


#Function to execute the main program
def questCode(program, state=None):
    #initialize state if it's not provided
    if state is None:
        state = {}

    #Default boolean for condition met
    condition_met = False 
    
    #Split the program into individual lines
    for line in program.splitlines():
        #Strip the leading and tailing whitespace
        line = line.strip()
        #if the line is empty, continue to the next line
        if not line:
            continue

        #split the line into an instruction and its expression
        statements = line.split(maxsplit=1)
        
        #make sure the line have both instruction and expression
        if len(statements) != 2:
            continue
        
        
        instruction, expression = statements
        
        if instruction == "treasure":
            var, val = expression.strip().split('=')
            var = var.strip()
            val = val.strip()
            state[var] = float(val.strip())

        elif instruction == "message":
            var, val = expression.strip().split('=')
            var = var.strip()
            val = val.strip('" "')
            state[var] = val

        elif instruction == "display":
            expression = expression.strip('()').strip()
            if expression.isdigit():
                print(float(expression))
                
            elif expression.startswith('"') and expression.endswith('"'):
                print(expression.strip('"'))
            else:
                try:
                    val = state[expression]
                    print(val)
                except KeyError:
                    print(f"Error: Var not found")

        elif instruction == "challenge":
            # Attempt to find the outermost parentheses for the condition and the first curly braces for the block
            try:
                start_condition_index = expression.index('(') + 1
                print(start_condition_index)
                end_condition_index = expression.rindex(')')  # Change to rindex to handle nested cases
                start_block_index = expression.index('{') + 1
                end_block_index = expression.rindex('}')  # Ensure matching the last '}'
                print(start_condition_index, end_condition_index, start_block_index, end_block_index)

                if start_condition_index > end_condition_index or start_block_index > end_block_index:
                    raise ValueError("Mismatched parentheses or curly braces")

                condition = expression[start_condition_index:end_condition_index].strip()
                print(condition)
                block = expression[start_block_index:end_block_index].strip()
                print(block)
                # Execute the condition and block if the condition is met
                condition_met = if_statement(condition, block, state)
            
            except ValueError as ve:
                print(f"Syntax Error: {ve}")
                return False
            except Exception as e:
                print(f"Unexpected error during parsing: {str(e)}")
                return False
            print(condition)
            print(block)


        else:
            print("Error! Instruction not found")

def read_and_execute(filename):
    try:
        with open(filename, 'r') as file:
            code = file.read()
            print("File read successfully:")
            #print(code)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    questCode(code)


# read_and_execute('sample1.questcode')
read_and_execute('sample2.questcode')
