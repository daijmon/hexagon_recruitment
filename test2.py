# Test 2
# -----
# Scan all files in any folder e.g. usr/share/doc recursively and group them by first three
# letters. For each 3-letter group sort the filenames in that group by the
# actual size of the files in reverse order. Store the resulting structure in a
# dictionary called result:
#
# Example:
#
# {
# 'aam': [(42281, 'aamfigs.pdf'), (1219, 'aamfigs.tex')],
# 'aas': [(113610, 'aassymbols.pdf'), (4753, 'aassymbols.tex.gz')],
#
# ...
#
# 'zxj': [(132386, 'zxjafont.pdf'), (3182, 'zxjafont.tex.gz'
# 'zz_': [(654,'zz_translate_test.crm')]
# }
import os


def scan_directories(path) -> object:
    """Recursive scan of directory to create grouped dictionary from found files"""
    result = {}
    file_size = 0
    # Populate result dictionary
    for root, _, file_names in os.walk(path):
        for file in file_names:
            try:
                full_file_path = os.path.join(root, file)
                try:
                    file_size = os.stat(full_file_path).st_size
                except FileNotFoundError as e:
                    print('{details} {filename}'.format(details=e.strerror, filename=e.filename))
                    continue
                result[file[:3]].append((file_size, file))
            except KeyError:
                result[file[:3]] = []
                result[file[:3]].append((file_size, file))
    # Sort result dictionary
    for key, value in result.items():
        result[key] = sorted(value, key=lambda tup: tup[0], reverse=True)
    return result


if __name__ == '__main__':
    dir_path = '/usr/share/doc'
    print(scan_directories(dir_path))
