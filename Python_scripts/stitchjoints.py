import bpy
import re

def union_test(first,second):
    modifier = first.modifiers.new('Modifier', 'BOOLEAN')
    modifier.object = second
    modifier.operation = 'UNION'
    bpy.ops.object.modifier_apply()
    #scene = bpy.context.scene
    #scene.objects.unlink(second)

i= 0;
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
bpy.ops.import_mesh.stl(filepath="C:/Users/Sai/Documents/GitHub/Interactive-puppets/3d_models/bj.stl", filter_glob="*.stl", files=[{"name":"bj.stl", "name":"bj.stl"}],                 directory="C:/Users/Sai/Documents/GitHub/Interactive-puppets/3d_models/")
        

i=0
nextJoint=.001;
move_joint=0;
for ob in obs:
    prog = re.compile('Cylinder.0..')
    if  prog.match(ob.name):
        
        myObj = bpy.data.objects.get(ob.name)
        if(myObj.dimensions[2]==0): 
             
             continue 
        mesh_prepare(myObj)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        bpy.ops.mesh.edge_face_add()
              
        
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        height_object = myObj.location[2]+(myObj.dimensions[2]/2)
        
       
        #bpy.ops.import_mesh.stl(filepath="C:/Users/Sai/Documents/GitHub/Interactive-puppets/3d_models/bj.stl", filter_glob="*.stl", files=[{"name":"bj.stl", "name":"bj.stl"}],                 directory="C:/Users/Sai/Documents/GitHub/Interactive-puppets/3d_models/")
        
        if(i!=0):
            joint_id = str(nextJoint)
            joint = bpy.data.objects.get('Bj'+joint_id[1:])
            nextJoint+=.001
        else:
            
            joint = bpy.data.objects.get('Bj')   
        
        joint_dimension = joint.dimensions[2]/2
        myObj = bpy.data.objects.get(ob.name)
        if(i!=0):
          print(joint_dimension)
          move_joint = (((joint_dimension*2)-0.025)*i)
          bpy.ops.transform.translate(value=(0.0, 0,((joint_dimension*2)-0.085)*i))
        i+=1
        
        bpy.ops.import_mesh.stl(filepath="C:/Users/Sai/Documents/GitHub/Interactive-puppets/3d_models/bj.stl", filter_glob="*.stl", files=[{"name":"bj.stl", "name":"bj.stl"}],                 directory="C:/Users/Sai/Documents/GitHub/Interactive-puppets/3d_models/")
        
        
        mesh_prepare(joint)
        bpy.ops.object.mode_set(mode='OBJECT')
        height_object = height_object+ joint_dimension 
        print(height_object)
        bpy.ops.transform.translate(value=(0.0, 0,((height_object+move_joint)-0.005)))                 
        
       
        
        
        
        
    else:
        print('no match')
        


'''
 for ob in obs:
    prog = re.compile('Cylinder.0..')
    if  prog.match(ob.name):
   
       
'''