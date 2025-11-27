# Changelog — tkz-euclide

All notable changes to this project will be documented here.  
The version suffix **c** indicates the CTAN release.  
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [5.11c] — 2025/09/17
### Fixed
- Macro `\tkzClipSector`.

### Docs
- Example *Pentagon in a square*.
- Example *Part I: golden triangle* in the **Presentation** section.

---

## [5.10c]
### Added
- `mini` option.
- French documentation on [altermundus.fr](http://altermundus.fr).

### Changed
- Extracted `tkz-tool-eu-angles.arc.tex` from `tkz-tool-eu-angles.tex`.

---

## [5.06c]
### Added
- `\tkzSetUpCircle`.

### Fixed
- Bug in `\tkzLabelAngle` with option `angle`.
- Typos in the documentation.

### Removed
- Obsolete French texts.

---

## [5.05c]
### Fixed
- Documentation corrections.

---

## [5.04c]
### Changed
- Renamed several files.

---

## [5.03c]
### Added
- Macro `\tkzDrawEllipse`.

### Fixed
- Bug in `tkz-obj-lua-points-spc.tex` (`\tkzDefBarycentricPointTwo`).

---

## [5.02c]
### Fixed
- Duplicate macro in `tkz-lib-eu-shape.tex`.
- Removed duplicate definitions in `tkz-draw-eu-points.tex`.

---

## [5.01c]
### Added
- File `tkz-obj-eu-points-spc.tex`.

### Changed
- Cleaned `tkz-tools-lua-math.tex`.

### Fixed
- Incorrect date in `tkz-euclide.sty`.

---

## [5.00c]
### Added
- **`lua` option** for performing calculations with Lua (faster and more precise).

---

## [4.25c]
### Removed
- `\input{tkz-obj-eu-draw-triangles.tex}` from the list of loaded files.

---

## [4.24c]
### Changed
- Macro `\tkzDefCircle[apollonius]`.

### Fixed
- Bug in `\tkzMarkAngle`.

---

## [4.23c]
### Changed
- Macro `\tkzDefRadicalAxis`.

### Fixed
- Bug in `\tkzDrawSemiCircle`.

### Removed
- Deprecated code.

---

## [4.22c]
### Changed
- Documentation updated (clarified usage of `\tkzDefCircle[R](...)`).

### Fixed
- Bug in `\tkzMarkAngle`.

### Removed
- Obsolete options for `\tkzDrawCircle` (now always requires center + one point).

---

## [4.21c]
### Fixed
- Corrupted archive (all `|` symbols disappeared).

---

## [4.20c ... 4.00c] — Major restructuring
### Added
- `\tkzDefLine[euler]`, `\tkzDefLine[altitude]`, `\tkzDefLine[tangent ...]`.
- `\tkzPicAngle`, `\tkzFillAngles`.
- `\tkzDotProduct`, `\tkzPowerCircle`, `\tkzDefRadicalAxis`.
- `\tkzIsOrtho`, `\tkzIsLinear`.
- Arc options: `reverse`, `next to`, `in rad`.
- Vector style: `\tikzset{vector style/.style={>=Latex,->}}`.
- Arrow options for lines and circles.

### Changed
- Unified label styles (only `label style` remains).
- Circle inversion rewritten.
- Argument order of `\tkzDefPointOnCircle` modified.
- Documentation extensively revised.

### Removed
- Deprecated macros: `\tkzDrawTriangle`, `\tkzDrawSquare`, `\tkzDrawGoldRectangle`, etc.
- Old options (`label seg style`, `label line style`, `label angle style`).
