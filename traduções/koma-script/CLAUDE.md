# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the KOMA-Script bundle, a comprehensive LaTeX2e document class and package system. KOMA-Script provides versatile replacements for standard LaTeX classes (article, book, report, letter) with extensive customization capabilities. The project is maintained by Markus Kohm and has been in development since 1994.

The repository contains:
- Source files (`.dtx` format) for all KOMA-Script classes and packages
- English documentation in the `doc/` directory
- Installation and build scripts (`scrmain.ins`, `scrdocstrip.tex`)

## Building the Project

### Generate Classes and Packages from Source

To unpack all KOMA-Script files from the documented source files:

```bash
tex scrmain.ins
```

This generates `.cls` (classes), `.sty` (packages), `.lco` (letter class options), `.clo` (class options), and `.hak` (hook files).

### Install Using l3build

From the repository root:

```bash
# Install development version without manual
l3build install

# Install with complete manual
l3build install --full

# Install to specific TEXMF tree (required for MiKTeX)
l3build install --texmfhome <TEXMF-ROOT>

# Uninstall
l3build uninstall
```

### Build Documentation

The main English documentation is in `doc/scrguide-en.tex`:

```bash
cd doc

# IMPORTANT: Generate letter examples first
latex scrlttr2-examples.dtx

# Build the complete guide (requires multiple passes)
pdflatex scrguide-en.tex
makeindex -s scrguide.ist scrguide-en.idx
makeindex -s scrguide.gst -o scrguide-en.gls scrguide-en.glo
bibtex scrguide-en
pdflatex scrguide-en.tex
pdflatex scrguide-en.tex
pdflatex scrguide-en.tex  # Run additional passes if labels changed
```

### Build Implementation Documentation

For any `.dtx` file, generate its implementation documentation:

```bash
# First, create the documentation class
tex koma-script-source-doc.dtx

# Then generate documentation for specific components
lualatex-dev <component>.dtx
makeindex <component>
lualatex-dev <component>.dtx
lualatex-dev <component>.dtx
```

### Testing with Development LaTeX

For pre-release testing, use development versions of LaTeX engines:
- `pdflatex-dev` instead of `pdflatex`
- `lualatex-dev` instead of `lualatex`
- `xelatex-dev` instead of `xelatex`

## Source Code Architecture

### File Organization

The KOMA-Script source is organized into documented source files (`.dtx`):

**Kernel Components** (scrkernel-*.dtx):
- `scrkernel-version.dtx` - Version information
- `scrkernel-basics.dtx` - Core functionality (207+ KB, fundamental features)
- `scrkernel-sections.dtx` - Section commands (281+ KB)
- `scrkernel-typearea.dtx` - Page layout calculation (130+ KB)
- `scrkernel-fonts.dtx` - Font handling (87+ KB)
- `scrkernel-floats.dtx` - Float environments (78+ KB)
- `scrkernel-footnotes.dtx` - Footnote customization
- `scrkernel-title.dtx` - Title pages
- `scrkernel-notepaper.dtx` - Letter notepaper (190+ KB)
- `scrkernel-letterclassoptions.dtx` - Letter class options
- `scrkernel-pagestyles.dtx` - Page style definitions
- `scrkernel-language.dtx` - Language support (79+ KB)
- `scrkernel-compatibility.dtx` - Standard class compatibility
- And others for bibliography, index, lists, paragraphs, TOC, variables, etc.

**Layer System** (scrlayer*.dtx):
- `scrlayer.dtx` - Layer management for page styles (173+ KB)
- `scrlayer-scrpage.dtx` - Page header/footer customization (98+ KB)
- `scrlayer-notecolumn.dtx` - Note columns parallel to text (62+ KB)

**Standalone Packages**:
- `tocbasic.dtx` - Table of contents management (103+ KB)
- `scrbase.dtx` - Basic features (key=value, conditionals)
- `scrlfile.dtx` / `scrlfile-hook.dtx` - File loading manipulation
- `typearea.dtx` - Type area calculation (can be used standalone)
- `scraddr.dtx` - Address file handling
- `scrtime.dtx` - Time formatting
- `scrextend.dtx` - KOMA features for non-KOMA classes
- `scrjura.dtx` - Legal document support
- `scrlogo.dtx` - KOMA-Script logo
- `japanlco.dtx` - Japanese letter class options

### Build System Files

- `scrmain.ins` - Main docstrip installation script
- `scrstrip.inc` / `scrstrop.inc` - Docstrip include files
- `scrdocstrip.tex` - Custom docstrip configuration

### Documentation Architecture

The `doc/` directory contains modular English documentation:

**Main Structure**:
- `scrguide-en.tex` - Main document entry point
- `scrguide-body.tex` - Body that includes all component files
- `scrguide.cls` - Custom document class for the guide
- `scrguide.bib` - Bibliography database
- `scrguide.ist` / `scrguide.gst` - Index and glossary styles

**Component Documentation**:
- `scrbookreportarticle-en.tex` - Core classes (scrbook, scrreprt, scrartcl)
- `scrlttr2-en.tex` - Letter class
- `typearea-en.tex` - Page layout package
- `scrlayer-en.tex`, `scrlayer-scrpage-en.tex` - Layer system
- `tocbasic-en.tex`, `scrbase-en.tex`, etc. - Package documentation
- Files with `*-experts-en.tex` suffix contain advanced documentation

**Common Features**:
- `common-*.tex` files document features shared across multiple classes
- Examples: `common-footnotes-en.tex`, `common-titles-en.tex`, `common-options-en.tex`

## Key Characteristics

### Modular Design

KOMA-Script uses a highly modular architecture where:
1. Core functionality is split into scrkernel-* components
2. Each major feature area has its own `.dtx` file
3. Packages can be used independently or with KOMA classes
4. Common features are shared across multiple classes

### Documented Source Format

All source files use the `.dtx` (documented TeX) format:
- Source code and documentation are interleaved
- DocStrip guards control what gets extracted (e.g., `%<*package>`)
- Running `tex scrmain.ins` extracts usable files
- Running `lualatex-dev` on `.dtx` produces implementation documentation

### Version Control

- Version information is centralized in `scrkernel-version.dtx`
- Current version: 3.48 (2025/09/09)
- All files include LPPL 1.3c license headers

## Development Workflows

### When Modifying Source Code

1. Edit the appropriate `.dtx` file (never edit generated `.cls` or `.sty` files directly)
2. Run `tex scrmain.ins` to regenerate classes/packages
3. Test changes with both regular and `-dev` LaTeX engines
4. Update implementation documentation if needed

### When Modifying Documentation

1. Identify the correct file in `doc/`:
   - Component-specific: edit the component's `-en.tex` file
   - Common features: edit the appropriate `common-*-en.tex` file
   - Expert content: edit `*-experts-en.tex` files
2. Rebuild the complete guide to verify cross-references
3. Check index and glossary entries

### Cross-Compatibility Testing

Test with multiple scenarios:
- Standard LaTeX classes vs KOMA classes
- Different page sizes and paper formats
- Various language settings (babel, polyglossia)
- Both PDF and DVI output modes
- Development LaTeX versions (`pdflatex-dev`, etc.)

## Important Conventions

### File Naming

- `-en.tex` suffix: English documentation
- `common-*.tex`: Features shared across classes
- `*-experts-en.tex`: Advanced/expert documentation
- `scrkernel-*.dtx`: Core kernel components
- `.lco` files: Letter class options
- `.hak` files: Hooks for package compatibility

### License

All files are under LPPL 1.3c (LaTeX Project Public License). See `lppl.txt` (English) or `lppl-de.txt` (German).

### Maintenance

The project is author-maintained by Markus Kohm. Assistance is actively sought for testing, documentation, and development (see CONTRIBUTING.md).
