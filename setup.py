import cx_Freeze
executables = [
    cx_Freeze.Executable(script="main.py", icon="icospace.ico")
]
cx_Freeze.setup(
    name = "SpaceMarker",
    options = {
        "build_exe":{
            "packages": ["pygame"],
            "include_files": [
                "fundospace.jpg",
                "space.png",
                "Space_Machine_Power.mp3",
                "pontos.txt"
            ]
        }
    } , executables = executables
)