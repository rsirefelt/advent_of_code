class Folder:
    def __init__(self, folder_path, folder_content) -> None:
        self.inner_dirs = []
        self.files = dict()
        for content in folder_content:
            if content.startswith('dir'):
                self.inner_dirs.append(folder_path + content.split()[-1] + '/')
            else:
                self.files[content.split()[-1]] = int(content.split()[0])


def calculate_all_folder_sizes(folders):
    folder_sizes = dict()
    while len(folder_sizes) < len(folders):
        for folder_name, folder_content in folders.items():
            if folder_name in folder_sizes:
                continue

            folder_size = 0
            can_calculate = True
            for folder in folder_content.inner_dirs:
                if folder not in folder_sizes:
                    can_calculate = False
                    break
                else:
                    folder_size += folder_sizes[folder]
            if not can_calculate:
                continue
            folder_size += sum(s for s in folder_content.files.values())
            folder_sizes[folder_name] = folder_size
    return folder_sizes


folders = dict()
current_path = '/'
this_path = ''
folder_content = None
with open('inputs/day7') as f:
    for line in f:
        line_content = line.rstrip().split()
        if line_content[1] == 'cd':
            if folder_content is not None:
                folders[this_path] = Folder(this_path, folder_content)
                folder_content = None

            if line_content[2] == '..':
                current_path = '/'.join(current_path.split('/')[:-2]) + '/'
            elif line_content[2] != '/':
                current_path += f'{line_content[2]}/'
        elif line_content[1] == 'ls':
            this_path = current_path
            folder_content = []
        else:
            folder_content.append(line.rstrip())
    if folder_content is not None:
        folders[this_path] = Folder(this_path, folder_content)

folder_sizes = calculate_all_folder_sizes(folders)

print(sum(v for v in folder_sizes.values() if v <= 100000))

space_needed = 30000000 - (70000000 - folder_sizes['/'])
min_folder_size = 70000000
for folder_size in folder_sizes.values():
    if folder_size >= space_needed and folder_size < min_folder_size:
        min_folder_size = folder_size
print(min_folder_size)
