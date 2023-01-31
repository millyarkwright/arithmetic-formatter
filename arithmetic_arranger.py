import operator

ops = {"+": operator.add, "-": operator.sub}


def arithmetic_arranger(problems, result=True):
  # Receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
  # Second argument: when set to True, the answers should be displayed.
  
  # Possible Errors: 
    # 'Error: Too many problems.': If there are too many problems supplied to the function. The limit is five.
    # 'Error: Operator must be '+' or '-'.': The appropriate operators the function will accept are addition (+) and subtraction (-). Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. 
    # 'Error: Numbers must only contain digits.': Each number (operand) should only contain digits. 
    # 'Error: Numbers cannot be more than four digits.': Each operand (aka number on each side of the operator) has a max of four digits in width. 
  # Base Case 1: Too many problems supplied. Limit: 5. Return error: 'Too many problems'
  if len(problems) > 5:
    print("Too many problems")
    return "Error: Too many problems."

  top = []
  bottom = []
  lines = []
  results = []
  arranged_problems = ""

  for s in problems:
    x, operator, y = s.split()

    if operator not in ops:
      return "Error: Operator must be '+' or '-'."

    if not x.isnumeric() or not y.isnumeric():
      print("Error: Numbers must only contain digits.")
      return "Error: Numbers must only contain digits."

    # The number to the left of the e multiplied by 10 raised to the power of the number after the e. ie 10 x 10 x 10 x 10 = 10000
    if abs(int(x)) >= 1e4 or abs(int(y)) >= 1e4:
      # for n in (int(x), int(y)):
      # if abs(n) >= 1e4:
      print("Error: Numbers cannot be more than four digits.")
      return "Error: Numbers cannot be more than four digits."

  # #  Find the longest number in the problem.  plus two (one for the space and one for the operator) and that's the number of columns required for each problem. 
    # Longest number in each problem
    max_length = max(len(x), len(y))
    # Line length (max_length plus 2 for a space and operator)
    line_length = max_length + 2

    first_number = x.rjust(line_length, ' ')
    second_number = f"{operator}{' ' * (line_length - len(y) - 1)}{y}"
    line = '-' * line_length

    top.append(first_number)
    bottom.append(second_number)
    lines.append(line)
    
        # If second argument (result) is set to True: Calculate the total sum of each problem, format (stringify and right align) and then append the result to the results array.
    if result: 
      # Get total of each problem
      total = ops[operator](int(x), int(y))
      result = str(total).rjust(line_length, ' ')
      results.append(result)

  arranged_problems = '\n'.join(['    '.join(i) for i in (top, bottom, lines)])
  
  if results: 
    arranged_problems += '\n' + '    '.join(results)
      
  print(arranged_problems)

  return arranged_problems


  # print(top)
  # print(bottom)
  # print(lines)
  # print(results)
    # ! Attempt 1 - variables when initiated need to be strings not array.
    # topline = topline + x.rjust(max_length) + (4 * " ")
    # bottomline = bottomline + operator + y.rjust(max_length - 1) + (4 * " ")
    # line = line + (max_length * "-") + (4 * " ")
    # totalline = totalline + str(total).rjust(max_length) + (4 * " ")