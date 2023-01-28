import importlib.util

class PythonFileRunner():
    def __init__(self,file_path) -> None:
        self.file_path = file_path
        self.specs = importlib.util.spec_from_file_location("binarytree",file_path)
        func = importlib.util.module_from_spec(self.specs)
        self.specs.loader.exec_module(func)
        self.func = func

    def method_runner(self,method_name,input:dict):
        outputs = getattr(self.func, method_name)(**input)
        return outputs

if __name__ == '__main__':
    py = PythonFileRunner("/Users/narendrakumar/MYSPACE/LEARNING/recipe/binarytree.py")
    print(py.method_runner("test",{"2":2}))