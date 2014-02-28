import bpy

arm = bpy.data.objects.get('Armature')
cube = bpy.data.objects.get('Cube') 

def mesh_prepare(cube):
    if cube is not None and bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = cube
        cube.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        return True
    return False

def armature_prepare(arm):
    if arm is not None and bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = arm
        arm.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        return True
    return False

if armature_prepare(arm):
   print("get arm=" + 'Armature' + " arm=" + str(arm))
for bone in arm.data.edit_bones: 
    print(bone,bone.tail)
    v = bone.tail
    

if mesh_prepare(cube):
   print("get cube=" + 'Cube' + " cube=" + str(cube))
mesh = bpy.context.object.to_mesh(bpy.context.scene, True, "PREVIEW")
for vertex in mesh.vertices:
    for group in vertex.groups:
        print(vertex, group.weight)    
        
