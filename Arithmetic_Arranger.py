def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    widths = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        # Validating
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Preparing 
        width = max(len(operand1), len(operand2)) + 2
        first_operands.append(operand1)
        second_operands.append(operand2)
        operators.append(operator)
        widths.append(width)

    return format_problems(first_operands, second_operands, operators, widths, show_answers)

# Formatting 

def format_problems(first_operands, second_operands, operators, widths, show_answers):
    
    # Each row as a list to join with 4 spaces later
    top_row = []
    second_row = []
    dashes_row = []
    answers_row = []

    for i in range(len(first_operands)):
        
        # Row 1: right‑align first operand
        
        top_row.append(first_operands[i].rjust(widths[i]))

        # Row 2: operator + right‑align second operand (minus the operator's space)
        second_row.append(operators[i] + second_operands[i].rjust(widths[i] - 1))

        # Row 3: dashes equal to the width
        dashes_row.append("-" * widths[i])

        # Row 4: answer
        if show_answers:
            if operators[i] == "+":
                result = str(int(first_operands[i]) + int(second_operands[i]))
            else:
                result = str(int(first_operands[i]) - int(second_operands[i]))
            answers_row.append(result.rjust(widths[i]))

    # Four spaces between problems
    arranged = (
        "    ".join(top_row) + "\n" +
        "    ".join(second_row) + "\n" +
        "    ".join(dashes_row)
    )

    if show_answers:
        arranged += "\n" + "    ".join(answers_row)

    return arranged


# Insert "True" after the comma at end of the probplems list below to see answers

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}\n')
