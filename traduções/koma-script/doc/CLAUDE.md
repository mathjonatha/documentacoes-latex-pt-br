# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the documentation directory (`doc/`) for the KOMA-Script bundle, a comprehensive LaTeX2e document class and package system. KOMA-Script is a replacement for the standard LaTeX classes (article, book, report, letter) with extensive customization capabilities.

This directory contains the English (`-en`) versions of the documentation source files. The complete KOMA-Script guide is assembled from modular `.tex` files and compiled into a single comprehensive PDF (`scrguide-en.pdf`).

## Building the Documentation

The main documentation file is `scrguide-en.tex`, which uses the custom `scrguide` document class and includes `scrguide-body.tex`.

### Building with LaTeX

```bash
# IMPORTANT: First, generate the letter example files from the dtx
latex scrlttr2-examples.dtx

# Build the complete guide (from the doc directory)
pdflatex scrguide-en.tex
makeindex -s scrguide.ist scrguide-en.idx
makeindex -s scrguide.gst -o scrguide-en.gls scrguide-en.glo
bibtex scrguide-en
pdflatex scrguide-en.tex
pdflatex scrguide-en.tex
# Run additional passes if you see warnings about changed labels
pdflatex scrguide-en.tex
```

### Building with development LaTeX (for testing)

```bash
pdflatex-dev scrguide-en.tex
# (same sequence of commands as above)
```

According to CONTRIBUTING.md, testing with `pdflatex-dev`, `lualatex-dev`, or `xelatex-dev` is recommended for pre-release testing.

### Installation (from parent directory)

From the parent `koma-script/` directory:
```bash
# Install development version without manual
l3build install

# Install with manual
l3build install --full

# Install to specific TEXMF tree (required for MiKTeX)
l3build install --texmfhome <TEXMF-ROOT>

# Uninstall
l3build uninstall
```

## Documentation Architecture

The documentation is highly modular, organized by topic and component:

### Main Structure Files
- `scrguide-en.tex` - Main document that sets language to English
- `scrguide-body.tex` - Document body that includes all component files
- `scrguide.cls` - Custom document class for the guide itself
- `scrguide.bib` - Bibliography database
- `scrguide.ist` / `scrguide.gst` - Index and glossary styles

### Document Parts
- `preface-en.tex` - Preface
- `introduction-en.tex` - Introduction and preliminary information
- `authorpart-en.tex` - Author part
- `expertpart-en.tex` - Expert part
- `terms-en.tex` - Terminology definitions

### Component Documentation Files

**Core Classes:**
- `scrbookreportarticle-en.tex` - Documentation for scrbook, scrreprt, scrartcl classes
- `scrbookreportarticle-experts-en.tex` - Expert-level documentation for these classes
- `scrlttr2-en.tex` - Letter class documentation
- `scrlttr2-experts-en.tex` - Expert-level letter class documentation

**Packages:**
- `scrbase-en.tex` - Basic features package (key=value, conditionals)
- `scrextend-en.tex` - KOMA-Script features for non-KOMA classes
- `typearea-en.tex` - Page layout and type area calculation
- `typearea-experts-en.tex` - Expert-level type area documentation
- `scrlayer-en.tex` - Layer management for page styles
- `scrlayer-scrpage-en.tex` - Page style customization
- `scrlayer-scrpage-experts-en.tex` - Expert page style documentation
- `scrlayer-notecolumn-en.tex` - Note column functionality
- `tocbasic-en.tex` - Table of contents management
- `scrlfile-en.tex` - File loading manipulation
- `scraddr-en.tex` - Address file handling
- `scrdate-en.tex` - Date formatting
- `scrtime-en.tex` - Time formatting
- `scrlogo-en.tex` - KOMA-Script logo
- `scrjura-en.tex` - Legal document support
- `scrwfile-en.tex` - Write file handling

**Special Topics:**
- `japanlco-en.tex` - Japanese letter class options

### Common Features Documentation

Files prefixed with `common-` document features shared across multiple KOMA-Script classes:

- `common-compatibility-en.tex` - Compatibility with standard classes
- `common-dictum-en.tex` - Smart sayings/epigraphs
- `common-draftmode-en.tex` - Draft mode functionality
- `common-fontsize-en.tex` - Font size options
- `common-footnotes-en.tex` - Footnote customization
- `common-footnotes-experts-en.tex` - Expert footnote features
- `common-headfootheight-en.tex` - Header and footer height
- `common-interleafpage-en.tex` - Interleaf pages
- `common-lists-en.tex` - List customization
- `common-marginpar-en.tex` - Margin notes
- `common-oddorevenpage-en.tex` - Odd/even page detection
- `common-options-en.tex` - Option handling
- `common-pagestylemanipulation-en.tex` - Page style manipulation
- `common-parmarkup-en.tex` - Paragraph markup
- `common-textmarkup-en.tex` - Text markup and emphasis
- `common-titles-en.tex` - Title page customization
- `common-typearea-en.tex` - Type area basics

### Supporting Files

- `linkalias.tex` - Link aliasing for cross-references
- `plength-tikz.tex` - TikZ-based pseudo-length visualization
- `variables-tikz.tex` - TikZ-based variable visualization
- `book-remarkbox-*.tex` - Example files for remark boxes

### Generated Files

- `scrguide-en.pdf` - The compiled comprehensive guide (2.9 MB PDF)
- `letter-example-*.pdf` - Letter class examples (numbered 00-23)
- `scrlayer-notecolumn-example-en.pdf` - Note column example
- Various `.html` files - Component reference pages

## File Naming Conventions

- `-en.tex` suffix: English version of documentation files
- `common-*.tex`: Features shared across multiple KOMA-Script classes
- `*-experts-en.tex`: Advanced/expert-level documentation
- `*-example-*.tex/pdf`: Example documents demonstrating features

## Key Characteristics

### License
All documentation files are under LPPL 1.3c (LaTeX Project Public License), maintained by Markus Kohm.

### Language Support
This directory contains only English documentation. German versions exist elsewhere with `-de` suffix.

### Documentation Style
The documentation uses extensive cross-referencing, examples, and is structured for both beginners and expert users (with separate expert sections).

### Cross-References
The modular structure allows each component to be documented independently while maintaining coherent cross-references across the entire guide.

## Working with This Documentation

### When editing documentation:
1. Identify which component file needs modification based on the feature being documented
2. Common features affecting multiple classes should be edited in `common-*.tex` files
3. Class-specific features go in the respective class documentation files
4. Expert-level content should be in `*-experts-en.tex` files

### Testing changes:
1. Rebuild the complete guide after changes to verify cross-references work
2. Check that index and glossary entries are correct
3. Test with both regular LaTeX and development versions (`pdflatex-dev`)

### Maintaining consistency:
1. Follow existing terminology defined in `terms-en.tex`
2. Use consistent command documentation format
3. Maintain the distinction between user-level and expert-level documentation
