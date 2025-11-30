#!/usr/bin/env python3
"""
Enhanced Theme Generator for Animated Octo Giggle v4.0
Advanced Zed theme features with ultra-vibrant text colors
"""

import colorsys
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

# Extended syntax scopes with ULTRA-VIBRANT colors
EXTENDED_SYNTAX = {
    # Functions - Purple family
    "function.method": {"color": "#da9eff"},
    "function.builtin": {"color": "#b967ff"},
    "function.special": {"color": "#ff78b8"},
    # Variables - Teal/Cyan family
    "variable.builtin": {"color": "#ff4757", "font_style": "italic"},
    "variable.parameter": {"color": "#70e8c8", "font_style": "italic"},
    "variable.other.member": {"color": "#5ec9ff"},
    "variable.special": {"color": "#ff78b8"},
    "variable.readonly": {"color": "#ff4757"},
    # JSX/TSX
    "tag.jsx": {"color": "#ff4757"},
    "tag.attribute": {"color": "#ffc938"},
    "tag.delimiter": {"color": "#7ac07a"},
    # Types
    "type.builtin": {"color": "#52c9d1", "font_style": "italic"},
    "type.interface": {"color": "#5ec9ff"},
    "type.class": {"color": "#ffc938"},
    # Strings
    "string.regexp": {"color": "#ff78b8"},
    "string.escape": {"color": "#b967ff"},
    "string.special": {"color": "#3affdb"},
    "string.special.symbol": {"color": "#ffc938"},
    # Markdown
    "markup.heading.1": {"color": "#ff4757", "font_weight": 700},
    "markup.heading.2": {"color": "#ffc938", "font_weight": 700},
    "markup.heading.3": {"color": "#3affdb", "font_weight": 600},
    "markup.heading.4": {"color": "#5ec9ff", "font_weight": 600},
    "markup.heading.5": {"color": "#b967ff", "font_weight": 500},
    "markup.heading.6": {"color": "#70e8c8", "font_weight": 500},
    "markup.code": {"color": "#b967ff"},
    "markup.link": {"color": "#3affdb"},
    "markup.quote": {"color": "#7ac07a", "font_style": "italic"},
    "markup.list": {"color": "#52c9d1"},
    "markup.raw": {"color": "#3affdb"},
    "markup.bold": {"font_weight": 700},
    "markup.italic": {"font_style": "italic"},
    # Emphasis
    "emphasis": {"color": "#5ec9ff", "font_style": "italic"},
    "emphasis.strong": {"color": "#ff4757", "font_weight": 700},
    # Rust
    "attribute.rust": {"color": "#ffc938"},
    "lifetime": {"color": "#ff78b8", "font_style": "italic"},
    "macro": {"color": "#b967ff"},
    # Python
    "function.decorator": {"color": "#ffc938"},
    "string.documentation": {"color": "#7ac07acc", "font_style": "italic"},
    # JavaScript/TypeScript
    "constructor.javascript": {"color": "#da9eff"},
    "constructor.typescript": {"color": "#da9eff"},
    # CSS/SCSS
    "property.css": {"color": "#5ec9ff"},
    "property.class": {"color": "#ffc938"},
    "property.id": {"color": "#ff4757"},
    "selector": {"color": "#6ed946"},
    "selector.pseudo": {"color": "#5ec9ff"},
    # SQL
    "keyword.sql": {"color": "#d4d9c8"},
    "function.sql": {"color": "#da9eff"},
    # Comments
    "comment.doc": {"color": "#3affdb", "font_style": "italic"},
    "comment.block.documentation": {"color": "#3affdb", "font_style": "italic"},
    # Advanced syntax
    "enum": {"color": "#ff4757"},
    "variant": {"color": "#da9eff"},
    "namespace": {"color": "#70e8c8"},
    "label": {"color": "#5ec9ff"},
    "embedded": {"color": "#3affdb"},
    "preproc": {"color": "#ffc938"},
    "primary": {"color": "#e8f0ee"},
    "title": {"color": "#ff4757", "font_weight": 600},
    "link_text": {"color": "#5ec9ff", "font_style": "italic"},
    "link_uri": {"color": "#3affdb"},
    # Punctuation
    "punctuation.bracket": {"color": "#d4d9c8"},
    "punctuation.delimiter": {"color": "#d4d9c8"},
    "punctuation.list_marker": {"color": "#ff4757"},
    "punctuation.markup": {"color": "#ff78b8"},
    "punctuation.special": {"color": "#ff4757"},
    # Hints and predictions
    "hint": {"color": "#52c9d1", "font_style": "italic"},
    "predictive": {"color": "#7ac07a99", "font_style": "italic"},
}

# Ultra-vibrant rainbow accents
RAINBOW_ACCENTS = [
    "#ff4757",  # Vivid Red
    "#ffc938",  # Golden Yellow
    "#3affdb",  # Neon Cyan
    "#5ec9ff",  # Electric Blue
    "#b967ff",  # Vibrant Purple
    "#6ed946",  # Vivid Green
]

# Transparency configurations
TRANSPARENCY_CONFIGS = [
    {
        "name": "Glass",
        "suffix": "Glass",
        "description": "Ultra-transparent glass effect",
        "bg_opacity": "99",
        "panel_opacity": "80",
        "editor_opacity": "66",
        "gutter_opacity": "66",
        "border_boost": "1.8",
        "glow_active": True,
    },
    {
        "name": "Transparent",
        "suffix": "Transparent",
        "description": "Balanced transparency",
        "bg_opacity": "b3",
        "panel_opacity": "99",
        "editor_opacity": "80",
        "gutter_opacity": "80",
        "border_boost": "1.5",
        "glow_active": True,
    },
    {
        "name": "Translucent",
        "suffix": "Translucent",
        "description": "Subtle see-through effect",
        "bg_opacity": "cc",
        "panel_opacity": "b3",
        "editor_opacity": "99",
        "gutter_opacity": "99",
        "border_boost": "1.3",
        "glow_active": True,
    },
]

# Blur configurations
BLUR_CONFIGS = [
    {
        "name": "Frosted",
        "suffix": "Frosted",
        "description": "Heavy frosted glass effect",
        "bg_opacity": "80",
        "panel_opacity": "66",
        "editor_opacity": "40",
        "gutter_opacity": "40",
        "border_boost": "2.0",
        "glow_active": True,
        "glow_intensity": "high",
    },
    {
        "name": "Blurred",
        "suffix": "Blurred",
        "description": "Medium blur with vibrancy",
        "bg_opacity": "99",
        "panel_opacity": "80",
        "editor_opacity": "66",
        "gutter_opacity": "66",
        "border_boost": "1.8",
        "glow_active": True,
        "glow_intensity": "medium",
    },
    {
        "name": "Hazy",
        "suffix": "Hazy",
        "description": "Light blur, soft effect",
        "bg_opacity": "b3",
        "panel_opacity": "99",
        "editor_opacity": "80",
        "gutter_opacity": "80",
        "border_boost": "1.5",
        "glow_active": True,
        "glow_intensity": "low",
    },
]


def hex_to_rgba(hex_color: str, alpha: str = "ff") -> str:
    """Convert hex to rgba with alpha"""
    if len(hex_color) == 7:
        return f"{hex_color}{alpha}"
    return hex_color


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple"""
    if len(hex_color) != 7:
        return (0, 0, 0)
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return (r, g, b)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB to hex color"""
    return f"#{r:02x}{g:02x}{b:02x}"


def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """Convert RGB to HSL color space"""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360, s * 100, l * 100)


def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """Convert HSL to RGB color space"""
    h, s, l = h / 360.0, s / 100.0, l / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (int(r * 255), int(g * 255), int(b * 255))


def brighten_color(hex_color: str, factor: float = 1.2) -> str:
    """Brighten a hex color using perceptual lightness in HSL space"""
    if len(hex_color) != 7:
        return hex_color

    r, g, b = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(r, g, b)

    l = min(95, l + (100 - l) * (factor - 1.0))

    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b)


def enhance_color_vibrancy(hex_color: str, vibrancy: float = 1.6) -> str:
    """
    Advanced color enhancement using HSL color space.
    Increases saturation and optimizes lightness for maximum visual impact.
    """
    if len(hex_color) != 7:
        return hex_color

    r, g, b = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(r, g, b)

    # Skip near-grayscale colors
    if s < 5 or l < 8 or l > 94:
        return hex_color

    # Aggressive saturation enhancement
    s = min(100, s * vibrancy)

    # Hue shift toward pure spectrum colors
    pure_hues = [0, 60, 120, 180, 240, 300]
    nearest_hue = min(pure_hues, key=lambda x: min(abs(h - x), 360 - abs(h - x)))
    hue_distance = min(abs(h - nearest_hue), 360 - abs(h - nearest_hue))

    if hue_distance > 0:
        shift_factor = 0.08
        if h < nearest_hue:
            if nearest_hue - h < 180:
                h = h + hue_distance * shift_factor
            else:
                h = h - hue_distance * shift_factor
        else:
            if h - nearest_hue < 180:
                h = h - hue_distance * shift_factor
            else:
                h = h + hue_distance * shift_factor
        h = h % 360

    # Optimize lightness
    if l < 40:
        l = l + (50 - l) * 0.3
    elif l > 70:
        l = l - (l - 65) * 0.2
    else:
        l = l + (60 - l) * 0.1

    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b)


def enhance_text_colors_only(style: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enhance ONLY text and syntax colors - leaves UI structure untouched.
    """
    # Text colors
    if "text" in style:
        style["text"] = enhance_color_vibrancy(style["text"], vibrancy=1.4)
    if "text.muted" in style:
        style["text.muted"] = enhance_color_vibrancy(style["text.muted"], vibrancy=1.6)

    # Editor text
    if "editor.foreground" in style:
        style["editor.foreground"] = enhance_color_vibrancy(
            style["editor.foreground"], vibrancy=1.3
        )
    if "editor.line_number" in style:
        style["editor.line_number"] = enhance_color_vibrancy(
            style["editor.line_number"], vibrancy=1.6
        )
    if "editor.active_line_number" in style:
        style["editor.active_line_number"] = enhance_color_vibrancy(
            style["editor.active_line_number"], vibrancy=1.8
        )
    if "editor.hover_line_number" in style:
        style["editor.hover_line_number"] = enhance_color_vibrancy(
            style["editor.hover_line_number"], vibrancy=1.7
        )

    # Terminal text
    if "terminal.foreground" in style:
        style["terminal.foreground"] = enhance_color_vibrancy(
            style["terminal.foreground"], vibrancy=1.3
        )
    if "terminal.bright_foreground" in style:
        style["terminal.bright_foreground"] = enhance_color_vibrancy(
            style["terminal.bright_foreground"], vibrancy=1.6
        )

    # Terminal ANSI colors
    ansi_colors = [
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "bright_red",
        "bright_green",
        "bright_yellow",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
    ]
    for color in ansi_colors:
        key = f"terminal.ansi.{color}"
        if key in style:
            vibrancy = 2.0 if "bright" in color else 1.8
            style[key] = enhance_color_vibrancy(style[key], vibrancy=vibrancy)

    return style


def add_advanced_features(style: Dict[str, Any]) -> Dict[str, Any]:
    """Add advanced Zed theme features like version control, conflicts, etc."""
    bg_color = style.get("background", "#1e2826")
    if len(bg_color) > 7:
        bg_color = bg_color[:7]

    # Version control colors - vibrant
    style["version_control.added"] = "#6ed946"  # Vivid green
    style["version_control.modified"] = "#ffc938"  # Golden yellow
    style["version_control.deleted"] = "#ff4757"  # Vivid red
    style["version_control.conflict_marker.ours"] = "#6ed94626"  # 15%
    style["version_control.conflict_marker.theirs"] = "#5ec9ff26"  # 15%

    # Conflict markers
    style["conflict"] = "#ffc938"
    style["conflict.background"] = "#ffc93826"  # 15%
    style["conflict.border"] = "#ffc938"

    # Git status colors
    style["created"] = "#6ed946"
    style["created.background"] = "#6ed94626"  # 15%
    style["created.border"] = "#6ed946"

    style["modified"] = "#ffc938"
    style["modified.background"] = "#ffc93826"  # 15%
    style["modified.border"] = "#ffc938"

    style["deleted"] = "#ff4757"
    style["deleted.background"] = "#ff475726"  # 15%
    style["deleted.border"] = "#ff4757"

    style["renamed"] = "#b967ff"
    style["renamed.background"] = "#b967ff26"  # 15%
    style["renamed.border"] = "#b967ff"

    # Diagnostic colors
    style["error"] = "#ff4757"
    style["error.background"] = "#ff475726"  # 15%
    style["error.border"] = "#ff4757"

    style["warning"] = "#ffc938"
    style["warning.background"] = "#ffc93826"  # 15%
    style["warning.border"] = "#ffc938"

    style["info"] = "#5ec9ff"
    style["info.background"] = "#5ec9ff26"  # 15%
    style["info.border"] = "#5ec9ff"

    style["hint"] = "#3affdb"
    style["hint.background"] = "#3affdb26"  # 15%
    style["hint.border"] = "#3affdb"

    style["success"] = "#6ed946"
    style["success.background"] = "#6ed94626"  # 15%
    style["success.border"] = "#6ed946"

    # Predictive/AI text
    style["predictive"] = "#7ac07a99"
    style["predictive.background"] = "#7ac07a26"  # 15%
    style["predictive.border"] = "#7ac07a"

    # Code states
    style["ignored"] = enhance_color_vibrancy(
        style.get("text.muted", "#6b8b6b"), vibrancy=1.4
    )
    style["ignored.background"] = f"{bg_color}80"  # 50%
    style["ignored.border"] = style.get("border", "#394c44")

    style["hidden"] = enhance_color_vibrancy(
        style.get("text.disabled", "#4a6a5a"), vibrancy=1.3
    )
    style["hidden.background"] = f"{bg_color}cc"  # 80%
    style["hidden.border"] = style.get("border.variant", "#2f3e38")

    style["unreachable"] = style.get("text.muted", "#6b8b6b")
    style["unreachable.background"] = f"{bg_color}99"  # 60%
    style["unreachable.border"] = style.get("border.disabled", "#2a3832")

    # Document highlights
    style["editor.document_highlight.read_background"] = "#5ec9ff1a"  # 10%
    style["editor.document_highlight.write_background"] = "#ffc9381a"  # 10%

    # Hover line number
    if "editor.line_number" in style and "editor.hover_line_number" not in style:
        style["editor.hover_line_number"] = enhance_color_vibrancy(
            style["editor.line_number"], vibrancy=1.5
        )

    # Link hover
    style["link_text.hover"] = "#3affdb"

    return style


def add_rainbow_accents(style: Dict[str, Any]) -> Dict[str, Any]:
    """Add ultra-vibrant rainbow indent guide colors"""
    enhanced_accents = [
        enhance_color_vibrancy(color, vibrancy=1.7) for color in RAINBOW_ACCENTS
    ]
    style["accents"] = enhanced_accents
    return style


def add_extended_syntax(style: Dict[str, Any]) -> Dict[str, Any]:
    """Add extended syntax highlighting scopes"""
    if "syntax" not in style:
        style["syntax"] = {}

    bg_color = style.get("background", "#1e2826")
    if len(bg_color) > 7:
        bg_color = bg_color[:7]

    # Enhance existing syntax colors
    for scope, props in style["syntax"].items():
        if "color" in props:
            original = props["color"]
            if len(original) >= 7:
                base_color = original[:7]
                vibrant = enhance_color_vibrancy(base_color, vibrancy=1.5)
                if len(original) > 7:
                    vibrant = vibrant + original[7:]
                style["syntax"][scope] = {**props, "color": vibrant}

    # Add extended syntax
    for scope, props in EXTENDED_SYNTAX.items():
        enhanced_props = props.copy()
        if "color" in enhanced_props:
            original_color = enhanced_props["color"]
            if len(original_color) >= 7:
                base_color = original_color[:7]
                vibrant_color = enhance_color_vibrancy(base_color, vibrancy=1.6)
                if len(original_color) > 7:
                    vibrant_color = vibrant_color + original_color[7:]
                enhanced_props["color"] = vibrant_color
        style["syntax"][scope] = enhanced_props

    return style


def add_multiplayer_colors(style: Dict[str, Any]) -> Dict[str, Any]:
    """Add vibrant multiplayer cursor colors"""
    player_colors = [
        "#3affdb",  # Neon cyan
        "#b967ff",  # Vibrant purple
        "#6ed946",  # Vivid green
        "#ffc938",  # Golden yellow
        "#ff4757",  # Vivid red
        "#5ec9ff",  # Electric blue
        "#ff78b8",  # Hot pink
        "#70e8c8",  # Bright aqua
    ]

    style["players"] = [
        {
            "cursor": color,
            "background": color,
            "selection": f"{color}4d",  # 30%
        }
        for color in player_colors
    ]

    return style


def create_transparent_variant(
    theme: Dict[str, Any], config: Dict[str, Any]
) -> Dict[str, Any]:
    """Create transparent variant"""
    variant = json.loads(json.dumps(theme))
    variant["name"] = f"{theme['name']} ({config['suffix']})"

    bg_color = variant["style"]["background"]
    accent_color = variant["style"].get("text.accent", "#9cb5aa")

    if len(bg_color) == 7:
        variant["style"]["background.appearance"] = "transparent"
        variant["style"]["background"] = hex_to_rgba(bg_color, config["bg_opacity"])
        variant["style"]["status_bar.background"] = hex_to_rgba(
            bg_color, config["bg_opacity"]
        )
        variant["style"]["title_bar.background"] = hex_to_rgba(
            bg_color, config["bg_opacity"]
        )

        # Fully transparent editor/panels
        variant["style"]["editor.background"] = "#00000000"
        variant["style"]["editor.gutter.background"] = "#00000000"
        variant["style"]["terminal.background"] = "#00000000"
        variant["style"]["panel.background"] = "#00000000"
        variant["style"]["toolbar.background"] = "#00000000"
        variant["style"]["tab_bar.background"] = "#00000000"

        # Keep popups slightly transparent for consistent look
        variant["style"]["elevated_surface.background"] = hex_to_rgba(
            bg_color, config["panel_opacity"]
        )
        variant["style"]["surface.background"] = hex_to_rgba(
            bg_color, config["panel_opacity"]
        )

        # Dramatically enhance borders for better visibility
        vibrant_accent = enhance_color_vibrancy(accent_color, vibrancy=2.2)
        border_factor = float(config["border_boost"]) * 1.8
        variant["style"]["border.focused"] = brighten_color(
            vibrant_accent, border_factor
        )
        variant["style"]["border.selected"] = brighten_color(
            vibrant_accent, border_factor
        )
        variant["style"]["panel.focused_border"] = brighten_color(
            vibrant_accent, border_factor
        )
        variant["style"]["pane.focused_border"] = brighten_color(
            vibrant_accent, border_factor
        )

    return variant


def create_blurred_variant(
    theme: Dict[str, Any], config: Dict[str, Any]
) -> Dict[str, Any]:
    """Create blurred variant"""
    variant = json.loads(json.dumps(theme))
    variant["name"] = f"{theme['name']} ({config['suffix']})"

    bg_color = variant["style"]["background"]
    accent_color = variant["style"].get("text.accent", "#9cb5aa")

    if len(bg_color) == 7:
        variant["style"]["background.appearance"] = "blurred"
        variant["style"]["background"] = hex_to_rgba(bg_color, config["bg_opacity"])
        variant["style"]["status_bar.background"] = hex_to_rgba(
            bg_color, config["bg_opacity"]
        )
        variant["style"]["title_bar.background"] = hex_to_rgba(
            bg_color, config["bg_opacity"]
        )

        # Fully transparent for maximum blur visibility
        variant["style"]["editor.background"] = "#00000000"
        variant["style"]["editor.gutter.background"] = "#00000000"
        variant["style"]["terminal.background"] = "#00000000"
        variant["style"]["panel.background"] = "#00000000"
        variant["style"]["toolbar.background"] = "#00000000"
        variant["style"]["tab_bar.background"] = "#00000000"

        # Keep popups slightly transparent for consistent look
        variant["style"]["elevated_surface.background"] = hex_to_rgba(
            bg_color, config["panel_opacity"]
        )
        variant["style"]["surface.background"] = hex_to_rgba(
            bg_color, config["panel_opacity"]
        )

        # Dramatically enhance borders for blur visibility
        vibrant_accent = enhance_color_vibrancy(accent_color, vibrancy=2.5)
        border_factor = float(config["border_boost"]) * 2.0
        variant["style"]["border.focused"] = brighten_color(
            vibrant_accent, border_factor
        )
        variant["style"]["border.selected"] = brighten_color(
            vibrant_accent, border_factor
        )
        variant["style"]["panel.focused_border"] = brighten_color(
            vibrant_accent, border_factor
        )
        variant["style"]["pane.focused_border"] = brighten_color(
            vibrant_accent, border_factor
        )

    return variant


def enhance_theme_file(input_path: Path, output_path: Path):
    """Enhance theme with all features"""
    print(f"📖 Reading {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    enhanced_themes = []

    for theme in data["themes"]:
        print(f"\n  ✨ Enhancing: {theme['name']}")

        # Enhance text colors only
        theme["style"] = enhance_text_colors_only(theme["style"])

        # Add advanced features
        theme["style"] = add_advanced_features(theme["style"])

        # Add rainbow accents
        theme["style"] = add_rainbow_accents(theme["style"])

        # Add extended syntax
        theme["style"] = add_extended_syntax(theme["style"])

        # Add multiplayer colors
        theme["style"] = add_multiplayer_colors(theme["style"])

        enhanced_themes.append(theme)
        print(f"    ✓ Enhanced with vibrant text colors & advanced features")

        # Create variants
        for config in TRANSPARENCY_CONFIGS:
            transparent = create_transparent_variant(theme, config)
            enhanced_themes.append(transparent)
            print(f"    🪟 {transparent['name']}")

        for config in BLUR_CONFIGS:
            blurred = create_blurred_variant(theme, config)
            enhanced_themes.append(blurred)
            print(f"    💨 {blurred['name']}")

    data["themes"] = enhanced_themes

    print(f"\n💾 Writing {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Created {len(enhanced_themes)} theme variants!")
    print(f"\n🎨 Advanced features:")
    print(f"  ✓ Ultra-vibrant text/syntax colors (+40-100% saturation)")
    print(f"  ✓ Version control colors (added/modified/deleted)")
    print(f"  ✓ Conflict markers (ours/theirs)")
    print(f"  ✓ Diagnostic colors (error/warning/info/hint)")
    print(f"  ✓ Predictive/AI text styling")
    print(f"  ✓ Document highlight (read/write)")
    print(f"  ✓ Code states (ignored/hidden/unreachable)")
    print(f"  ✓ Multiplayer cursors (8 vibrant colors)")
    print(f"  ✓ Rainbow indent guides")
    print(f"  ✓ Extended syntax scopes ({len(EXTENDED_SYNTAX)}+)")
    print(f"  ✓ Transparency variants (3)")
    print(f"  ✓ Blur variants (3)")


def main():
    """Main entry point"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    input_file = project_root / "themes" / "arstotzka-original-backup.json"
    output_file = project_root / "themes" / "arstotzka.json"

    if not input_file.exists():
        print(f"❌ Error: {input_file} not found!")
        sys.exit(1)

    print("🎨 Animated Octo Giggle - Advanced Theme Generator v4.0")
    print("=" * 60)
    enhance_theme_file(input_file, output_file)
    print("=" * 60)
    print("🎉 Done! Restart Zed and enjoy your enhanced themes!")


if __name__ == "__main__":
    main()
