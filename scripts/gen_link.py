import os

directory = input()

files = os.listdir(directory)

files = sorted(files)

for file_name in files:
    name, extension = os.path.splitext(file_name)
    print(fr'[{name}]({{< ref "{file_name}">}})  ')