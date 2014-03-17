import bpy

arm = bpy.data.objects.get('Armature')

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

    