import Rhino.Geometry as rg
from math import sin, cos

def uv_sin(u, v, w, scale_values):
    u_s, v_s, w_s = scale_values

    return sin(u/u_s) * sin(v/v_s) * sin(w/w_s) * .5 + .5

def uv_gyroid_gyroid(u, v, w, scale_values):
    s_n = uv_gyroid(u, v, w, tuple([scale_values[0] for i in range(3)])) * scale_values[1]

    return uv_gyroid(u,v,w,tuple([s_n for i in range(3)]))

def uv_gyroid(u, v, w, scale_values):
    u_s, v_s, w_s = scale_values

    u/=u_s
    v/=v_s
    w/=w_s

    return ( sin(u) * cos(v) + sin(v) * cos(w) + sin(w) * cos(u) ) / 3.0 + .5

def move_pts(pts, uv_function = uv_sin, direction = 'x', pos_neg = False, isoplane = 60, amplitude = 60, w = 0, scale_values = (1.,1.,1.) ):
    for pt in pts:
        if direction == 'x':
            ds_pln = abs(pt.X - isoplane)
            if ds_pln < amplitude:
                mv_val = (amplitude-ds_pln) * uv_function(pt.Y, pt.Z, w, scale_values)
                if pos_neg:
                    pt.X+=mv_val
                else:
                    pt.X-=mv_val

        if direction == 'y':
            ds_pln = abs(pt.Y - isoplane)
            if ds_pln < amplitude:
                mv_val = (amplitude-ds_pln) * uv_function(pt.X, pt.Z, w, scale_values)
                if pos_neg:
                    pt.Y+=mv_val
                else:
                    pt.Y-=mv_val

    return pts


