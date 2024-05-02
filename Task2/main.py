from plotly import express as px
import spline
import newton
import tio

mat = tio.read_matrix("data/t")

X = 0.8

mat_x = [p[0] for p in mat]
mat_y = [p[1] for p in mat]

spnat = spline.Spline(mat, 0, 0)
print()
print(spnat.a)
print(spnat.b)
print(spnat.c)
print(spnat.d)
# spnewton1 = spline.Spline(mat, newton.newtonSecondDeriativeThird(mat, min(mat_x)), 0)
# spnewton2 = spline.Spline(mat, newton.newtonSecondDeriativeThird(mat, min(mat_x)), newton.newtonSecondDeriativeThird(mat, max(mat_x)))

# print(f"Результаты для X={X:.3f}:")
# print(f"Полином ньютона 3-й степени: {newton.newton(mat, 3, X)}")
# print(f"Сплайн естественного порядка: {spnat.approximate(X)}")
# print(f"Сплайн с одной границей полиномом ньютона: {spnewton1.approximate(X)}")
# print(f"Сплайн с обоими границами полиномом ньютона: {spnewton2.approximate(X)}")


# # plot = px.line(x=mat_x, y=mat_y)
# # plot.add_scatter(x=[X], y=[newton.newton(mat, 3, X)], name="Ньютон")
# # plot.add_scatter(x=[X], y=[spnat.approximate(X)], name="Естественный сплайн")
# # plot.add_scatter(x=[X], y=[spnewton1.approximate(X)], name="Сплайн с одной границей")
# # plot.add_scatter(x=[X], y=[spnewton2.approximate(X)], name="Сплайн с двумя границами")

# # plot.show()

# x = [min(mat_x) + i * (max(mat_x) - min(mat_x)) / 100 for i in range(100)]
# plot = px.line(x=mat_x, y=mat_y)
# plot.add_scatter(x=x, y=[newton.newton(mat, 3, X) for X in x], name="Ньютон")
# plot.add_scatter(x=x, y=[spnat.approximate(X) for X in x], name="Естественный сплайн")
# plot.add_scatter(x=x, y=[spnewton1.approximate(X) for X in x], name="Сплайн с одной границей")
# plot.add_scatter(x=x, y=[spnewton2.approximate(X) for X in x], name="Сплайн с двумя границами")

# plot.show()