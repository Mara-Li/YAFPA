# Changelog

<!--next-version-placeholder-->

## v3.0.3 (2021-12-27)
### Fix
* A bunch of firewall in case of error ([`bce743b`](https://github.com/Mara-Li/YAFPA/commit/bce743b3a0d4db008f9884fa054db1f7d7c7ea4a))

## v3.0.2 (2021-12-27)
### Fix
* Wrong fix ; real fix now ([`70dbad2`](https://github.com/Mara-Li/YAFPA/commit/70dbad28a262da7b1e71b3c0b73f46257bd6be82))

## v3.0.1 (2021-12-27)
### Fix
* Fix metadata if 'category' don't exist ([`9a940e0`](https://github.com/Mara-Li/YAFPA/commit/9a940e0df64980d80e4342cba126874a66504da6))

## v3.0.0 (2021-12-26)
### Feature
* **metadata:** Change folder working and add a config option for the share key ([`0a3ce81`](https://github.com/Mara-Li/YAFPA/commit/0a3ce81a3d1db6db4eb1d312a528a51947d4ae7c))

### Fix
* **metadata:** Prevent breaking index ([`7f71484`](https://github.com/Mara-Li/YAFPA/commit/7f7148428a9ecf779fb35e939b34771356c43f4e))

### Breaking
* - the 'share' metadata key can be changed in the environnement settings.   - The 'folder' key is now optional : you can configure folder with the 'category' key using "category: Folder/category" ; to configure folder without category : "folder/false" will work.  ([`0a3ce81`](https://github.com/Mara-Li/YAFPA/commit/0a3ce81a3d1db6db4eb1d312a528a51947d4ae7c))

### Documentation
* **readme:** Update docs for the new metadata option ([`a24fab9`](https://github.com/Mara-Li/YAFPA/commit/a24fab958f5063f9a6ca2ab81e58c1adbc1e41ab))
* **readme:** Update docs for the new metadata option ([`01eb78e`](https://github.com/Mara-Li/YAFPA/commit/01eb78e24300503d19a788788c6e868192c7349b))
* **readme:** Update docs for metadata ([`b70a0a3`](https://github.com/Mara-Li/YAFPA/commit/b70a0a30f75460fd76152556fc18e56647d01539))

## v2.5.1 (2021-12-25)
### Fix
* Fix Heading IAL and add IAL line return ([`feb8e20`](https://github.com/Mara-Li/YAFPA/commit/feb8e20d949b0504698b5e9fdf6a7e14fee841b3))

## v2.5.0 (2021-11-26)
### Feature
* :sparkles: mermaid support ([`458ae37`](https://github.com/Mara-Li/YAFPA-python/commit/458ae37550dd039f71392e9494969476f89e9498))

## v2.4.0 (2021-11-19)
### Feature
* Link not exist ([`2386818`](https://github.com/Mara-Li/YAFPA-python/commit/23868183261506bf2119c2cfa4db87bc867087ed))

## v2.3.5 (2021-11-18)
### Fix
* Fix link heading generation ([`40ed7ce`](https://github.com/Mara-Li/YAFPA-python/commit/40ed7ceb642525eab4baa3ce0680237823a73f7f))
* Hashtag in linked header ([`071ac60`](https://github.com/Mara-Li/YAFPA-python/commit/071ac608777f5df17dfe3e1391bf1949ad653087))

## v2.3.4 (2021-11-18)
### Fix
* Fix link generation ([`53d8d84`](https://github.com/Mara-Li/YAFPA-python/commit/53d8d84504c79c49a79a563bc3a99a18355f12fb))

### Performance
* Add skip comment ([`03afbdb`](https://github.com/Mara-Li/YAFPA-python/commit/03afbdbe50cf91c4ceaa8302c775f35502f822b1))
## v2.3.3 (2021-11-15)
### Fix
* :bug: Fix # conversion in links. ([`5ab5059`](https://github.com/Mara-Li/YAFPA-python/commit/5ab50596a50d865bc990fa22de172d5acd129de9))

## v2.3.2 (2021-11-15)


## v2.3.1 (2021-11-14)
### Fix
* Little fix for clipboard in convert all ([`e9fc266`](https://github.com/Mara-Li/YAFPA-python/commit/e9fc266f7ac5f1ae6b35624a6d426b140d181e35))

## v2.3.0 (2021-11-14)
### Feature
* Exclude folder ([`b319bbe`](https://github.com/Mara-Li/YAFPA-python/commit/b319bbe6725d41683902359cf6a2484cea190b09))
* Move admonition ([`96a4bf3`](https://github.com/Mara-Li/YAFPA-python/commit/96a4bf34e607a6105e49570671a43d20e83537de))

### Breaking
* Move admonition ([`96a4bf3`](https://github.com/Mara-Li/YAFPA-python/commit/96a4bf34e607a6105e49570671a43d20e83537de))

## v2.2.0 (2021-11-11)
### Fix
* Fix date ([`c93c1de`](https://github.com/Mara-Li/YAFPA-python/commit/c93c1de83035f97664ffbd7920eca4ae7244acb1))

## v2.1.0 (2021-11-11)


## v2.0.2 (2021-11-11)
### Fix
* Don't update date if there is a date key ([`b6b6307`](https://github.com/Mara-Li/YAFPA-python/commit/b6b63078db29f941b653dcfeeda21a0f1dafaf19))

### Breaking
* Don't update date if there is a date key ([`b6b6307`](https://github.com/Mara-Li/YAFPA-python/commit/b6b63078db29f941b653dcfeeda21a0f1dafaf19))

## v2.0.1 (2021-11-11)
### Fix
* Fix admonition and code blocks ([`e29fee1`](https://github.com/Mara-Li/YAFPA-python/commit/e29fee1bba2bbfb5f3c4ae8fde640f27aec1e9d0))

## v2.0.0 (2021-11-11)


## v1.56.0 (2021-11-09)
### Feature
* Update emoji admonition ([`571fc85`](https://github.com/Mara-Li/YAFPA-python/commit/571fc858d2161b0f3cfc79fbe3ee9840f97e53b8))

## v1.55.1 (2021-11-08)
### Feature
* Added a way to have custom admonition ! ([`1c71bcd`](https://github.com/Mara-Li/YAFPA-python/commit/1c71bcdd2933c2c7fcf5c9ad088011068be4db44))
* **admonition:** Added a way to have custom admonition ! ([`b9884fd`](https://github.com/Mara-Li/YAFPA-python/commit/b9884fd5ca6209b2bd9819d6e71dabc692491b56))

## v1.55.0 (2021-11-08)


## v1.54.6 (2021-11-08)
### Fix
* **admonition:** Fix admonition and adjust list style. ([`ae83a60`](https://github.com/Mara-Li/YAFPA-python/commit/ae83a600a5bbf7c49d4982462e578e34ebffc4bf))

## v1.54.5 (2021-11-07)


## v1.54.4 (2021-11-06)
### Fix
* :bug: Add a patch for expanduser and runtimeError ([`950086b`](https://github.com/Mara-Li/YAFPA-python/commit/950086b9cbff62562da73d3f6edc426801d11ae2))

## v1.54.3 (2021-11-06)
### Fix
* :bug: Emergency fix for image transform ([`9e39417`](https://github.com/Mara-Li/YAFPA-python/commit/9e39417ac4874a2db78138aa7494ec24f570b0ef))

## v1.54.2 (2021-11-06)


## v1.54.1 (2021-10-30)
### Fix
* Added unidecode in file checking for deletion ([`39e5562`](https://github.com/Mara-Li/YAFPA-python/commit/39e556281b55befb4d3148eccb3db858965b0236))

## v1.54.0 (2021-10-29)


## v1.53.0 (2021-10-29)
### Feature
* :arrow_up: Add unidecode in dependency ([`1c3a569`](https://github.com/Mara-Li/YAFPA-python/commit/1c3a56955294b02ea5263741e20d8674b46ad43f))
* Remove whitespace ([`6d69c63`](https://github.com/Mara-Li/YAFPA-python/commit/6d69c638c99283cb8b4f716cf60f7fb925fa3c8c))
* Update requirements ([`a64526d`](https://github.com/Mara-Li/YAFPA-python/commit/a64526dfd70bab76a361db9632383fe322d4e401))

### Fix
* Repear import ([`e639942`](https://github.com/Mara-Li/YAFPA-python/commit/e63994234cb6cd89847a76e2c5b3baf5bc578cae))
* Repear bug on mobile ([`e2c0019`](https://github.com/Mara-Li/YAFPA-python/commit/e2c0019de3211180654d435a68e58003e7820fb2))

## v1.52.7 (2021-10-29)
### Fix
* 🔧 Now, config file are in site package. ([`f90689a`](https://github.com/Mara-Li/YAFPA-python/commit/f90689abd851868713f6ac1fb0d8208d5e01cb7b))

## v1.52.6 (2021-10-27)
### Feature
* :art: Black formating ([`12866cf`](https://github.com/Mara-Li/YAFPA-python/commit/12866cf1a6413d7686d4006c9d2ed840e4389722))
* :see_no_evil: Update gitignore ([`8fd94eb`](https://github.com/Mara-Li/YAFPA-python/commit/8fd94eb7c1a34d724b166574912298a372659699))

### Fix
* :bug: Fix convert links for normal links (jekyll liquid) ([`6be2402`](https://github.com/Mara-Li/YAFPA-python/commit/6be240269bb7e6a925f012f94b097ee614827665))

## v1.52.5 (2021-10-27)
### Fix
* :bug: Remove print message ([`4fa4b3f`](https://github.com/Mara-Li/YAFPA-python/commit/4fa4b3ff8fadd5cb12c28f1a65bcb22659343881))

## v1.52.4 (2021-10-27)
### Fix
* :bug: fix problem with image link on one line ([`ebf1bb3`](https://github.com/Mara-Li/YAFPA-python/commit/ebf1bb383b6967ba1d71e8016c978ffdd63f0398))

## v1.52.3 (2021-10-27)
### Fix
* Fix flag ([`97f98da`](https://github.com/Mara-Li/YAFPA-python/commit/97f98dac8c931453b8268915072f653e3204407b))

## v1.52.2 (2021-10-26)
### Fix
* :ambulance: Fix parsing bug with Jekyll with link (convert https link to markdown normal links) ([`db59c47`](https://github.com/Mara-Li/YAFPA-python/commit/db59c47e2bfc5b601264a0de013a29aebdd5c7ab))

## v1.52.1 (2021-10-26)
### Feature
* **gitignore:** :see_no_evil: Update gitignore ([`b652ae3`](https://github.com/Mara-Li/YAFPA-python/commit/b652ae3796ce3ea2fcdee6ce28341ca95a93d5b0))
* Change the way date are saved ([`e18420a`](https://github.com/Mara-Li/YAFPA-python/commit/e18420aac415f54ec5987d2a83824609caabe92b))

### Fix
* :ambulance: Repear bug because of filepath ([`03f36a4`](https://github.com/Mara-Li/YAFPA-python/commit/03f36a47ef11914a280d0f1b3feda44ca4927be0))

