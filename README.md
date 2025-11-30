# Animated Octo Giggle

> **Dark Visual Studio Code themes for Zed, made even darker and perfect**

A port of the beloved [August Themes](https://github.com/inci-august/august-themes) by inci-august to Zed Editor, with 28 stunning variants featuring transparent/blurred **window chrome**, vibrant enhanced colors (+30% saturation), glass morphism effects, and rainbow indentation.

## ⚠️ Important: Transparency Limitations

**What works:** Window chrome (title bar, status bar) is beautifully transparent/blurred! ✅  
**What doesn't (yet):** Editor content area remains opaque (Zed limitation) ❌  

See [ZED_TRANSPARENCY_REALITY.md](ZED_TRANSPARENCY_REALITY.md) for full details.

## About The Name

The name "Animated Octo Giggle" was suggested by GitHub's repository name generator. We kept it because it perfectly captures the whimsical, creative spirit of these beautiful dark themes.

## Themes Included

### Arstotzka Series (28 variants!) 🎨✨

A sophisticated dark theme family featuring muted sage greens, deep reds, and teal accents. Perfect for long coding sessions with reduced eye strain.

**Each base theme comes in 7 background modes:**
- **Standard** - Solid backgrounds (original)
- **Glass** - 85% opacity, ultra-transparent glass effect
- **Transparent** - 90% opacity, balanced transparency
- **Translucent** - 94% opacity, subtle see-through effect
- **Frosted** - 75% opacity, heavy frosted glass with blur
- **Blurred** - 80% opacity, medium blur with vibrancy
- **Hazy** - 85% opacity, light blur with soft effect

#### Base Themes

- **Arstotzka** - The original, ultra-dark variant
  - Background: `#0f0b0b` (very dark brown-black)
  - Accent: `#9cb5aa` (light teal)
  - Badge: `#a62828` (deep red)

- **Arstotzka Lighter** - Slightly brighter for better visibility
  - Background: `#191212` (lighter charcoal)

- **Arstotzka Darker** - Maximum darkness for OLED displays
  - Background: `#050404` (nearly black)

- **Arstotzka v2** - Alternative variant with same base color
  - Background: `#0f0b0b`

#### Available Variants

Choose from 28 total combinations (4 base × 7 modes):

**Arstotzka Series:**
1. Arstotzka (Standard)
2. Arstotzka (Glass) - Ultra-transparent ✨
3. Arstotzka (Transparent) - Balanced
4. Arstotzka (Translucent) - Subtle
5. Arstotzka (Frosted) - Heavy blur 💨
6. Arstotzka (Blurred) - Medium blur
7. Arstotzka (Hazy) - Light blur

**Arstotzka Lighter Series:**
8-14. Same 7 modes with lighter background

**Arstotzka Darker Series:**
15-21. Same 7 modes with darker background (OLED-optimized)

**Arstotzka v2 Series:**
22-28. Same 7 modes with alternative styling

### Color Philosophy

All Arstotzka themes share the same carefully crafted color palette:

- **Sage Greens**: `#556955`, `#9cb5aa`, `#8bdbc2` - Primary text and strings
- **Deep Red**: `#a62828` - Errors, constants, and important UI elements
- **Gold**: `#b19600` - Warnings and modifications
- **Blue**: `#85a4b1` - Variables and Git additions
- **Purple**: `#9258d8`, `#b180d7` - Functions and constructors

## Installation

### Method 1: Manual Installation (Recommended)

1. Download the theme file from this repository:
   - `themes/arstotzka.json`

2. Copy it to your Zed themes directory:
   - **macOS/Linux**: `~/.config/zed/themes/`
   - **Windows**: `%USERPROFILE%\AppData\Roaming\Zed\themes\`

3. Restart Zed or reload your configuration

4. Open the command palette (`Cmd+Shift+P` or `Ctrl+Shift+P`)

5. Type "theme selector: toggle" (or use `Cmd+K Cmd+T` / `Ctrl+K Ctrl+T`)

6. Choose from:
   - Arstotzka
   - Arstotzka Lighter
   - Arstotzka Darker
   - Arstotzka v2

### Method 2: Via Settings

Add to your Zed settings (`Cmd+,` or `Ctrl+,`):

```json
{
  "theme": {
    "mode": "dark",
    "dark": "Arstotzka"
  }
}
```

## Features

### ✅ What Actually Works
- ✅ **Window Chrome Transparency** - Beautiful transparent/blurred title bar & status bar!
- ✅ **Vibrant Enhanced Colors** - 30% more saturated syntax colors for better contrast ✨
- ✅ **28 Theme Variants** - 4 base themes × 7 background modes
- ✅ **Glass Morphism Effects** - Modern frosted glass with glow effects in window chrome
- ✅ **Multiple Transparency Levels** - Glass (85%), Transparent (90%), Translucent (94%)
- ✅ **Multiple Blur Intensities** - Frosted (heavy), Blurred (medium), Hazy (light) - macOS vibrancy!
- ✅ **Rainbow Indent Guides** - Beautiful 6-color gradient for nested code
- ✅ **Extended Syntax Highlighting** - 67 scopes for superior code highlighting
- ✅ **Enhanced Borders & Vibrancy** - Better visibility with transparency
- ✅ **Active Element Glow** - Subtle glows for focused UI elements
- ✅ **Complete Syntax Highlighting** - Enhanced support for JS/TS, Rust, Python, Markdown, CSS
- ✅ **Terminal Colors** - Full ANSI color support (24 colors)
- ✅ **Git Integration** - Distinct colors for added, modified, and deleted files
- ✅ **Eye Strain Reduction** - Ultra-dark backgrounds with carefully balanced contrast

### ⚠️ Current Limitations (Zed Engine)
- ❌ **Editor content area** - Remains opaque (not a theme limitation, it's Zed!)
- ❌ **Panel backgrounds** - Stay solid (Zed limitation)
- ❌ **Wallpaper behind code** - Not supported yet (Zed limitation)

**See [ZED_TRANSPARENCY_REALITY.md](ZED_TRANSPARENCY_REALITY.md) for full technical explanation.**

## Screenshots

_Coming soon!_

## Credits

### Original Theme
- **August Themes** by [inci-august](https://github.com/inci-august)
- Original VS Code extension: [August Themes on VS Marketplace](https://marketplace.visualstudio.com/items?itemName=inci-august.august-themes)

### Inspiration
The Arstotzka themes are modified versions inspired by various excellent themes in the community.

### This Port
- Ported to Zed by the Animated Octo Giggle team
- Maintained with love and attention to color accuracy

## Roadmap

Phase 1 (Current):
- [x] Arstotzka Series (28 variants with glass morphism!)

Phase 2 (Planned):
- [ ] BeardedTheme Oceanic Reversed
- [ ] Catppuccin
- [ ] City Lights
- [ ] Drawbridge
- [ ] Gruvbox

Phase 3 (Future):
- [ ] In Bed By 7pm
- [ ] Ariake Dark
- [ ] Kanagawa
- [ ] Material Ocean
- [ ] Material Palenight
- [ ] Nord
- [ ] Night Owl
- [ ] Radical
- [ ] Rosé Pine

All 31 themes from the original August Themes collection will eventually be ported!

## Contributing

Found a color that doesn't match the original? Have a suggestion? Please open an issue!

## License

MIT License - See LICENSE file for details

## Support

If you enjoy these themes:
- ⭐ Star this repository
- ⭐ Star the [original August Themes](https://github.com/inci-august/august-themes)
- 📢 Share with your fellow Zed users

---

---

## 🌟 Cool Variant Highlights

### Glass Effects (Transparency) - Window Chrome Only
- **Glass** (85%) - Maximum transparency in title/status bars, perfect for showcasing wallpapers
- **Transparent** (90%) - Balanced transparency in window chrome with good readability
- **Translucent** (94%) - Subtle effect in window chrome that keeps focus on code

### Blur Effects (macOS Vibrancy) - Window Chrome Only
- **Frosted** (75%) - Heavy frosted glass in title/status bars, stunning on macOS
- **Blurred** (80%) - Perfect balance of blur in window chrome with readability
- **Hazy** (85%) - Gentle blur in window chrome, soft professional look

### Special Features
- ✨ **Vibrant Colors** - 30% more saturated syntax colors for better contrast!
- 🪟 **Beautiful Window Chrome** - Transparent/blurred title & status bars!
- ✨ **Glow Effects** - Active elements glow subtly for better focus
- 🎨 **Enhanced Borders** - Brighter borders (1.5x) for visibility with transparency
- 💎 **Depth & Layering** - Visual depth throughout UI
- 🌈 **Vibrancy Optimized** - Native macOS vibrancy support in window chrome
- 🌈 **Rainbow Indents** - 6 vibrant colors for code structure

### ⚠️ Reality Check
**Transparency works in:** Title bar, status bar, menu bar (window chrome) ✅  
**Transparency doesn't work in:** Editor area, panels, terminal (Zed limitation) ❌  

But you still get **the best-looking window chrome and most vibrant colors in Zed!** 🎨

**Made with 🎨 by developers who care about dark themes**
