import os
import re
from natsort import natsorted

directory = input()

files = os.listdir(directory)

def extract_number(s):
    # 正規表現で数値を抽出
    match = re.search(r'【([\d\.]+)】', s)
    if match:
        return [float(t) if t.replace('.', '', 1).isdigit() else float('inf') for t in match.group(1).split('.')]
    else:
        return [9999]

files = sorted(files, key=extract_number)

for file_name in files:
    name, extension = os.path.splitext(file_name)
    print(fr'[{name}]({{{{< ref "{file_name}">}}}})  ')