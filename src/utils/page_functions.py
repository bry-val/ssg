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
    md_filepath = os.path.join(from_path, 'index.md')
    html_filepath = os.path.join(dest_path, 'index.html')

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(html_filepath), exist_ok=True)

    print(f"Generating page from {md_filepath} to {html_filepath} using {template_path}")

    with open(md_filepath, 'r') as md_file:
        md_blocks = markdown_to_blocks(md_file.read())
    html = [block_to_html(block) for block in md_blocks]

    with open(template_path, 'r') as template_file:
        template = template_file.read()

    with open(html_filepath, 'w') as outfile:
        outfile.write(
            template.replace("{{ Title }}", extract_title(md_blocks)).replace("{{ Content }}", "\n".join(html)))


DESTINATION = "/home/bryan/bootdev/ssg"
TEMPLATE_PATH = "/home/bryan/bootdev/ssg/template.html"


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file == 'index.md':  # Only process 'index.md' files
                from_path = root
                relative_path = os.path.relpath(root, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path)

                # Ensure the destination directory exists
                os.makedirs(dest_path, exist_ok=True)

                generate_page(from_path, template_path, dest_path)
