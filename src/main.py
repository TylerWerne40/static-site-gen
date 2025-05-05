from textnode import TextNode, TextType
import sys
import os, re
import shutil
from markdown_blocks import markdown_to_html_node

def copy_folder(source, dest, first_run=True):
    
    if os.path.exists(dest) and first_run:
        shutil.rmtree(dest)

    os.makedirs(dest, exist_ok=True)

    paths = os.listdir(source)
    for obj in paths:
        src_path = os.path.join(source, obj)
        dest_path = os.path.join(dest, obj)
        if os.path.isdir(src_path):
            copy_folder(src_path, dest_path, False)
        else:
            shutil.copy2(src_path, dest_path)
    return

def extract_title(markdown):
    lines = markdown.splitlines()
    for i in lines:
        if '# ' == i[:2]:
            return i[2:].lstrip().rstrip()
    return ''

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    

    os.makedirs(dest_dir_path, exist_ok=True)
    
    paths = os.listdir(dir_path_content)
    for obj in paths:
        
        src_path = os.path.join(dir_path_content, obj)
        dest_path = os.path.join(dest_dir_path, obj)
        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path, basepath)
        else:
            dest_path = os.path.join(dest_dir_path, obj.replace('.md', '.html'))
            generate_page(src_path, template_path, dest_path, basepath)
    return

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page form {from_path} to {dest_path} using {template_path}')
    fro = open(from_path, 'r')
    f_contents = fro.read()
    # print(f_contents)
    # print('Above is f_contents. Below is html')
    fro.close()
    tem = open(template_path)
    t_contents = tem.read()
    tem.close()
    f_html = markdown_to_html_node(f_contents).to_html()
    # print(f_html)
    title = extract_title(f_contents)
    t_contents = t_contents.replace(r'{{ Title }}', title)
    t_contents = t_contents.replace(r'{{ Content }}', f_html)
    t_contents = t_contents.replace(r'href="/', rf'href={basepath}')
    t_contents = t_contents.replace(r'src="/', rf'src={basepath}')
    to = open(dest_path, 'w')
    to.write(t_contents)
    to.close()
    return

def main():
    basepath = sys.argv[1]
    if basepath is None:
        basepath = '/'

    tn = TextNode('hi', TextType.BOLD, 'https://www.boot.dev')
    print(tn)
    copy_folder('./static', './docs')
    generate_page('./content/index.md', './template.html', './docs/index.html', basepath)
    generate_pages_recursive('./content/', './template.html', './docs/', basepath)

main()
