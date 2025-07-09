import os
from dll_utils import DllInjector


if __name__ == "__main__":

    pid = 15644
    dll_path = "./simple.dll"
    dll_name = os.path.basename(dll_path)

    d = DllInjector()

    # Inject DLL
    d.inject(pid, dll_path)
    # # Uninject DLL (Unload)
    d.uninject(pid, dll_name)
