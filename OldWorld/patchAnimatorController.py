from unityparser import UnityDocument

extracted_controller_file = './extracted/WarriorAnimator V2.controller'
extracted_controller = UnityDocument.load_yaml(extracted_controller_file)

motion_map = {}

for entry in extracted_controller.entries:
    if entry.__class__.__name__ == 'AnimatorState':
        motion_map[entry.m_Name] = entry.m_Motion

original_controller_file = './original/WarriorAnimator V2.controller'
working_controller = UnityDocument.load_yaml(original_controller_file)

for entry in working_controller.entries:
    if entry.__class__.__name__ == 'AnimatorState':
        entry.m_Motion = motion_map[entry.m_Name]

working_controller.dump_yaml('./python_amended/WarriorAnimator V2.controller')
