def extrude_face(bm, face, translate_forwards=0.0, extruded_face_list=None):
    new_faces = bmesh.ops.extrude_discrete_faces(bm, faces=[face])['faces']
    if extruded_face_list != None:
        extruded_face_list += new_faces[:]
    new_face = new_faces[0]
    bmesh.ops.translate(bm,
                        vec=new_face.normal * translate_forwards,
                        verts=new_face.verts)
    return new_face

def scale_face(bm, face, scale_x, scale_y, scale_z):
    face_space = get_face_matrix(face)
    face_space.invert()
    bmesh.ops.scale(bm,
                    vec=Vector((scale_x, scale_y, scale_z)),
                    space=face_space,
                    verts=face.verts)def menu_func(self, context):
    self.layout.operator(GenerateSpaceship.bl_idname, text="Spaceship")
#good
def register():
    bpy.utils.register_class(GenerateSpaceship)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(GenerateSpaceship)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
