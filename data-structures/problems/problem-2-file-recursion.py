import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

    Returns:
    a list of paths
    """
    if suffix == 'c':
        print (path)

    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            suffix = f.split('.')[-1]
            print(os.path.join(path, f))
        if os.path.isdir(os.path.join(path, f)):
            find_files('c', os.path.join(path, f))
    return None
 
if __name__ == '__main__':
    find_files('c', 'testdir')
