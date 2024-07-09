from src.utils.page_functions import generate_page


def main():
    generate_page("/home/bryan/bootdev/ssg/content/index.md", "/home/bryan/bootdev/ssg/template.html",
                  "/home/bryan/bootdev/ssg/public/index.html")


if __name__ == "__main__":
    main()
