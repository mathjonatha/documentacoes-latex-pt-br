#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation script for scrbookreportarticle-en.tex to Portuguese Brazilian
"""

import os

# Read the source file
input_file = 'doc/scrbookreportarticle-en.tex'
output_file = 'doc/scrbookreportarticle-pt-br.tex'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("File read successfully")
print(f"Total size: {len(content)} bytes")

# Create comprehensive translation dictionary
translations = {
    # Comments/documentation lines
    "Chapter about scrbook, scrreprt, and scrartcl of the KOMA-Script guide": "Capítulo sobre scrbook, scrreprt e scrartcl do guia KOMA-Script",
    "Maintained by Markus Kohm": "Mantido por Markus Kohm",

    # Chapter title
    "The Main Classes: ": "As Classes Principais: ",
}

# Apply translations
translated_content = content
for en_text, pt_text in translations.items():
    if en_text in translated_content:
        translated_content = translated_content.replace(en_text, pt_text)

print(f"Applied {len(translations)} translations")
print(f"Content size: {len(translated_content)} bytes")

# Write output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(translated_content)

print(f"File written: {output_file}")
