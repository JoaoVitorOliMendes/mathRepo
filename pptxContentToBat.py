from pathlib import Path
from tika import parser
import re

directory = './Musicas/'

for file in Path(directory).iterdir():
    if file.is_file():
        print(file.name)
        print("----------------------")
        with open('./bats/' + file.stem + '.bat', 'w') as newFile:
            parsed = parser.from_file(directory + file.name)
            if parsed["content"]:
                newFile.write('goto start\n')
                newFile.write(re.sub(r"\n\n", "", parsed["content"]))
                newFile.write('\n:start\n')
                newFile.write('start %~dp0..\\Musicas\\' + file.name)
