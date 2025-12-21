# /**
#  * @author @hopsyder
#  * @organization Nexus Partners
#  * @description Script de nettoyage pour corriger les inclusions multi-lignes
#  * @created 2025-12-22
#  */

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pour trouver les @@include(...) qui s'étendent sur plusieurs lignes
    def replacement(match):
        # On remplace les sauts de ligne et on réduit les espaces multiples
        cleaned = match.group(0).replace('\n', ' ').replace('\r', ' ')
        return re.sub(r'\s+', ' ', cleaned)
    
    # Correction des @@include
    new_content = re.sub(r'@@include\([^)]+\)', replacement, content, flags=re.MULTILINE | re.DOTALL)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes: {filepath}")

src_dir = 'src'
if os.path.exists(src_dir):
    for filename in os.listdir(src_dir):
        if filename.endswith('.html'):
            fix_file(os.path.join(src_dir, filename))
else:
    print(f"Directory {src_dir} not found.")
