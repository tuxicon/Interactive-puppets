import bpy

# Which group to find?
groupName = 'Bone.001'

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

# Store the mesh
mesh = obj.data

# Get the selected verts
selVerts = [v for v in mesh.vertices if v.select]

# Get the index of the required group
index = obj.vertex_groups[groupName].index

# Get the vert weights
weights = [v.groups[index].weight for v in selVerts]

print(weights)


ob = bpy.data.objects['Cube']
vg = ob.vertex_groups[0]

for v in ob.data.vertices:
    for g in v.groups:
        if g.group == vg.index:
            print("Vertex "+str(v.index)+" is part of "+vg.name)
            v.co.z += 1