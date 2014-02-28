import bpy

# Which group to find?
mesh = bpy.data.objects['Cylinder']

#for g in mesh.vertex_groups

#print(len(mesh.vertex_groups))


i = 0
while i < len(mesh.vertex_groups):
    print(i)
    
    groupName = mesh.vertex_groups[i].name
    
    # Use the active object
    obj = bpy.context.active_object
    
    # Make sure you're in edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Deselect all verts
    bpy.ops.mesh.select_all(action='DESELECT')
    
    # Make sure the active group is the one we want
    bpy.ops.object.vertex_group_set_active(group=groupName)
    
    # Select the verts
    bpy.ops.object.vertex_group_select()
    
    bpy.ops.mesh.separate(type='SELECTED')
    
    i += 1 

