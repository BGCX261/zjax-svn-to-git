from distutils.core import setup
import py2exe

setup(
     options = {
        "py2exe": {
                    "compressed": 1,
                    "optimize": 2,
                    "ascii": 0,
                    "bundle_files": 1
        }
    },
    zipfile=None,  
    windows=[
        {
            "script": "main.py", 
            "icon_resources": [(1, "main.ico")]
        }
    ],
    #console=["runapp.py",]
)