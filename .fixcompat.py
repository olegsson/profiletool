from glob import iglob
import re

files = iglob('**/*.py')

search = 'qgis.PyQt'
destroy = 'PyQt4'

for py in files:
    with open(py, 'r') as f:
        content = f.read()
    if search in content:
        content = re.sub(
            search, destroy, content
        )
        with open(py, 'w') as f:
            f.write(content)
        print('rewrote', py)
