"""
These functions are helpers to generate the argument set required by Athera Compute job submissions, for different apps.

They follow the pattern provided by Compute submission plugins for in-Athera Apps. Some are recognizably the app arguments, others are interpreted by a script.

Placeholders are interpreted during Job creation, to enable splitting of Job frame ranges for a set of Parts.
"""
def get_houdini_arguments(output):
    return [
        "{{FRAME_RANGE_START}}",
        "{{FRAME_RANGE_FINISH}}",
        "{{FRAME_RANGE_INCREMENT}}",
        "{{FILE_PATH}}",
        output
    ]

def get_katana_arguments(render_node):
    return [
        "--batch",
        "--render-node",
        render_node,
        "--katana-file",
        "{{FILE_PATH}}",
        "-t",
        "{{FRAME_RANGE_START}}-{{FRAME_RANGE_FINISH}}"
    ]

def get_modo_arguments():
    return [
        "{{FILE_PATH}}",
        "default", # Output location not used, setting to default
        "{{FRAME_RANGE_START}}",
        "{{FRAME_RANGE_FINISH}}",
        "{{FRAME_RANGE_INCREMENT}}"
    ]

def get_nuke_arguments(write_node):
    return [
        "-X",
        write_node,
        "{{FILE_PATH}}",
        "{{FRAME_RANGE_START}}-{{FRAME_RANGE_FINISH}}"
    ]

# Returna a structure describing all available app IDs
# Example for retrieving the app ID of Nuke 11.2v4 compute:
# app_id=[app['app_id'] for app in athera.api.compute_arguments.get_app_ids() if app['app_name']=='Nuke 11' and app['type']=='COMPUTE' and app['version']=='11.2v4'][0]
def get_app_ids():
    return [
        {
            "app_name": "NukeX 11 + Cara VR",
            "type": "COMPUTE",
            "version": "11.2v4+2.1v3",
            "app_id": "51893592-aa30-4f57-9e9f-fbfc919619b4"
        },
        {
            "app_name": "NukeX 11 + Cara VR",
            "type": "COMPUTE",
            "version": "11.2v3+2.1v2",
            "app_id": "35dd2f9a-b86b-4407-90d6-47e4870ca9e4"
        },
        {
            "app_name": "NukeX + Cara VR 11.2v3+2.1v2 Bundled",
            "type": "COMPUTE",
            "version": "11.2v3+2.1v2",
            "app_id": "7018edca-c1d4-4148-a87a-5d74746f273d"
        },
        {
            "app_name": "Power NukeX + Cara VR 11.2v3+2.1v2 Bundled",
            "type": "COMPUTE",
            "version": "11.2v3+2.1v2",
            "app_id": "0b03ad41-9d4b-455f-a753-97570b0b3a09"
        },
        {
            "app_name": "Modo 12",
            "type": "COMPUTE",
            "version": "12.1v2",
            "app_id": "93ade357-dffe-4e87-a7d7-29013074e49b"
        },
        {
            "app_name": "Houdini FX Render 16.5.496 Bundled",
            "type": "COMPUTE",
            "version": "16.5.496",
            "app_id": "a238f464-37c6-4486-bf27-cd8b96ace706"
        },
        {
            "app_name": "Power Houdini Sim 16.5.496 Bundled",
            "type": "COMPUTE",
            "version": "16.5.496",
            "app_id": "83bef75b-850a-41be-b075-fedcb6a05c18"
        },
        {
            "app_name": "Modo 12.1v2 Bundled",
            "type": "COMPUTE",
            "version": "12.1v2",
            "app_id": "45d88ab9-a179-4585-bf37-65d5d2e89aa5"
        },
        {
            "app_name": "Houdini Sim 16.5.496 Bundled",
            "type": "COMPUTE",
            "version": "16.5.496",
            "app_id": "778a2bb7-f4b5-42c6-b1d8-639f82e32dc4"
        },
        {
            "app_name": "Nuke 11",
            "type": "COMPUTE",
            "version": "11.2v4",
            "app_id": "4d6c2992-5bb6-47d8-9464-5f30be969980"
        },
        {
            "app_name": "Houdini FX",
            "type": "COMPUTE",
            "version": "16.5.496",
            "app_id": "16c46871-7c63-400a-bc63-14f8acd537d1"
        },
        {
            "app_name": "Nuke 11",
            "type": "COMPUTE",
            "version": "11.2v3",
            "app_id": "c1609e27-3d00-496e-8c57-e79c8fdf7f76"
        },
        {
            "app_name": "Houdini FX",
            "type": "COMPUTE",
            "version": "17.0.352",
            "app_id": "8903e998-d098-49d5-a420-6d81593b8cba"
        },
        {
            "app_name": "Nuke 11.2v3 Bundled",
            "type": "COMPUTE",
            "version": "11.2v3",
            "app_id": "672234e2-fa75-43c4-99aa-011ab8092af7"
        },
        {
            "app_name": "Katana 3 + 3Delight",
            "type": "COMPUTE",
            "version": "3.0v6",
            "app_id": "6ec37733-0ad9-4dfe-aa6b-a6b5a6fc04cf"
        },
        {
            "app_name": "Katana + 3Delight 3.0v3 Bundled",
            "type": "COMPUTE",
            "version": "3.0v3",
            "app_id": "06d4b7bb-5eb1-459b-a380-623c98bacf97"
        },
        {
            "app_name": "Katana 3 + 3Delight",
            "type": "COMPUTE",
            "version": "3.0v3",
            "app_id": "06765622-b03c-474f-899c-538a91170505"
        },
        {
            "app_name": "FFmpeg",
            "type": "COMPUTE",
            "version": "4.1",
            "app_id": "c2371064-9570-4009-8bfa-25b5ed984f51"
        },
        {
            "app_name": "VLC (alpha)",
            "type": "COMPUTE",
            "version": "3.0.6",
            "app_id": "94b20ac2-1262-448a-9dab-2298bfed3ec5"
        },
        {
            "app_name": "Katana 3 + 3Delight",
            "type": "INTERACTIVE",
            "version": "3.0v3",
            "app_id": "02d103e0-bade-464c-a898-aac7c240789a"
        },
        {
            "app_name": "Katana + 3Delight 3.0v3 Bundled",
            "type": "INTERACTIVE",
            "version": "3.0v3",
            "app_id": "d5b23dc6-1161-4171-8910-2fced5090bbf"
        },
        {
            "app_name": "Katana 3 + 3Delight",
            "type": "INTERACTIVE",
            "version": "3.0v6",
            "app_id": "9511f3be-103a-4c27-9b7d-0205d515728a"
        },
        {
            "app_name": "Mari 4.1v2 Bundled",
            "type": "INTERACTIVE",
            "version": "4.1v2",
            "app_id": "d2074b08-cb46-448e-a891-33bffb7b6350"
        },
        {
            "app_name": "Mari 4",
            "type": "INTERACTIVE",
            "version": "4.1v2",
            "app_id": "7d8d2f02-c93f-4b4e-a1f3-e34b49e270cf"
        },
        {
            "app_name": "Mari 4",
            "type": "INTERACTIVE",
            "version": "4.2v1",
            "app_id": "1fe1ca3e-3ca2-4bb8-8a7a-529ec4dcc20f"
        },
        {
            "app_name": "Power NukeX 11.2v3 Bundled",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "e27ed991-1da5-45c4-9ad5-bbb6e1de4615"
        },
        {
            "app_name": "Power Nuke Studio 11.2v3 Bundled",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "7cf7c323-9489-4804-a144-b8dea11563a5"
        },
        {
            "app_name": "Nuke 11.2v3 Bundled",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "1aa25efc-382e-4873-80f3-3fbd831546a5"
        },
        {
            "app_name": "NukeX 11.2v3 Bundled",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "b5735540-381b-45af-bae3-148adf8a50f3"
        },
        {
            "app_name": "Nuke Studio 11.2v3 Bundled",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "f141fa6d-8ea3-45a1-8cf3-a41520039b4f"
        },
        {
            "app_name": "Power Katana + 3Delight 3.0v3 Bundled",
            "type": "INTERACTIVE",
            "version": "3.0v3",
            "app_id": "4200b82d-17e9-4c43-935f-c93bfab0db48"
        },
        {
            "app_name": "Nuke Studio 11",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "9a3ba67f-fc88-452f-96b4-da1d2fe8b7f6"
        },
        {
            "app_name": "Nuke 11",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "d88a6981-0f7e-449d-ba72-95564aa0c110"
        },
        {
            "app_name": "NukeX 11",
            "type": "INTERACTIVE",
            "version": "11.2v3",
            "app_id": "16ccadff-3046-4179-bfd7-78b630225985"
        },
        {
            "app_name": "Houdini FX",
            "type": "INTERACTIVE",
            "version": "17.0.352",
            "app_id": "0880164e-aada-4164-ac76-15bfe865954d"
        },
        {
            "app_name": "Nuke 11",
            "type": "INTERACTIVE",
            "version": "11.2v4",
            "app_id": "73d2f4d0-e148-4fc2-b843-81d0a53aca4b"
        },
        {
            "app_name": "Houdini FX",
            "type": "INTERACTIVE",
            "version": "16.5.496",
            "app_id": "6cbf87a3-2aee-47ef-a2cc-217652b6e6e7"
        },
        {
            "app_name": "NukeX 11",
            "type": "INTERACTIVE",
            "version": "11.2v4",
            "app_id": "66a896e4-ffdb-4880-87fd-87b0fffe4b1d"
        },
        {
            "app_name": "Nuke Studio 11",
            "type": "INTERACTIVE",
            "version": "11.2v4",
            "app_id": "2edfb284-4424-46e8-88ad-b18b779fa977"
        },
        {
            "app_name": "Modo 12.1v2 Bundled",
            "type": "INTERACTIVE",
            "version": "12.1v2",
            "app_id": "e2878a4f-f431-4813-9402-3f86b95aef9e"
        },
        {
            "app_name": "Power Houdini FX 16.5.496 Bundled",
            "type": "INTERACTIVE",
            "version": "16.5.496",
            "app_id": "026a2573-d00d-4ebe-84bc-ac27d2d9b067"
        },
        {
            "app_name": "Houdini FX 16.5.496 Bundled",
            "type": "INTERACTIVE",
            "version": "16.5.496",
            "app_id": "6ad73e13-7df4-4672-b4bf-d2e9980eb9f1"
        },
        {
            "app_name": "Modo 12",
            "type": "INTERACTIVE",
            "version": "12.1v2",
            "app_id": "7dec8ef9-a19c-4ee4-b4f8-dea1d9db224f"
        },
        {
            "app_name": "DJV View",
            "type": "INTERACTIVE",
            "version": "1.1.2",
            "app_id": "fe81ef6e-dede-4bc7-aaf9-75294b21048f"
        },
        {
            "app_name": "NukeX + Cara VR 11.2v3+2.1v2 Bundled",
            "type": "INTERACTIVE",
            "version": "11.2v3+2.1v2",
            "app_id": "4b3e8550-e4e6-4039-ac8c-95d70150a3d3"
        },
        {
            "app_name": "DJV View 1.1.2 Bundled",
            "type": "INTERACTIVE",
            "version": "1.1.2",
            "app_id": "3629e7a0-1976-4471-988d-a018ea7503f0"
        },
        {
            "app_name": "NukeX 11 + Cara VR",
            "type": "INTERACTIVE",
            "version": "11.2v3+2.1v2",
            "app_id": "b3b6be78-1eef-4225-b3d4-d32dc61e94f0"
        },
        {
            "app_name": "Toolbox",
            "type": "INTERACTIVE",
            "version": "0.1.0",
            "app_id": "85321d27-f02c-47cc-8253-5a70192c8b7d"
        },
        {
            "app_name": "Toolbox 0.1.0 Bundled",
            "type": "INTERACTIVE",
            "version": "0.1.0",
            "app_id": "cd51f470-fed6-498d-9c31-779b09e949ac"
        },
        {
            "app_name": "NukeX 11 + Cara VR",
            "type": "INTERACTIVE",
            "version": "11.2v4+2.1v3",
            "app_id": "cdbdff07-ddb7-4898-8e24-955de4a541d7"
        },
        {
            "app_name": "Blender 2.79b Bundled",
            "type": "INTERACTIVE",
            "version": "2.79b",
            "app_id": "f53c4621-8ef7-4a7e-9370-40a7c75e2c54"
        },
        {
            "app_name": "Blender",
            "type": "INTERACTIVE",
            "version": "2.79b",
            "app_id": "917187a4-222d-41fe-86d4-bb31cff70421"
        },
        {
            "app_name": "Gaffer 0.46.0.0 Bundled",
            "type": "INTERACTIVE",
            "version": "0.46.0.0",
            "app_id": "3f3343f2-b579-4682-8c36-3e4d62d01fb8"
        },
        {
            "app_name": "Gaffer",
            "type": "INTERACTIVE",
            "version": "0.46.0.0",
            "app_id": "c0442da4-95dc-4c5f-8dfe-902fb2bf84ab"
        },
        {
            "app_name": "Gaffer",
            "type": "INTERACTIVE",
            "version": "0.52.1.0",
            "app_id": "78f2fd26-dcdd-4b84-aa1b-2e27cbea90cc"
        },
        {
            "app_name": "Hiero 11",
            "type": "INTERACTIVE",
            "version": "11.3v2",
            "app_id": "36252053-c839-4603-a6b4-b721378a815b"
        }
    ]
