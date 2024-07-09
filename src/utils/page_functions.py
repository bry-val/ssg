import os.path
import shutil

from src.utils.block_functions import markdown_to_blocks, block_to_html


def extract_title(markdown_blocks):
    if not markdown_blocks[0].startswith('# '):
        raise Exception("Markdown file needs to start with h1 header")
    else:
        return markdown_blocks[0][2:]


def dir_copy(static_dir, public_dir):
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    if not os.path.exists(static_dir):
        raise FileNotFoundError("static folder does not exist, please create one")

    for path in os.listdir(static_dir):
        working_dir = f"{static_dir}/{path}"
        if os.path.isfile(working_dir):
            shutil.copy(working_dir, public_dir)
        else:
            pub_path = f"{public_dir}/{path}"
            dir_copy(working_dir, pub_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as md_file:
        md_blocks = markdown_to_blocks(md_file.read())
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    html = []
    for block in md_blocks:
        html.append(block_to_html(block))
    dir_copy('/home/bryan/bootdev/ssg/static', '/home/bryan/bootdev/ssg/public')
    with open(dest_path, 'w') as outfile:
        outfile.write(
            template.replace("{{ Title }}", extract_title(md_blocks)).replace("{{ Content }}", "\n".join(html)))
    return
