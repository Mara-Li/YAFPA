import re


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
        "quote": "📋",
        "cite": "📋",
        }
    if type in admonition.keys():
        logo = admonition[type]
    else:
        logo = "🖊️ [" + type.title() + "]"
    if line == "":
        title = "**" + logo + "**{: .title}  \n"
    else:
        title = "**" + logo + " " + line + "**{: .title}  \n"
    return title


def admonition_trad_content(line, type):
    title = line
    if re.search('[*\-\+] ', line):
        title = re.sub('[*\-\+] ', '**•**{: .bullet} ', line)
    if "collapse:" in line:
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
    adm_list = ['note', 'seealso', 'abstract', 'summary', 'tldr', 'info',
           'todo', 'tip',
           'hint', 'important', 'success', 'check', 'done', 'question',
           'help', 'faq', 'warning',
           'caution', 'attention', 'failure', 'fail', 'missing', 'danger',
           'error', 'bug', 'example', 'exemple', "abstract",
           'quote', 'cite'
           ]
    for i in range(0, len(file_data)):
        if re.search("[`?!]{3}( ?)ad-(.*)", file_data[i]):
            start = i
            start_list.append(start)
        elif re.match("```", file_data[i]) or re.match("--- admonition", file_data[i]):
            end = i
            end_list.append(end)
    for i, j in zip(start_list, end_list):
        code = {
            code_index: (i, j)}
        code_index = code_index + 1
        code_dict.update(code)

    offset_for_title = 0
    for ad, ln in code_dict.items():
        ad_start = ln[0] + offset_for_title
        ad_end = ln[1] + offset_for_title
        type = re.search("[`!?]{3}( ?)ad-\w+", file_data[ad_start])
        type = re.sub("[`!?]{3}( ?)ad-", "", type.group())
        adm = "b"
        title = ""
        if re.search("[!?]{3} ad-(\w+) (.*)", file_data[ad_start]):
            title = re.search("[!?]{3} ad-(\w+) (.*)", file_data[ad_start])
            adm = "MT"
            title = title.group(2)
        first_block = re.search("ad-(\w+)", file_data[ad_start])
        adm_type_code = first_block.group().replace('ad-', '')
        if adm_type_code not in adm_list:
            first_block = "ad-note"
        else:
            first_block = first_block.group()
        first_block = "  \n!!!" + first_block + "  "

        num_lines = lambda x: x.count('\n')

        file_data[ad_start] = re.sub(
            "[`!?]{3}( ?)ad-(.*)", first_block, file_data[ad_start]
            )

        file_data[ad_end] = "  \n"
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
