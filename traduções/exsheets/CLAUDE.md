# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains the **exsheets** LaTeX package bundle (v0.21k, 2019/09/30), which provides tools for creating exercise sheets and exams with corresponding solutions. This appears to be part of a Portuguese translation project for LaTeX documentation (`documentacoes-latex-pt-br/traduções`).

## Package Components

The bundle consists of three main package files:
- **exsheets.sty** - Main package written in LaTeX3 (expl3), providing question/solution environments, metadata management, and selective printing
- **exsheets-listings.sty** - Extension for using the `listings` package with exsheets environments
- **exsheets_headings.def** - Heading definitions using coffin-based layout system
- **exsheets_headings.cfg** - Default heading configurations
- **exsheets_configurations.cfg** - User configuration file (currently empty)

## Building Documentation

### Compile the main documentation:
```bash
# Using arara (recommended - directives are in the .tex file)
arara exsheets_en.tex

# Or manually with pdflatex and biber:
pdflatex exsheets_en.tex
biber exsheets_en
pdflatex exsheets_en.tex
pdflatex exsheets_en.tex
pdflatex exsheets_en.tex
```

### Compile the grading table example:
```bash
pdflatex grading-table.tex
```

## Architecture Notes

### LaTeX3 Programming Layer
The package is written using LaTeX3 (expl3) syntax:
- Uses `\ExplSyntaxOn` and `\ExplSyntaxOff` delimiters
- Naming convention: `\<scope>__<module>_<description>_<type>` (e.g., `\l__exsheets_tmpa_tl`)
- Heavy use of property lists (`prop`), sequences (`seq`), token lists (`tl`), integers (`int`), dimensions (`dim`), and floating point (`fp`) variables
- Function variants generated with `\cs_generate_variant:Nn` for flexible argument handling

### Core Functionality
- **Question/Solution Pairs**: Created with `\NewQuSolPair` (or `\NewLstQuSolPair` for listings)
- **Question Properties**: Extensible metadata system via `\DeclareQuestionProperty` and `\SetQuestionProperties`
- **Question Classes**: Categorization system via `\DeclareQuestionClass` for selective printing
- **Headings System**: Object-oriented heading customization using coffins for precise layout control
- **Points System**: Configurable point tracking with `\points`, `\pointssum`, `\totalpoints`
- **Solution Printing**: Solutions can be printed inline, collected and printed later, or printed selectively

### Document Class for Manual
The documentation uses `cnltx-doc` document class with the `load-preamble+` option, suggesting a custom documentation class for LaTeX packages.

## File Modifications

When editing LaTeX package files (.sty, .def, .cfg):
- Preserve the exact indentation and spacing of LaTeX3 code
- Maintain the copyright header format (2011-2019 Clemens Niederberger, LPPL 1.3)
- Keep function naming consistent with expl3 conventions
- Test changes by recompiling the documentation

When editing documentation (.tex):
- The arara directives at the top specify the build sequence
- The documentation is heavily cross-referenced and indexed
- Uses custom cnltx-doc commands for package documentation

## Translation Progress (PT-BR)

Translation status of documentation files to Brazilian Portuguese:

- [x] **exsheets_en.tex** - Main documentation file (COMPLETED ✓) - PDF gerado: 49 páginas
- [x] **grading-table.tex** - Grading table example (COMPLETED ✓) - PDF gerado: 1 página

**Translation Guidelines:**
- Maintain all LaTeX code intact
- Translate all explanatory text and comments
- Preserve code structure and formatting
- Ensure complete fidelity to the original content
- Translate one file at a time, completely, without skipping parts