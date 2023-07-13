


# from typing import TypeAlias


class filter:

    _items = []
    def __init__(self, items = []):
        self._items = items

    def filter(self, item) -> bool:
        return item in self._items

# listStr : TypeAlias = list[str]

class filter_extension(filter):

    # def __init__(self, extension_list: list[str]):
    def __init__(self, extension_list: list):
        self._items = extension_list

    def filter(self, filename : str) -> bool:
        extension = str(filename)[-4:]
        return extension in self._items



from pathlib import Path

class filter_folder(filter):

    # def __init__(self, _:list = []):
    #     pass

    def filter(self, filePath : Path ) -> bool:
        # filePath = Path(filename)
        return filePath.is_dir()
    


class filter_hiddenFile(filter):

    # def __init__(self, _:list = []):
    #     pass

    def filter(self, filePath : Path) -> bool :
        filename = filePath.name
        return filename[0] == '.'
    

class file_filter_composition(filter):

    # def __init__(self, filter_list:list[filter]):
    def __init__(self, filter_list:list):
        self._items = filter_list

    def filter(self, filePath : Path) -> bool:
        for filter in self._items:
            if filter.filter(filePath):
                return True
        return False
    

# class filter_zip(filter):

#     # def __init__(self, _:list = []):
#     #     pass

#     def filter(file : str) -> bool :
#         return file[0] == '.'

class dynamic_filter(filter):

    # def __init__(self, _:list = []):
    #     pass

    def add_new_filter_items(self, item):
        self._items.append(item)

    