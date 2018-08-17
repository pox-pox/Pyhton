import graphics as gr

window = gr.GraphWin("Russian game", 600, 600)
alpha = 0.05
point = []
def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    point.clear()
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window) # *M - развертывание кортежа
        point.append((M[0]*(1-alpha) + N[0]*alpha, M[1]*(1-alpha) + N[1]*alpha))
    fractal_rectangle(*point, deep-1)

fractal_rectangle ((100, 100), (500, 100), (500, 500), (100, 500), 200)
window.getMouse()
