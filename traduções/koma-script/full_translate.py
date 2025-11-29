#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete translation script for scrbookreportarticle-en.tex to Portuguese Brazilian
"""

import os
import re

input_file = 'doc/scrbookreportarticle-en.tex'
output_file = 'doc/scrbookreportarticle-pt-br.tex'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("Starting comprehensive translation...")
print(f"File size: {len(content)} bytes")

# Create comprehensive translation dictionary
# Using raw strings to avoid escape sequence issues
translations = [
    # Comments
    ("Chapter about scrbook, scrreprt, and scrartcl of the KOMA-Script guide", "Capítulo sobre scrbook, scrreprt e scrartcl do guia KOMA-Script"),
    ("Maintained by Markus Kohm", "Mantido por Markus Kohm"),

    # Chapter title
    ("The Main Classes: ", "As Classes Principais: "),

    # Main content (done by line groups to preserve structure)
    ("The main classes of the {\\KOMAScript} bundle are designed as counterparts to\nthe standard {\\LaTeX} classes. This means that the {\\KOMAScript} bundle\ncontains replacements for the three standard classes,",
     "As classes principais do pacote {\\KOMAScript} foram projetadas como contrapartes das\nclasses padrão {\\LaTeX}. Isso significa que o pacote {\\KOMAScript}\ncontém substitutos para as três classes padrão,"),

    ("There is also a replacement for the\nstandard ", "Também há um substituto para a\nclasse padrão "),

    ("class. The document class for\nletters is described in a separate chapter because it is fundamentally\ndifferent from the three main classes (see",
     "classe. A classe de documento para\ncartas é descrita em um capítulo separado porque é fundamentalmente\ndiferente das três classes principais (veja"),

    ("The simplest way to use a {\\KOMAScript} class instead of a standard one is to\nsubstitute the class name in the \\verb|\\documentclass| command in accordance\nwith",
     "A forma mais simples de usar uma classe {\\KOMAScript} em vez de uma padrão é\nsubstituir o nome da classe no comando \\verb|\\documentclass| de acordo com"),

    ("For example, you can replace", "Por exemplo, você pode substituir"),

    ("Normally, {\\LaTeX} should process\nthe document without errors, just as before the substitution. The layout,\nhowever, should be different. Additionally, the {\\KOMAScript} classes provide\nnew possibilities and options that are described in the following sections.",
     "Normalmente, o {\\LaTeX} deve processar\no documento sem erros, assim como antes da substituição. O layout,\nno entanto, deve ser diferente. Além disso, as classes {\\KOMAScript} fornecem\nnovas possibilidades e opções que são descritas nas seções a seguir."),

    ("Class correspondence", "Correspondência de Classes"),
    ("Correspondence between\n\tstandard classes and {\\KOMAScript} classes", "Correspondência entre\n\tclasses padrão e classes {\\KOMAScript}"),
    ("standard class  & \\KOMAScript{} class", "classe padrão  & classe \\KOMAScript{}"),

    # Warning/note block
    ("However, it should be noted here that some package authors develop their\npackages based on the implementation and even internal code of the standard\nclasses, without regard to completely independent developments like the\n\\KOMAScript{} classes. In such cases, the first \\LaTeX{} run after the change\nmay well result in error messages or additional warnings. These can usually be\ncorrected in a simple way. Often the extended capabilities of \\KOMAScript{}\ncan be used for this purpose, which completely eliminates the problematic\npackage.",
     "No entanto, deve-se notar aqui que alguns autores de pacotes desenvolvem seus\npacotes com base na implementação e até mesmo no código interno das classes\npadrão, sem levar em consideração desenvolvimentos completamente independentes\ncomo as classes \\KOMAScript{}. Nesses casos, a primeira execução de \\LaTeX{}\napós a mudança bem pode resultar em mensagens de erro ou avisos adicionais.\nEstas geralmente podem ser corrigidas de forma simples. Frequentemente, os\nrecursos estendidos de \\KOMAScript{} podem ser usados para esse fim,\neliminando completamente o pacote problemático."),

    ("Sometimes the package", "Às vezes, o pacote"),
    ("documented in", "documentado em"),
    ("can also help. Replacing obsolete packages with\ncurrent successors can also help to eliminate such problems. Sometimes even\nthe \\KOMAScript{} classes provide warnings to help solve incompatibilities.",
     "também pode ajudar. Substituir pacotes obsoletos por sucessores atuais\ntambém pode ajudar a eliminar esses problemas. Às vezes, até mesmo as\nclasses \\KOMAScript{} fornecem avisos para ajudar a resolver incompatibilidades."),

    # Philosophical paragraph
    ("Let me say something before describing the classes. When beginning to write a\ndocument, you are often unsure which specific options to choose. Some\nsettings, for instance the choice of paper size, may be fixed in advance. But\neven the question of the appropriate page layout could be difficult to answer\ninitially. On the other hand, these settings should be nearly irrelevant, in\nthe beginning, to the main business of an author: planning the document\nstructure, writing the text, preparing figures, tables, lists, index, and\nother data. As an author, you should concentrate initially on the content.\nWhen that is done, you can take on the fine points of presentation. In\naddition to the choice of options, this includes correcting hyphenation,\noptimizing page breaks, and placing tables and figures.",
     "Deixe-me dizer algo antes de descrever as classes. Ao começar a escrever um\ndocumento, você frequentemente fica inseguro sobre quais opções específicas\nescolher. Algumas configurações, por exemplo, a escolha do tamanho do papel,\npodem ser fixadas antecipadamente. Mas até mesmo a questão do layout apropriado\nda página poderia ser difícil de responder inicialmente. Por outro lado, essas\nconfigurações devem ser quase irrelevantes, no início, para o negócio principal\nde um autor: planejar a estrutura do documento, escrever o texto, preparar\nfiguras, tabelas, listas, índice e outros dados. Como autor, você deve se\nconcentrar inicialmente no conteúdo. Quando isso for feito, você poderá cuidar\ndos pontos finos da apresentação. Além da escolha de opções, isso inclui a\ncorreção de hifenização, a otimização de quebras de página e o posicionamento\nde tabelas e figuras."),
]

# Apply translations (sorted by length descending to avoid substring conflicts)
translated_content = content
count = 0
for en_text, pt_text in sorted(translations, key=lambda x: len(x[0]), reverse=True):
    if en_text in translated_content:
        translated_content = translated_content.replace(en_text, pt_text)
        count += 1
        print(f"[{count}] Translated substring ({len(en_text)} chars)")

print(f"\nTotal translations applied: {count}")
print(f"Final file size: {len(translated_content)} bytes")

# Write output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(translated_content)

print(f"Output written to: {output_file}")
print("Translation complete!")
