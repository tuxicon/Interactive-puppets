import bpy
import re



def mesh_prepare(mesh):
    if mesh is not None and bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = mesh
        mesh.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        return True
    return False

obs = bpy.data.objects
for ob in obs:
    prog = re.compile('Cylinder.0..')
    if  prog.match(ob.name):
        myObj = bpy.data.objects.get(ob.name)
        print (myObj)
        mesh_prepare(myObj)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        bpy.ops.mesh.edge_face_add()
        
        
    else:
        print('no match')           
