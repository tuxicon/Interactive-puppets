############################
# add cylinders on the bones
############################


import bpy
from mathutils import Matrix, Vector
import math


from math import *

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

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
    
   print(length(v1),length(v2))
   denominator = (length(v1) * length(v2))
   if (denominator != 0):
        return math.acos(dotproduct(v1, v2) / denominator)
   else:
        return 0;     

def objselect(objct):
    obj.mode_set(mode='OBJECT')
    scn.objects.active = objct
    objct.select = True

def posemode(objct):
    obj.mode_set(mode='POSE')
    scn.objects.active = objct
    objct.select = True

    
def meshselect(objct):
    obj.mode_set(mode='EDIT')
    scn.objects.active = objct
    objct.select = True


objselect(amt)
x1 = 0;
y1 = 0;
z1 = 0;
origin = [x1,y1,z1]
obj.mode_set(mode='EDIT')
bone = amt.data

for i in bone.edit_bones:
    bcount += 1
count = 0
rad = bone.edit_bones[0].tail_radius


for i in range(bcount):
    objselect(amt)
    obj.mode_set(mode='EDIT')
    bpy.ops.armature.select_all()
    bone.edit_bones[count].select = True
    bone.edit_bones[count].select_head = True
    bone.edit_bones[count].select_tail = True
    scn.objects[oname].data.edit_bones.active = bone.edit_bones[count]
    bpy.ops.view3d.snap_cursor_to_selected()
    print(bone.edit_bones[count].head)
    
    #bone_obj = bone.edit_bones[count].id_data
    #matrix_final = bone_obj.matrix_world * bone.edit_bones[count].matrix
  
    objselect(amt)
    
    obj.mode_set(mode='POSE')
    pose_bone = bpy.context.active_pose_bone

    # we can get the object from the pose bone
    bone_obj = pose_bone.name
    


    
    
    # now we can view the matrix by applying it to an object
    #obj_empty = bpy.data.objects.new("Test", None)
    #bpy.context.scene.objects.link(obj_empty)
    #obj_empty.matrix_world = matrix_final

   
        
  
   
    
    matrix_final = amt.matrix_world * pose_bone.matrix
    loc, rot, sca = matrix_final.decompose()
    print(loc, rot.to_euler() , sca, matrix_final)

    
    obj.mode_set(mode='EDIT')
    msh.primitive_cylinder_add(vertices=cv,radius=rad*sclr,depth=bone.edit_bones[count].length, rotation = rot.to_euler() )
    count += 1
    bpy.ops.view3d.snap_selected_to_cursor()
    
    newobj = bpy.context.object
    objselect(newobj)
    mat_obj_world = newobj.matrix_world
    loc, rot, sca = mat_obj_world.decompose()
    rotations = rot.to_euler() 
    print(rotations[0],rotations[1],rotations[2])
    add_rotation = 0
    
    if (rot[0] < 0 ):
            add_rotation = -1.57079633 
    else:
            add_rotation =  1.57079633         
            
    newobj.rotation_mode = 'XYZ'      
    newobj.rotation_euler = (add_rotation+rotations[0], rotations[1], rotations[2])  
    #bpy.ops.transform.rotate(value=(add_rotation+rot[0],))
    
    #newobj.matrix_world = matrix_final
    newobj.select = False
    #newobj.matrix_world =  matrix_final;
   
   
    
    
    
    #newobj.worldOrientation = [thetax,thetay,thetaz]
    
    
bpy.context.area.type = 'TEXT_EDITOR'   