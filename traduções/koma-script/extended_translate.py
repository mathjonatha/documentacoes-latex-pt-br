#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extended translation script for scrbookreportarticle-en.tex
Translates additional sections to Portuguese Brazilian
"""

import os

input_file = 'doc/scrbookreportarticle-pt-br.tex'
output_file = 'doc/scrbookreportarticle-pt-br.tex'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("Starting extended translation...")
print(f"File size before: {len(content)} bytes")

# Additional translations for sections not yet covered
additional_translations = [
    # Comments in LoadCommonFile lines
    ("Early or Late Selection of Options", "Selecao Antecipada ou Tardia de Opcoes"),
    ("Compatibility with Earlier Versions of KOMA-Script", "Compatibilidade com Versoes Anteriores do KOMA-Script"),
    ("Draft Mode", "Modo Rascunho"),
    ("Page Layout", "Layout da Pagina"),
    ("Choosing the Document Font Size", "Escolhendo o Tamanho da Fonte do Documento"),
    ("Text Markup", "Marcacao de Texto"),
    ("Document Titles", "Titulos do Documento"),

    # Abstract section
    ("Abstract", "Resumo"),
    ("Particularly with articles, more rarely with reports, there is an abstract, or\nsummary, directly beneath the title and before the table of contents. When\nusing an in-page title, this abstract is normally a kind of left- and\nright-indented block. In comparison, the abstract appears as a chapter or\nsection when using title pages.",
     "Particularmente com artigos, mais raramente com relatorios, ha um resumo ou\nsumarito, diretamente abaixo do titulo e antes da tabela de conteudos. Ao\nusar um titulo na pagina, este resumo eh normalmente um tipo de bloco\nrecuado a esquerda e a direita. Em comparacao, o resumo aparece como um\ncapitulo ou secao ao usar paginas de titulo."),

    # Simple words/phrases
    ("In two-sided documents especially, it is preferable to have the same visual\nbaseline not only for the first lines of each text area in a two-page spread\nbut also for the last lines. If a page consists only of text without\nparagraphs or headings, this is generally the result. But a paragraph\nspacing of half a line would be enough to prevent you from achieving this\ngoal if the number of paragraphs on each page of the two-page spread differs\nby an odd number. In this case, at least some of the paragraph distances\nneed to be stretched or shrunk to reach the target again.",
     "Em documentos de dois lados especialmente, eh preferivel ter a mesma\nlinha de base visual nao apenas para as primeiras linhas de cada area de texto\nem uma pagina dupla, mas tambem para as ultimas linhas. Se uma pagina\nconsiste apenas em texto sem paragrafos ou titulos, esse eh geralmente o\nresultado. Mas um espacamento de paragrafo de meia linha seria suficiente\npara impedir que voce atingisse esse objetivo se o numero de paragrafos em\ncada pagina da pagina dupla diferir por um numero impar. Neste caso, pelo\nmenos alguns dos espacamentos de paragrafo precisam ser esticados ou\nencolhidos para atingir o objetivo novamente."),

    ("You can also explicitly request vertical adjustment at any time starting with\nthe current page by using",
     "Voce tambem pode solicitar explicitamente o ajuste vertical a qualquer momento comecando com\na pagina atual usando"),

    ("has the\nopposite effect, switching off vertical adjustment starting with the current\npage. This corresponds to the default for one-sided printing.",
     "tem o\nefeito oposto, desligando o ajuste vertical comecando com a pagina\natual. Isso corresponde ao padrao para impressao unilateral."),

    ("By the way, ", "Aliás, "),

    ("uses a slightly modified method for adjusting the\nvertical skip. This has been done to move footnotes to the bottom of the\ntext area instead of having them close to the last text line used.",
     "usa um metodo ligeiramente modificado para ajustar o\nspacamento vertical. Isso foi feito para mover as notas de rodape para o\nfundo da area de texto em vez de tê-las perto da ultima linha de texto usada."),

    ("Books typically use a different kind of summary. There, you usually place an\nappropriate chapter at the beginning or the end of the work. This chapter is\noften combined with either the introduction or a description of a larger\nprospectus. Therefore, the",
     "Livros normalmente usam um tipo diferente de resumo. Lá, voce geralmente coloca um\ncapitulo apropriado no inicio ou no final da obra. Este capitulo eh\nfrequentemente combinado com a introducao ou uma descricao de um\nprospecto maior. Portanto, o"),

    ("class has no\n", "classe nao tem\n"),

    ("environment.", "ambiente."),

    ("summary\nchapter is also recommended for reports in a wider sense, such as a Master's\nthesis or Ph.D. dissertation.", "resumo\no capitulo tambem eh recomendado para relatorios em um sentido mais amplo, como uma\ntese de Mestrado ou dissertacao de Doutorado."),
]

# Apply translations in order (longer ones first)
sorted_translations = sorted(additional_translations, key=lambda x: len(x[0]), reverse=True)

translated_content = content
count = 0
for en_text, pt_text in sorted_translations:
    if en_text in translated_content:
        translated_content = translated_content.replace(en_text, pt_text)
        count += 1
        print(f"[{count}] Translated: {en_text[:50]}...")

print(f"\nTotal new translations applied: {count}")
print(f"File size after: {len(translated_content)} bytes")

# Write output
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(translated_content)

print(f"Translation complete!")
