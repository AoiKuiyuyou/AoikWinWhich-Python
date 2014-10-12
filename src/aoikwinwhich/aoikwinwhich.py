# coding: utf-8

#
import os
import sys


#
def list_uniq(item_s):
    item_s_uniq = []

    for item in item_s:
        if item not in item_s_uniq:
            item_s_uniq.append(item)

    return item_s_uniq

# "exe" means executable, not just paths ending with ".exe"
def find_exe_paths(prog):
    # 8f1kRCu
    env_pathext = os.environ.get('PATHEXT', None)

    # 4fpQ2RB
    if not env_pathext:
        # 9dqlPRg
        return []

    # 6qhHTHF
    # Split into a list of extensions
    ext_s = env_pathext.split(os.pathsep)

    # 2pGJrMW
    # Strip
    ext_s = [x.strip() for x in ext_s]

    # 2gqeHHl
    # Remove empty.
    # Must be done after the stripping at 2pGJrMW.
    ext_s = [x for x in ext_s if x != '']

    # 2zdGM8W
    # Convert to lowercase
    ext_s = [x.lower() for x in ext_s]

    # 2fT8aRB
    # Uniquify
    ext_s = list_uniq(ext_s)

    # 4ysaQVN
    env_path = os.environ.get('PATH', None)

    # 5gGwKZL
    if not env_path:
        # 7bVmOKe
        # Go ahead with "dir_path_s" being empty
        dir_path_s = []
    else:
        # 6mPI0lg
        # Split into a list of dir paths
        dir_path_s = env_path.split(os.pathsep)

    # 5rT49zI
    # Insert empty dir path to the beginning.
    #
    # Empty dir handles the case that "prog" is a path, either relative or
    #  absolute. See code 7rO7NIN.
    dir_path_s.insert(0, '')

    # 2klTv20
    # Uniquify
    dir_path_s = list_uniq(dir_path_s)

    # 9gTU1rI
    # Check if "prog" ends with one of the file extension in "ext_s".
    #
    # "ext_s" are all in lowercase, ensured at 2zdGM8W.
    prog_lc = prog.lower()

    prog_has_ext = prog_lc.endswith(tuple(ext_s))
    # "endswith" requires tuple, not list.

    # 6bFwhbv
    exe_path_s = []

    for dir_path in dir_path_s:
        # 7rO7NIN
        # Synthesize a path
        if dir_path == '':
            path = prog
        else:
            path = os.path.join(dir_path, prog)

        # 6kZa5cq
        # If "prog" ends with executable file extension
        if prog_has_ext:
            # 3whKebE
            if os.path.isfile(path):
                # 2ffmxRF
                exe_path_s.append(path)

        # 2sJhhEV
        # Assume user has omitted the file extension
        for ext in ext_s:
            # 6k9X6GP
            # Synthesize a path with one of the file extensions in PATHEXT
            path_2 = path + ext

            # 6kabzQg
            if os.path.isfile(path_2):
                # 7dui4cD
                exe_path_s.append(path_2)

    # 8swW6Av
    # Uniquify
    exe_path_s = list_uniq(exe_path_s)

    # 7y3JlnS
    return exe_path_s

#
def main():
    # 9mlJlKg
    # If not exactly one command argument is given
    if len(sys.argv) != 2:
        # 7rOUXFo
        # Print program usage
        usage = r"""Usage: aoikwinwhich PROG

#/ PROG can be either name or path
aoikwinwhich notepad.exe
aoikwinwhich C:\Windows\notepad.exe

#/ PROG can be either absolute or relative
aoikwinwhich C:\Windows\notepad.exe
aoikwinwhich Windows\notepad.exe

#/ PROG can be either with or without extension
aoikwinwhich notepad.exe
aoikwinwhich notepad
aoikwinwhich C:\Windows\notepad.exe
aoikwinwhich C:\Windows\notepad"""

        print(usage)

        # 3nqHnP7
        return 1

    #
    assert len(sys.argv) == 2

    # 9m5B08H
    # Get executable name or path
    prog = sys.argv[1]

    # 8ulvPXM
    # Find executable paths
    exe_path_s = find_exe_paths(prog)

    # 5fWrcaF
    # If has found none
    if not exe_path_s:
        # 3uswpx0
        return 2
    # If has found some
    else:
        # 9xPCWuS
        # Print result
        print('\n'.join(exe_path_s))

        # 4s1yY1b
        return 0

    #
    assert 0

# 4zKrqsC
# Program entry
if __name__ == '__main__':
    sys.exit(main())
