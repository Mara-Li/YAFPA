import os
import re
from itertools import zip_longest
from pathlib import Path

import yaml

from YAFPA.common import global_value as settings

BASEDIR = Path(settings.BASEDIR)

def code_blocks(start_list, end_list):
    start_bug = []
    end_bug = []
    bug = [(x, y) for x, y in zip_longest(start_list, end_list, fillvalue=-1)]
    for i in bug:
        if i[0] > i[1]:
            start_bug.append(i[0])
        elif i[0] == -1:
            end_bug.append(i[1])
    merged = []
    for i in start_bug:
        for j in end_bug:
            if i < j:
                merged.append((i, j))
    no_bug = [(x, y) for x, y in zip_longest(start_list, end_list, fillvalue=-1) if
              x != -1 and x < y]
    merged = no_bug + merged
    return merged

def admonition_logo(type, line):
    admonition = {
        "note": "🖊️",
        "seealso": "🖊️",
        "abstract": "📝",
        "summary": "📝",
        "tldr": "📝",
        "info": "ℹ️",
        "todo": "ℹ️",
        "tip": "🔥",
        "hint": "🔥",
        "important": "🔥",
        "success": "✨",
        "check": "✨",
        "done": "✨",
        "question": "❓",
        "help": "❓",
        "faq": "❓",
        "warning": "⚠️",
        "caution": "⚠️",
        "attention": "⚠️",
        "failure": "❌",
        "fail": "❌",
        "missing": "❌",
        "danger": "⚡",
        "error": "⚡",
        "bug": "🐛",
        "example": "📌",
        "exemple": "📌",
        "quote": "🗨️",
        "cite": "🗨️",
    }
    admonition_custom = Path(f"{BASEDIR}/custom_admonition.yml")
    custom={}

    if os.path.exists(admonition_custom):
        with open(admonition_custom, "r", encoding="utf-8") as stream:
            try:
                custom = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                exit(1)

    if type in admonition.keys():
        logo = admonition[type]
        admo_type = type.title()
    elif len(custom) > 0:
        if type in custom.keys():
            logo = custom[type][0]
            admo_type = custom[type][1].title()
    else:
        logo = "🖊️"
        admo_type = type.title()

    if line == "":
        title = "**" + logo + ' <u>' + admo_type + '</u>' + "**{: .title}  \n"
    else:
        title = "**" + logo + " " + line + "**{: .title}  \n"
    return title


def admonition_trad_content(line, type):
    title = line
    if re.search("[*\-\+] ", line):
        title = re.sub("[*\-\+] ", "**•**{: .bullet} ", line)
    elif "collapse:" in line:
        title = ""
    elif "icon:" in line:
        title = ""
    elif "color:" in line:
        title = ""
    elif len(line) == 1:
        title = "$~$  \n"
    elif "title:" in line:
        title = admonition_logo(type, line.replace("title:", "").strip())
    return title


def admonition_trad(file_data):
    code_index = 0
    code_dict = {}
    start_list = []
    end_list = []
    adm_list = [
        "note",
        "seealso",
        "abstract",
        "summary",
        "tldr",
        "info",
        "todo",
        "tip",
        "hint",
        "important",
        "success",
        "check",
        "done",
        "question",
        "help",
        "faq",
        "warning",
        "caution",
        "attention",
        "failure",
        "fail",
        "missing",
        "danger",
        "error",
        "bug",
        "example",
        "exemple",
        "abstract",
        "quote",
        "cite",
    ]

    for i in range(0, len(file_data)):
        if re.search("[`?!]{3}( ?)\w+(.*)", file_data[i]):
            start = i
            start_list.append(start)
        if re.match("^```$", file_data[i]) or re.match("--- admonition", file_data[i]) :
            end = i
            end_list.append(end)
    merged = code_blocks(start_list, end_list)
    for i, j in merged:
        code = {code_index: (i, j)}
        code_index = code_index + 1
        code_dict.update(code)
    offset_for_title = 0
    for ad, ln in code_dict.items():
        ad_start = ln[0] + offset_for_title
        ad_end = ln[1] + offset_for_title
        type = re.search("[`!?]{3}( ?)ad-\w+", file_data[ad_start])
        if type:
            type = re.sub("[`!?]{3}( ?)ad-", "", type.group())
            adm = "b"
            if re.search("[!?]{3} ad-(\w+) (.*)", file_data[ad_start]):
                title = re.search("[!?]{3} ad-(\w+) (.*)", file_data[ad_start])
                adm = "MT"
                title = title.group(2)
            first_block = re.search("ad-(\w+)", file_data[ad_start])
            if first_block:
                file_data[ad_end] = '  \n'
            adm_type_code = first_block.group().replace("ad-", "")
            if adm_type_code not in adm_list:
                first_block = "ad-note"
            else:
                first_block = first_block.group()
            first_block = "  \n!!!" + first_block + "  "

            num_lines = lambda x: x.count("\n")

            file_data[ad_start] = re.sub(
                "[`!?]{3}( ?)ad-(.*)", first_block, file_data[ad_start]
            )


            for i in range(ad_start, ad_end):
                file_data[i] = admonition_trad_content(file_data[i], type)

            if adm == "MT":
                if len(title) > 0:
                    title_admo = admonition_logo(type, title)
                else:
                    title_admo = admonition_logo(type, "")

                file_data.insert(ad_start + 1, title_admo)
                offset_for_title += 1
            else:
                converted = [file_data[i] for i in range(ad_start, ad_end)]
                if not any(re.search(".*title.*", line) for line in converted):
                    title_admo = admonition_logo(type, "")
                    file_data.insert(ad_start + 1, title_admo)
                    offset_for_title += 1
    return file_data
