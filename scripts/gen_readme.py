import os
from mdutils.mdutils import MdUtils
from xml.etree import ElementTree

# Generate README.md
def generate_readme(export_path: str):
    mdFile = MdUtils(file_name=export_path, title='suzmemo')

    tag_names = get_title_and_links('../docs/tags/index.xml')
    tag_names = dict(sorted(tag_names, key=lambda x: x[0]))
    for tag in tag_names.keys():
        mdFile.new_header(level=1, title=tag)
        article_and_link = get_articles(tag)
        # TODO: double loop
        for a, l in article_and_link.items():
            mdFile.new_line(' - ' + mdFile.new_inline_link(link=l, text=a))
        mdFile.new_line('')
    mdFile.create_md_file()


# Get article titles and links
def get_articles(tag: str):
    tag = tag.lower()
    articles = get_title_and_links(f'../docs/tags/{tag}/index.xml')
    return articles

# Get xml items
def get_title_and_links(xml_path: str):
    result = {}
    tree = ElementTree.parse(xml_path)
    elem = tree.getroot()
    for item in elem.findall('.//item'):
        title = item.find('title').text
        link  = item.find('link').text
        result[title] = link
    return result

if __name__ == '__main__':
    generate_readme('README.md')
    