import bpy

class CustomPanel(bpy.types.Panel):
    """A Custom Panel in the Viewport Toolbar"""
    bl_label = "Cable Monsters Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Modify Model:")

        split = layout.split()
        col = split.column(align=True)

        col.operator("mesh.loopcut_slide", text="Add Joint", icon='MESH_PLANE')
        col.operator("mesh.primitive_torus_add", text="Delete Joint", icon='MESH_TORUS')
        col.operator("mesh.primitive_torus_add", text="Add cable supports", icon='MESH_TORUS')

def register():
    bpy.utils.register_class(CustomPanel)

def unregister():
    bpy.utils.unregister_class(CustomPanel)

if __name__ == "__main__":
    register()