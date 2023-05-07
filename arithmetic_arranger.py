def arithmetic_arranger(problems:list, show_answer=False):
    result = []
    # Errors
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."
        for item in problem.split():
            if item == '+' or item == '-':
                continue
            if not item.isdigit():
                return "Error: Numbers must only contain digits."
            if len(item) > 4:
                return "Error: Numbers cannot be more than four digits."
    
    # Functionality
    fline = []
    sline = []
    eqlines = []
    totals = []
    for problem in problems:
        p = problem.split()
        evaluation = eval(problem)
        maximum = max([len(item) for item in p])
        fline.append(p[0].rjust(maximum + 2))
        sline.append(p[1]+ ' ' + p[2].rjust(maximum))
        eqlines.append(('-' * (maximum+2)).rjust(maximum))
        totals.append(str(evaluation).rjust(maximum + 2))
    
    result.append('    '.join(fline))
    result.append('    '.join(sline))
    result.append('    '.join(eqlines))
    if show_answer:
        result.append('    '.join(totals))
    
    arranged_problems = '\n'.join(result)
    return arranged_problems
    
    
if __name__ == "__main__":
    problems = ['1 + 2', '1 - 9380']
    print(arithmetic_arranger(problems, True))