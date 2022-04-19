class Problem():  # 'n1  +/- n2'
    def __init__(self, string):
        elems = string.split()
        self.flag = "Correct"
        self.n1 = elems[0]
        if not self.n1.isdigit(): self.flag = "Error: Numbers must only contain digits."
        self.op = elems[1]
        if self.op != '+' and self.op != '-': self.flag = "Error: Operator must be '+' or '-'."
        self.n2 = elems[2]
        if not self.n2.isdigit(): self.flag = "Error: Numbers must only contain digits."
        self.no_dashes = max(len(self.n1), len(self.n2)) + 2
        if self.flag == "Correct":
            if self.op == '+':
                self.sol = str(int(self.n1) + int(self.n2))
            else:
                self.sol = str(int(self.n1) - int(self.n2))
        else:
            self.sol = 'Error'


def arithmetic_arranger(problems, solution=False):
    p = []
    arranged_problems = ""
    for problem in problems:
        cls = Problem(problem)
        if len(cls.n1) > 4 or len(cls.n2) > 4: return "Error: Numbers cannot be more than four digits."
        p.append(cls)
        if cls.flag != "Correct": return cls.flag
    if len(p) > 5: return "Error: Too many problems."
    first_line = " " * (p[0].no_dashes - len(p[0].n1)) + p[0].n1
    second_line = p[0].op + " " * (p[0].no_dashes - len(p[0].n2) - 1) + p[0].n2
    third_line = "-" * p[0].no_dashes
    fourth_line = " " * (p[0].no_dashes - len(p[0].sol)) + p[0].sol
    if len(p) > 1:
        i = 1
        for i in range(1, len(p)):
            first_line += 4 * " " + " " * (p[i].no_dashes - len(p[i].n1)) + p[i].n1
            second_line += 4 * " " + p[i].op + " " * (p[i].no_dashes - len(p[i].n2) - 1) + p[i].n2
            third_line += 4 * " " + "-" * p[i].no_dashes
            fourth_line += 4 * " " + " " * (p[i].no_dashes - len(p[i].sol)) + p[i].sol
    arranged_problems = first_line + '\n' + second_line + '\n' + third_line
    if solution == True:
        arranged_problems += '\n' + fourth_line
    return arranged_problems



