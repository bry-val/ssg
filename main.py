from src.utils.page_functions import generate_pages_recursive, dir_copy

dir_path_content = '/home/bryan/bootdev/ssg/content/'
template_path = '/home/bryan/bootdev/ssg/template.html'
dest_dir_path = '/home/bryan/bootdev/ssg/public/'
STATIC_PATH = '/home/bryan/bootdev/ssg/static'
PUBLIC_PATH = '/home/bryan/bootdev/ssg/public'


# CONTENT_DIR = '/home/bryan/bootdev/ssg/content/majesty/index.md'
# OUTPUT_DIR = '/home/bryan/bootdev/ssg/public/majesty/index.html'


def main():
    # generate_page(CONTENT_DIR, DEFAULT_TEMPLATE, OUTPUT_DIR)
    dir_copy(STATIC_PATH, PUBLIC_PATH)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)


if __name__ == "__main__":
    main()
