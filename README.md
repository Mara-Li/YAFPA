⚠️THIS SCRIPT IS NO LONGER MAINTENED. PLEASE [READ MORE ON OBSIDIAN FORUM](https://forum.obsidian.md/t/yet-another-free-publish-alternative-yafpa/23608/19?u=mara-li)

[PLEASE CHECK THE NEW VERSION BASED ON MKDOCS](https://pypi.org/project/obs2mk/)


[![GitHub license](https://img.shields.io/github/license/Mara-Li/YAFPA-python)](https://github.com/Mara-Li/YAFPA-python)
[![PyPI](https://img.shields.io/pypi/v/YAFPA)](https://pypi.org/project/yafpa/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/YAFPA)
![PyPI - Status](https://img.shields.io/pypi/status/YAFPA)
![](https://img.shields.io/badge/Auxiliary%20Tool-Obsidian-blueviolet)
[![Yet Another Publish Alternative](https://img.shields.io/badge/Github-YAFPA-success)](https://github.com/Mara-Li/yet-another-free-publish-alternative)

**This script is intended to be used with [YAFPA](https://github.com/Mara-Li/yet-another-free-publish-alternative), a free way to share your obsidian vault**.

*⚠️ The script and site are not a replacement for [Obsidian Publish](https://obsidian.md/publish), which is a much more efficient way to share Obsidian files.*

# Get Started

- You first need to create a template using [YAFPA-blog](https://github.com/Mara-Li/yet-another-free-publish-alternative)
- After, do `pip install YAFPA`

The first time you use the script, it will ask you three things :
- Your vault path (absolute path !)
- The path of the blog (absolute too !)
- The link of your blog, as `https://my-awesome-blog.netlify.app/`

You can reconfigure the path with `yafpa --config`

The file will be created in your site_package folder. 

# Script
usage: yafpa [-h] [--preserve | --update] [--filepath FILEPATH] [--git] [--keep] [--config]

Create file in folder, move image in assets, convert to relative path, add share support, and push to git

optional arguments:
  - `-h, --help`: show this help message and exit
  - `--preserve, --p, --P` : Don't delete file if already exist
  - `--update, --u, --U` : force update : delete all file and reform.
  - `--filepath FILEPATH, --f FILEPATH, --F FILEPATH `: Filepath of the file you want to convert
  - `--git, --g, --G` : No commit and no push to git
  - `--keep, --k` : Keep deleted file from vault and removed shared file
  - `--config, --c` : Edit the config file


## Checking differences
The script will convert all file with `share:true` and check if the contents 
are different to the versions in `_notes`. The only things that are 
ignored is the contents of the metadata. If you want absolutely change the 
metadata you can:
- Use `yafpa --file <filepath>` directly
- Use `--u` to force update all file 
- Continue to work on the file before pushing it.
- Add a newline
- Manually delete the file 
- Add or edit the metadata keys (unless `date`/`title`/`created`/`update`/`link`).

⚠️ As always with git, you can repost the exact same file that already exists on the server. 

## Limitations

⚠️ In case you have two files with the same name but :
- In different folder
- With different sharing status or folder
The script will bug because **The folder is not checked** (It's not required). In this unique case, you need to rename one of the files. 

- In the same way, in case you change the folder key in the metadata, you will have two identic file in different folder. 

## Options
### Share all
`yafpa` and all `yafpa` option without `--F FILEPATH` will automatically read all file in your vault to check the `share: true` key in metadata (frontmatter YAML).

By default, the script will check the difference between line [(*cf checking difference*)](README.md#checking-differences), and convert only the file with difference. You can use `--u` to force update. 

### Share only a file
The command will be : `yafpa --F filepath`

The file to be shared does not need to contain `share: true` in its YAML, and will be updated no matter what.

## How it works

The script : 
- Moves file (with `share: true` frontmatter or specific file) in the `_notes` folder
- Moves image in `assets/img` and convert (with alt support)
- Converts highlight (`==mark==` to `[[mark::highlight]]`)
- Converts "normal" writing to GFM markdown (adding `  \n` each `\n`)
- Supports non existent file (adding a css for that 😉)
- Supports image flags css (Lithou snippet 🙏)
- Support normal and external files (convert "normal markdown link" to 
  "wikilinks")
- Edit link to support transluction (if not `embed: False`)
- Remove block id (no support)
- Add CSS settings for inline tags (no link support) ; Tags are : class = .hash ; id = #tag_name (so you can style each tags you use)
- Frontmatter :  Update the date if there is no date in frontmatter
- Frontmatter : In absence of title, add the file's title.
- Copy the link to your clipboard if one file is edited.
- ⭐ Admonition conversion to "callout inspired notion"
- Update the frontmatter in the original file, adding the link and change `share` to true if one file is shared.

Finally, the plugin will add, commit and push if supported.

Note : The clipboard may not work in your configuration. I have (and can) only test the script on IOS and Windows, so I use `pyperclip` and `pasteboard` to do that. If you are on MacOS, Linux, Android, please, check your configuration on your python and open an issue if it doesn't work. 
Note : I **can't** test on these 3 OSes, so I can't create a clipboard option on my own. 

### Custom CSS 
You can add CSS using the file [custom.css](https://github.com/Mara-Li/yet-another-free-publish-alternative/blob/master/assets/css/custom.css). The plugin [Markdown Attribute](https://github.com/valentine195/obsidian-markdown-attributes) allow to use the creation of inline css. 
Some information about this :
- You need to add `:` after the first `{`
- The inline IAL work only if there is stylized markdown. In absence, the text will be bolded. 
- It won't work with highlight (removed automatically by the script)
 
⚠️ As I use CodeMirror Options and Contextual Typography, I warn you : the use of `#tags` to stylize the text before it doesn't work with my build. So, as an option to don't have a random tag in a text, you can use `custom.css` to remove it with `display: none` (you can have an example with `#left`). 


### Frontmatter settings
- `share: true` : Share the file
- `embed: false` : remove the transluction (convert to normal wikilinks)
- `update: false` : Don't update the file at all after the first push
- `folder` : Use a different folder than `_note` ([here some more information](https://github.com/Mara-Li/yet-another-free-publish-alternative#folder-options))
Alternatively, you can use the `category` key : `category: folder/category`
    - `folder` is optional ; as default : `_notes`
    -  `category` can be `false` to prevent apparence in the feed
NB : if `category` and `folder` is used at the same time, `folder` will be used as the folder. 

### Admonition 
As admonition is very tricky, I choose to convert all admonition to a "callout Notion".
The script will : 
- Remove codeblock for admonition codeblocks
- Convert ` ```ad-``` ` to ```!!!ad-```
- Bold title and add a IAL `{: .title}`

JavaScript will make all things nice.

⚠️ As always with markdown, you will see some problem with new paragraph inside admonition. You can use `$~$` to fake line. The script will automatically add this.
Also, you can add emoji on title to add some nice formatting.

#### Custom Admonition
You can now use custom admonition using the file [custom_admonition.yml](https://github.com/Mara-Li/yet-another-free-publish-alternative/blob/master/custom_admonition.yml). The file is formated as a YAML :
```yml
admonition_type: #In obsidian
  - logo #emoji
  - admonition title: #the name you want in the website 
```
- Admonition name correspond to `admonition type` in the admonition plugin.
- Admonition title correspond to `admonition title` you use in the admonition plugin.

You need to create multiple key and value for each different synonyme you use (as in admonition...)

### IOS Shortcuts

You need to found the path of your vault and the blog in your phone. To achieve that, I use [a-shell](https://holzschu.github.io/a-Shell_iOS/). 

First, in a-shell, run `pickFolder` and choose the folder of your vault, and rerun `pickFolder` to choose the folder where are the blog data (you need to clone with [Working Copy](https://workingcopyapp.com/))
After, do `showmarks` and copy the two path in any note app. Check if the path is not broken because of the paste!
You can also do :
```bash
cd 
showmarks > bookmark
vim bookmark
```

Here is a blank sheet to help you if you want to manually write / edit it :
```
vault=
blog_path=
blog=
share=
```
With :
- `vault`: Vault Absolute Path
- `blog_path` : Blog repository absolute path
- `blog` : Blog link
- `share` : your wanted share key ; by default : `share`

To use the [shortcuts](https://routinehub.co/shortcut/10151/), you need :
- [a-shell](https://holzschu.github.io/a-Shell_iOS/) (Free)
- [Working Copy](https://workingcopyapp.com/)

Before running the shortcuts, you need to install all requirements, aka :
```
pip install yafpa
yafpa --C
```

Links : 
- [Share All File](https://routinehub.co/shortcut/10151/)
- [Share One File](https://routinehub.co/shortcut/10475/)

For the moment I can't create a shortcut to share only one file, BUT! You can use `a-shell` as you do in a normal terminal, aka : 
```
jump <vault>
yafpa --f <file>
```

To run the script for all your file, run `yafpa`.

Note : Compared to pyto, the script cannot work with `$HOME`, so the `.YAFPA-env` will be created in the folder you use to run it. It is also possible to use multiple folder, but you need to create the file for each. The better is to have one in the vault ; and one in the default folder of a-shell. 


### Obsidian 
→ Please use Wikilinks with "short links" (I BEG YOU)
You can integrate the script within obsidian using the nice plugin [Obsidian ShellCommands](https://github.com/Taitava/obsidian-shellcommands).

You could create two commands :
1. `share all` : `yafpa`
2. `share one` : `yafpa --f {{file_path:absolute}}`

You can use :
- [Customizable Sidebar](https://github.com/phibr0/obsidian-customizable-sidebar)
- [Obsidian Customizable Menu](https://github.com/kzhovn/obsidian-customizable-menu)
To have a button to share your file directly in Obsidian !

#### Template frontmatter
→ The • indicate that this value is optional
```yaml
title: My files•
date: 12-11-2021•
embed: true•
update: true•
current: true•
flux: true•
share: false (this key can be changed in the configuration)
category: folder/category (category can be false)
description: my awesome file
```
You can use MetaEdit / Supercharged links to quickly update the front matter. 

## Exemple of frontmatter :
```yml
category: Roleplay/Application
date: 21-12-2021
share: true
tag: RP/Darkness-Haunted/Application/PC
title: (Darkness Haunted) Alwyn Kallendris
```
The file will be added in the `Roleplay` folder ; and the `Application` will now show the file in the sidebar, the Roleplay page and the collections page. 
