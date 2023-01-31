import operator

ops = {"+": operator.add, "-": operator.sub}

def arithmetic_arranger(problems, result=True):
  # Receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
  # Second argument: when set to True, the answers should be displayed.
  
  # ! Possible Errors: 
    # 'Error: Too many problems.': If there are too many problems supplied to the function. The limit is five.
    # 'Error: Operator must be '+' or '-'.': The appropriate operators the function will accept are addition (+) and subtraction (-). Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. 
    # 'Error: Numbers must only contain digits.': Each number (operand) should only contain digits. 
    # 'Error: Numbers cannot be more than four digits.': Each operand (aka number on each side of the operator) has a max of four digits in width. 
  
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
      return "Error: Numbers must only contain digits."

    # The number to the left of the e multiplied by 10 raised to the power of the number after the e. ie 10 x 10 x 10 x 10 = 10000
    if abs(int(x)) >= 1e4 or abs(int(y)) >= 1e4:
      return "Error: Numbers cannot be more than four digits."

    # Longest number in each problem
    max_length = max(len(x), len(y))
    # Plus 2 corresponds to the space and the operator
    line_length = max_length + 2

    first_number = x.rjust(line_length, ' ')
    second_number = f"{operator}{' ' * (line_length - len(y) - 1)}{y}"
    line = '-' * line_length

    top.append(first_number)
    bottom.append(second_number)
    lines.append(line)

    if result: 
      total = ops[operator](int(x), int(y))
      result = str(total).rjust(line_length, ' ')
      results.append(result)

  arranged_problems = '\n'.join(['    '.join(i) for i in (top, bottom, lines)])
  
  if results: 
    arranged_problems += '\n' + '    '.join(results)
      
  print(arranged_problems)

  return arranged_problems

