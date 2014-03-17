############################
# add cylinders on the bones
############################


import bpy

size = 5        # cylinder size: 1(small)-> 6(big)
cv = 32          # cylinder's vertex number 3->
cf = 0          # cylinder opentype = 0, closetype = 1(Ngon) or 2(tri-Poly)
cj = 0          # cylinders join off = 0, on = 1

listEF = ['NOTHING','NGON','TRIFAN']
listSR = [0.25,0.5,1,1.5,2,3]
listSD = [0.5,1,2,3,4,5]

size -= 1
sclr = listSR[size]
scld = listSD[size]

scn = bpy.context.scene
oname = bpy.context.object.name

amt = bpy.data.objects[oname]
msh = bpy.ops.mesh 
obj = bpy.ops.object
bcount = 0

bpy.context.area.type = 'VIEW_3D'

def objselect(objct):
    obj.mode_set(mode='OBJECT')
    scn.objects.active = objct
    objct.select = True
    
def meshselect(objct):
    obj.mode_set(mode='EDIT')
    scn.objects.active = objct
    objct.select = True


objselect(amt)

obj.mode_set(mode='EDIT')
bone = amt.data

for i in bone.edit_bones:
    bcount += 1
count = 0
rad = bone.edit_bones[0].tail_radius
print(bcount, rad)

for i in range(bcount):
    objselect(amt)
    obj.mode_set(mode='EDIT')
    bpy.ops.armature.select_all()
    bone.edit_bones[count].select = True
    bone.edit_bones[count].select_head = True
    bone.edit_bones[count].select_tail = True
    scn.objects[oname].data.edit_bones.active = bone.edit_bones[count]
    print(bone.edit_bones[count].length)
    bpy.ops.view3d.snap_cursor_to_selected()
    msh.primitive_cylinder_add(vertices=cv,radius=rad*sclr,depth=bone.edit_bones[count].length,end_fill_type=listEF[cf])
    count += 1
    bpy.ops.view3d.snap_selected_to_cursor()
    
bpy.context.area.type = 'TEXT_EDITOR'