from collections import defaultdict
def findDuplicate(self, paths):
    result=defaultdict(list)
    for path in paths:
        parts=path.split(" ")
        root=parts[0]
        for file in parts[1:]:
            name,content=file.split("(")
            content=content[:-1]
            full_path=f"{root}/{name}"
            result[content].append(full_path)
    return [group for group in result.values() if len(group)>1]  