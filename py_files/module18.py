def line(dot1:list, dot2:list) -> str:
    x1, y1 = dot1
    x2, y2 = dot2
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k*x2
    return f'y = {k}x + {b}'
    
def check_parallel(line1: str, line2: str) -> bool:
    return line1.split('x')[0][-1] == line2.split('x')[0][-1]

def check_dot_on_line(line: str, dot: list) -> bool:
    x_dot, y_dot = dot
    b = int(line.split('+')[-1].strip()) if '+' in line else 0
    k = int(line.split('x')[-2].split('=')[-1].strip()) if 'x' in line else 0
    return y_dot == k*x_dot + b