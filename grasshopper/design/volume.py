from Rhino.Geometry import Point3d, Mesh, Transform, Plane

# class VertexFaceMesh():
#     def __init__(self, vs, fs):
#         self.vs = vs
#         self.fs = fs

#     def rhino_mesh(self):
#         msh = Mesh()

def pedistle(top_box_side = 500., side_h = 150., side_w = 150.):
    msh = Mesh()
    h_l = top_box_side * .5

    half_pi = 1.5707963268

    pts = [
        Point3d(h_l + side_w, h_l + side_w, 0.),
        Point3d(h_l, h_l, side_h),
        Point3d(h_l, h_l, top_box_side + side_h)
    ]

    for i in range(4):
        angle = half_pi * i

        t_matrix = Transform.Rotation(angle, Point3d.Origin)

        for pt in pts:
            loc_pt = Point3d(pt)
            loc_pt.Transform(t_matrix)
            msh.Vertices.Add(loc_pt)

    cnt = len(msh.Vertices)

    for i in range(4):
        # print(i*3+0, i*3+1, ((i+1)*3+1)%len(pts), ((i+1)*3+0)%len(pts))
        msh.Faces.AddFace(i*3+0, i*3+1, ((i+1)*3+1)%cnt, ((i+1)*3+0)%cnt)
        msh.Faces.AddFace(i*3+1, i*3+2, ((i+1)*3+2)%cnt, ((i+1)*3+1)%cnt)

    msh.Faces.AddFace(0, 3, 6, 9)
    msh.Faces.AddFace(11, 8, 5, 2)

    return msh

def box(w, b_0, b_1):
    msh = Mesh()
    h_l = w * .5

    half_pi = 1.5707963268

    pts = [
        Point3d(h_l, h_l, b_0),
        Point3d(h_l, h_l, b_1)
    ]

    for i in range(4):
        angle = half_pi * i

        t_matrix = Transform.Rotation(angle, Point3d.Origin)

        for pt in pts:
            loc_pt = Point3d(pt)
            loc_pt.Transform(t_matrix)
            msh.Vertices.Add(loc_pt)

    for i in range(4):
        msh.Faces.AddFace(i*2+0, i*2+1, ((i+1)*2+1)%8, ((i+1)*2+0)%8)

    msh.Faces.AddFace(0, 2, 4, 6)
    msh.Faces.AddFace(7, 5, 3, 1)

    return msh

def pedistle_with_tolerance(top_box_side = 500., side_w = 150., side_h = 150., extra_b_h = 100.):
    total_b_h = side_h+extra_b_h
    total_w = side_w*total_b_h/side_h

    return (
        pedistle(top_box_side, total_b_h, total_w),
        box(top_box_side+2.*side_w, extra_b_h, total_b_h+top_box_side+side_h)
    )

def print_mesh(msh):
    str_list = ["Vertices:"]
    for v in msh.Vertices:
        str_list.append('\t'+str(v))
    
    str_list.append("Faces:")
    for f in msh.Faces:
        str_list.append('\t'+str(f))

    return '\n'.join(str_list)

