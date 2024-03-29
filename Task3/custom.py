import newton
import spline
import matrix3d as m3
import matrix4d as m4

def customInterpolation3d(
    mat: m3.Matrix3d,
    nx,
    ny,
    x,
    y,
    x_method, # 'newton' or 'spline'
    y_method,      
):
    if x_method not in ["newton", "spline"] or y_method not in ["newton", "spline"]:
        raise ValueError("Methods can only be 'newton' or 'spline'")
    zy = []
    # Если ньютон по y, то нам нужно аппроксимировать по x только в ближаших к y точках
    if (y_method == "newton"):
        neary = mat.getNearestYIndex(y, ny + 1)
        neary, nearyindexes = zip(*neary)
    else:
        neary, nearyindexes = mat.y, list(range(len(mat.y)))
    
    # Аппроксимуруем по X во всех точках neary со значением x
    if (x_method == "newton"):
        for yi in nearyindexes:
            zy.append(newton.newton(mat.getZXfromY(yi), nx, x))
    else:
        for yi in nearyindexes:
            sp = spline.Spline(mat.getZXfromY(yi), 0, 0)
            zy.append(sp.approximate(x))
    # Аппроксимируем по y
    if (y_method == "newton"):
        return (newton.newton(list(zip(neary, zy)), ny, y))
    else:
        sp = spline.Spline(list(zip(neary, zy)), 0, 0)
        return sp.approximate(y)

def customInterpolation4d(
        mat: m4.Matrix4d,
        nx,
        ny,
        nz,
        x,
        y,
        z,
        x_method,
        y_method,
        z_method
):
    if x_method not in ["newton", "spline"] or y_method not in ["newton", "spline"] or z_method not in ["newton", "spline"]:
        raise ValueError("Methods can only be 'newton' or 'spline'")
    fz = []
    if (z_method == "newton"):
        nearz = mat.getNearestZIndex(z, nz + 1)
        nearz, nearzindexes = zip(*nearz)
        for zi in nearzindexes:
            fz.append(customInterpolation3d(mat.getZSlice(zi), nx, ny, x, y, x_method, y_method))
        return newton.newton(list(zip(nearz, fz)), nz, z)
    else:
        for zi in range(len(mat.z)):
            fz.append(customInterpolation3d(mat.f[zi], nx, ny, x, y, x_method, y_method))
        sp = spline.Spline(list(zip(mat.z, fz)), 0, 0)
        return sp.approximate(z)

   
    

    