import os
import re
import shutil

import unidecode

from YAFPA.common import file_checking as checking
from YAFPA.common import global_value as settings

vault = settings.vault
img = settings.img


def get_image(image):
    image = os.path.basename(image)
    for sub, dirs, files in os.walk(vault):
        for file in files:
            filepath = sub + os.sep + file
            if unidecode.unidecode(image) in unidecode.unidecode(file):
                return filepath


def flags_transform(line, flag):
    img_flags = re.search("[\|\+\-](.*)[]{1,2})]", flag)
    if img_flags:
        img_flags = img_flags.group(0)
        img_flags = img_flags.replace("|", "")
        img_flags = img_flags.replace("]", "")
        img_flags = img_flags.replace(")", "")
        img_flags.replace("(", "")
    else:
        img_flags = ""
    link = re.search("(\[{2}|\().*\.(png|jpg|jpeg|gif)", flag)
    final_text = link.group(0)
    final_text = final_text.replace("(", "")
    final_text = final_text.replace("%20", " ")
    final_text = final_text.replace("[", "")
    final_text = final_text.replace("]", "")
    final_text = final_text.replace(")", "")
    final_text = os.path.basename(final_text)
    image_path = get_image(final_text)
    if image_path:
        shutil.copyfile(image_path, f"{img}/{final_text}")
        final_text = f"../assets/img/{final_text}"
        IAL = f"[{img_flags}]({final_text})"
        line = line.replace(flag, IAL)
    return line


def move_img(line):
    flags = re.search("(\[{2}|\().*\.(png|jpg|jpeg|gif)(\|)?(.*)?[-+]?(.*)?\]{2}", line)
    if flags:
        flags = flags.group().split("!")
        if len(flags) > 1:
            for flag in flags:
                line = flags_transform(line, flag)
        else:
            flags = flags[0]
            line = flags_transform(line, flags)
    return line


def excalidraw_convert(line):
    if ".excalidraw" in line:
        # take the png img from excalidraw
        line = line.replace(".excalidraw", ".excalidraw.png")
        line = line.replace(".md", "")
    return line


def convert_no_embed(line):
    final_text = line
    if re.match("\!\[{2}", line) and not re.match("(.*)\.(png|jpg|jpeg|gif)", line):
        final_text = line.replace("!", "")  # remove "!"
        final_text = re.sub("#\^(.*)", "]]", final_text)  # Link to block doesn't work
    return final_text


def transform_link(line, link):
    title = re.search("\[(.*)]", link)
    if title:
        title = title.group(0)
        title = title.replace("[", "")
        title = title.replace("]", "")
    else:
        title = ""
    links = re.search("\((.*)\)", link)
    if links:
        final_text = links.group(1)
        final_text = final_text.replace("%20", " ")
        final_text = final_text.replace(".md", "")
        IAL = f"[[{final_text}\|{title}]]"
        line = line.replace(link, IAL)
    return line


def convert_to_wikilink(line):
    final_text = line
    if re.search("\[(.*)]\((.*)\)", final_text):
        links = re.search("\[(.*)]\((.*)\)", final_text).group().split()
        if len(links) > 1:
            for link in links:
                if not re.search("https?:\/\/", link) or link == "":
                    line = transform_link(line, link)
        else:
            links = links[0]
            if not re.search("https?:\/\/", links):
                line = transform_link(line, links)
    elif re.search("https?:\/\/", final_text):
        link = re.search("<?(.*)?https?:\/\/.*", final_text).group()
        spl = re.split(">", link)
        links = [x for x in spl if re.search("https?:\/\/.*", x)]
        if len(links) > 1:
            for f in links:
                if not "<" in f:
                    line = final_text.replace(f.strip(), f"[{f.strip()}]({f.strip()})")
        else:
            f = links[0]
            if not "<" in f:
                line = final_text.replace(f.strip(), f"[{f.strip()}]({f.strip()})")
    return line



def heading_conversion(final_text, line, title, all_file, folder):
    file = title.replace('.md', '')
    if re.search(
            '\[{2}(.*)#(.*)]{2}', final_text
            ):  # title working → Convertion for the blog
        # Need to be converted to []() links
        link = re.search('\[{2}(.*)#(.*)]{2}', final_text)
        file_name = re.search('\[{2}(.*)#', final_text)
        file_name = file_name.group().replace('#', '').replace('[', '')
        if re.search('\|', final_text):
            # get headings
            heading = re.search('\|(.*)\]{2}', final_text).group().replace(']', '')

            heading = '[' + heading.replace('|', '') + ']'
        else:
            heading = ""
        # [heading](link !) → #things

        link = re.search('#(.*)(\|)?', link.group())
        if heading == "":
            title = link.group(0).lstrip()
            title = title.replace(']', '')
            title = title.replace('#', '')
            heading = '[' + title + ']'
        link = link.group(1).lower()
        link = re.sub('\|(.*)', '', link)
        section = re.sub('[^ \w\-\d_]', '', link)
        section = re.sub('[^\w\d]', '-', section)
        if file_name != file :
            file_name_pattern = file_name + '.md'
            check = checking.check_file(file_name_pattern, folder, all_file)
            final_text = heading + '(' + file_name.replace(' ', '-') + '#' + section + ')'
            if check == "NE":
                final_text = "**" + final_text + "**{: .link_error}"
        else:
            final_text = heading + '(#' + section + ')'
        final_text = re.sub('\[{2}(.*)\]{2}', final_text, line)


    return final_text

def link_image_conversion(line, meta, title, all_file, folder):
    final_text = line
    if re.search("(\[{2}|\[).*", final_text):
        final_text = convert_to_wikilink(line)
        final_text = excalidraw_convert(final_text)
        if re.search("\^\w+", final_text) and not re.search("\[\^\w+\]", final_text):
            # remove block id
            final_text = re.sub("#\^\w+", "", final_text)

        if "embed" in meta.keys() and meta["embed"] == False:
            final_text = convert_no_embed(final_text)
        else:
            final_text = transluction_note(final_text)
        final_text = heading_conversion(final_text, line, title, all_file, folder)
        if not '\|' in final_text:
            final_text = final_text.replace('|', '\|')
    return final_text

def transluction_note(line):
    # If file (not image) start with "![[" : transluction with rmn-transclude (exclude
    # image from that)
    # Note : Doesn't support partial transluction for the moment ; remove title
    final_text = line
    if (
        re.search("\!\[", line)
        and not re.search("(png|jpg|jpeg|gif)", line)
        and not re.search("https", line)
    ):
        final_text = line.replace("!", "")  # remove "!"
        final_text = re.sub("#(.*)", "]]", final_text)
        final_text = re.sub("\\|(.*)", "]]", final_text)  # remove Alternative title
        final_text = re.sub("]]", "::rmn-transclude]]", final_text)
    return final_text
