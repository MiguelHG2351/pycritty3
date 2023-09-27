from pathlib import Path

DIRECTORIES = {
    'local_fonts': Path.home() / '.local/share/fonts',
    'global_fonts': Path('/usr/share/fonts'),
}

print(DIRECTORIES)