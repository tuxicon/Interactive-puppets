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
##################################################################






#########################################
## "Visual Transform" helper functions ##
#########################################


def get_pose_matrix_in_other_space(mat, pose_bone):
    """ Returns the transform matrix relative to pose_bone's current
    transform space. In other words, presuming that mat is in
    armature space, slapping the returned matrix onto pose_bone
    should give it the armature-space transforms of mat.
    TODO: try to handle cases with axis-scaled parents better.
    """
    rest = pose_bone.bone.matrix_local.copy()
    rest_inv = rest.inverted()
    if pose_bone.parent:
        par_mat = pose_bone.parent.matrix.copy()
        par_inv = par_mat.inverted()
        par_rest = pose_bone.parent.bone.matrix_local.copy()
    else:
        par_mat = Matrix()
        par_inv = Matrix()
        par_rest = Matrix()
    
    
    # Get matrix in bone's current transform space
    smat = rest_inv * (par_rest * (par_inv * mat))
    
    
    # Compensate for non-local location
    #if not pose_bone.bone.use_local_location:
    # loc = smat.to_translation() * (par_rest.inverted() * rest).to_quaternion()
    # smat.translation = loc
    
    
    return smat
    



def get_local_pose_matrix(pose_bone):
    """ Returns the local transform matrix of the given pose bone.
    """
    return get_pose_matrix_in_other_space(pose_bone.matrix, pose_bone)




def get_bones_rotation(armature,bone,axis):

    mat = get_local_pose_matrix(bpy.data.objects[armature].pose.bones[bone])
    if axis == 'z':
        return degrees(mat.to_euler().z)
    elif axis == 'y':
        return degrees(mat.to_euler().y)
    elif axis == 'x':
        return degrees(mat.to_euler().x)
    






################################################## ############ main program setup




######################################################################


##############################Calculate bone rotation ###########################################
# returns visual rotation of this bone, relative to rest pose, as a quaternion
# after channels and constraints are applied
def quaternionRotation(armatureName, boneName):
    bone        = bpy.data.armatures[armatureName].bones[boneName]
    bone_ml     = bone.matrix_local
    bone_pose   = bpy.data.objects[armatureName].pose.bones[boneName]
    bone_pose_m = bone_pose.matrix
    
    if bone.parent:

        parent        = bone.parent
        parent_ml     = parent.matrix_local
        parent_pose   = bone_pose.parent
        parent_pose_m = parent_pose.matrix

        object_diff = parent_ml.inverted() * bone_ml
        pose_diff   = parent_pose_m.inverted() * bone_pose_m
        local_diff  = object_diff.inverted() * pose_diff

    else:
    
        local_diff = bone_ml.inverted() * bone_pose_m
    
    #print(local_diff.to_quaternion())
    return local_diff.to_quaternion()

def xAxisRotation(armatureName, boneName):
    q = quaternionRotation(armatureName, boneName)
    return atan2(2*(q[0]*q[1]+q[2]*q[3]), 1-2*(q[1]*q[1]+q[2]*q[2]))

def yAxisRotation(armatureName, boneName):
    q = quaternionRotation(armatureName, boneName)
    return asin(2*(q[0]*q[2]-q[3]*q[1]))

def zAxisRotation(armatureName, boneName):
    q = quaternionRotation(armatureName, boneName)
    return atan2(2*(q[0]*q[3]+q[1]*q[2]), 1-2*(q[2]*q[2]+q[3]*q[3]))

def xAxisRotation_2(armatureName, boneName):
    return xAxisRotation(armatureName, boneName) * 2 / pi

def yAxisRotation_2(armatureName, boneName):
    return yAxisRotation(armatureName, boneName) * 2 / pi

def zAxisRotation_2(armatureName, boneName):
    return zAxisRotation(armatureName, boneName) * 2 / pi
   



#######################################################################################

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
    #print(math.acos())
    dx = bone.edit_bones[count].head[0] - bone.edit_bones[count].tail[0];
    dy = bone.edit_bones[count].head[1] - bone.edit_bones[count].tail[1];
    dz = bone.edit_bones[count].head[2] - bone.edit_bones[count].tail[2];
    thetax = math.atan2(dy, dz);
    thetay = math.atan2(dx, dz);
    thetaz = math.atan2(dy, dx);
    pthetax = thetax * 180/3.14 
    pthetay = thetay * 180/3.14
    pthetaz = thetaz * 180/3.14 #rads to degs'''
    print(pthetax,pthetay,pthetaz)
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
    #newobj.matrix_world = matrix_final
    newobj.select = False
    #newobj.matrix_world =  matrix_final;
    print(newobj)
   
    
    #newobj.worldOrientation = [thetax,thetay,thetaz]
    
    
bpy.context.area.type = 'TEXT_EDITOR'   