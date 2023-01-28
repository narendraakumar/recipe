import os


class FolderResource():
    def __init__(self,folder_path,file_path=None) -> None:
        self.dir = folder_path
        self.file_path = file_path

    @staticmethod
    def run_fast_scandir(dir, ext, recursive):    # dir: str, ext: list

        subfolders, files = [], []

        for f in os.scandir(dir):
            if f.is_dir():
                subfolders.append(f.path)
            if f.is_file():
                if os.path.splitext(f.name)[1].lower() in ext:
                    files.append(f.path)
        if not recursive:
            return subfolders,files

        for dir in list(subfolders):
            sf, f = FolderResource.run_fast_scandir(dir, ext)
            subfolders.extend(sf)
            files.extend(f)
        return subfolders, files

    def get_all_files(self,ext=['.py'],recursive=False):

        return FolderResource.run_fast_scandir(self.dir,ext,recursive)[1]

if __name__ == '__main__':
    print(FolderResource(folder_path='python_files').get_all_files())
