# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**tkz-euclide** is a LaTeX package for drawing two-dimensional Euclidean geometric figures using TikZ. It provides tools to define points and manipulate them in a Cartesian orthonormal coordinate system (unit = 1 cm), reproducing geometric constructions as they would be done by hand.

Current version: 5.11c (2025/09/17)

## Building the Documentation

The documentation is built using LuaLaTeX:

```bash
cd doc/latex
lualatex TKZdoc-euclide-main.tex
```

The main documentation file is `doc/latex/TKZdoc-euclide-main.tex`, which uses the `lua` option for tkz-euclide. It compiles to produce `doc/tkz-euclide.pdf`.

## Package Architecture

### Main Entry Point

- **`latex/tkz-euclide.sty`**: Main package file that declares two options:
  - `lua`: Enables Lua-based calculations (faster and more precise)
  - `mini`: Minimal mode when used with `tkz-elements` package (focuses only on drawings)

### Module Organization

The package loads different sets of files based on options:

1. **Base modules** (loaded when `tkz-base` is not already present):
   - `tkz-tools-eu-base.tex`: Base utility functions
   - `tkz-obj-eu-points.tex`: Point object definitions
   - `tkz-draw-eu-points.tex`: Point drawing commands
   - `tkz-lib-eu-marks.tex`: Marking utilities
   - `tkz-tools-eu-utilities.tex`: General utilities
   - `tkz-tools-eu-BB.tex`: Bounding box management

2. **Standard mode** (when `lua` option is not set):
   - `obj/tkz-obj-eu-*.tex`: Object definition files (points, circles, lines, polygons, triangles)
   - `tools/tkz-tools-eu-*.tex`: Calculation and math utilities (angles, intersections, math)

3. **Lua mode** (when `lua` option is set):
   - `obj-lua/tkz-obj-eu-lua-*.tex`: Lua-based object definitions
   - `tools-lua/tkz-tools-eu-lua-*.tex`: Lua-based calculations
   - Lua mode provides the same functionality with better performance

4. **Drawing modules** (always loaded):
   - `drawings/tkz-draw-eu-*.tex`: Drawing commands for lines, circles, arcs, angles, polygons, sectors, compass, protractor, etc.

5. **Mini mode**: Loads only essential drawing commands with Lua support enabled

### File Categories

- **`latex/obj/`**: Object definition macros (non-Lua calculations)
- **`latex/obj-lua/`**: Object definition macros (Lua-based calculations)
- **`latex/tools/`**: Mathematical utilities and intersection calculations (non-Lua)
- **`latex/tools-lua/`**: Mathematical utilities using Lua
- **`latex/drawings/`**: Drawing commands (geometry rendering)
- **`latex/libs/`**: Support libraries (marks, shapes)
- **`latex/tkz-euclide.cfg`**: Default style configurations (colors, line widths, point styles)

### Configuration System

Default styles are defined in `tkz-euclide.cfg`, including:
- Point styles (shape, color, size, position)
- Line styles (color, width, style)
- Circle styles
- Label styles
- Compass and angle mark styles

Users can override these by creating a custom `tkz-euclide.cfg` in their TEXINPUTS path.

## Code Patterns

### Dual Implementation (Lua vs. Non-Lua)

The package maintains parallel implementations:
- **Non-Lua path**: Uses xfp package for calculations
- **Lua path**: Uses Lua for calculations (enabled with `\usepackage[lua]{tkz-euclide}`)

When modifying functionality, check if changes are needed in both:
- `latex/obj/tkz-obj-eu-points-by.tex` (standard)
- `latex/obj-lua/tkz-obj-eu-lua-points-by.tex` (Lua variant)

### Conditional Compilation

The main `.sty` file uses conditional loading:
```latex
\if@tkzlua
  % Load Lua-based modules
\else
  % Load standard modules
\fi
```

### Dependencies

- **Required**: tikz (with multiple libraries), xfp
- **Optional**: luacode (when using `lua` option)
- **Compatible with**: pdfLaTeX and LuaLaTeX engines
- **May coexist with**: tkz-base, tkz-elements packages

## Documentation Structure

Documentation is modular, located in `doc/latex/`:
- **TKZdoc-euclide-main.tex**: Main documentation file (compiles everything)
- **TKZdoc-euclide-*.tex**: Topic-specific documentation sections:
  - `points`, `lines`, `circles`, `angles`, `triangles`, `polygons`
  - `intersection`, `marking`, `labelling`, `drawing`, `filling`, `clipping`
  - `compass`, `show`, `styles`, `tools`, `examples`, `FAQ`
  - `lua`, `news`, `installation`, `presentation`

Each section is included via `\input` in the main file.

## Important Notes

### Backwards Compatibility

Version 4.x introduced major breaking changes:
- Deprecated macros like `\tkzDrawTriangle`, `\tkzDrawSquare`, etc. were removed
- Argument order changed for some commands (e.g., `\tkzDefPointOnCircle`)
- Old style options (`label seg style`, `label line style`) unified to `label style`

See Changelog.md for full list of breaking changes.

### Coordinate System

All constructions use a Cartesian orthonormal coordinate system with 1 cm = 1 unit. The package is designed to mirror hand-drawn geometric constructions step by step.

### Testing Changes

When modifying the package:
1. Test with both pdfLaTeX and LuaLaTeX
2. Test with and without the `lua` option
3. Verify examples in documentation still compile correctly
4. Check that both standard and Lua code paths work if applicable
