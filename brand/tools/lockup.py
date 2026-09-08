import subprocess, sys, os, re, json
from xml.etree import ElementTree as ET

S = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(S, "out")
os.makedirs(OUT, exist_ok=True)

MARK = "M0,-46 L34,34 L9,34 L9,20 L-9,20 L-9,34 L-34,34 Z"  # bbox x -34..34, y -46..34
MARK_W, MARK_H = 68, 80
TEAL, TEAL_DARK = "#0f8f87", "#2fd0c3"
CREAM, NAVY = "#f6f3ec", "#0b1622"
INK, INK_DARK = "#1c1b18", "#f1ede4"

FONTS = {
    "montserrat": ("Montserrat", 700, 0.06, 600, 0.32),
    "outfit":     ("Outfit", 600, 0.07, 500, 0.34),
    "sora":       ("Sora", 600, 0.05, 500, 0.30),
}
CAP_BIG, CAP_SMALL, GAP, RULE_GAP, RULE_W = 42.0, 15.0, 13.0, 12.0, 3.0

def run(*a):
    return subprocess.run(a, capture_output=True, text=True, check=True).stdout

def text_to_paths(svg, path):
    """Write svg, convert text to paths with Inkscape, return (plain svg text, bboxes by id)."""
    src = path + ".src.svg"
    open(src, "w").write(svg)
    run("inkscape", src, "--export-text-to-path", "--export-plain-svg", f"--export-filename={path}")
    q = run("inkscape", path, "--query-all")
    bb = {}
    for line in q.splitlines():
        p = line.split(",")
        if len(p) == 5:
            bb[p[0]] = tuple(float(v) for v in p[1:])
    return open(path).read(), bb

def measure(family, weight, ls, text, size=100):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 400">'
           f'<text id="t" x="100" y="300" font-family="{family}" font-weight="{weight}" '
           f'font-size="{size}" letter-spacing="{ls*size}">{text}</text></svg>')
    _, bb = text_to_paths(svg, os.path.join(OUT, f"_m_{family}_{text}.svg"))
    x, y, w, h = bb["t"]
    return dict(size=size, w=w, h=h, top=y - 300, left=x - 100)  # top is negative (above baseline)

def extract_group(plain_svg, gid):
    """Return the inner markup of the element with id=gid, transforms included."""
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    root = ET.fromstring(plain_svg)
    ns = {"s": "http://www.w3.org/2000/svg"}
    for el in root.iter():
        if el.get("id") == gid:
            el.attrib.pop("id", None)
            el.attrib.pop("aria-label", None)
            for k in list(el.attrib):
                if k.startswith("{"):
                    el.attrib.pop(k)
            s = ET.tostring(el, encoding="unicode")
            s = re.sub(r' xmlns(:\w+)?="[^"]+"', "", s)
            s = re.sub(r'\s(font-[a-z-]+|letter-spacing|style)="[^"]*"', "", s)
            return s
    raise KeyError(gid)

def build(fkey, variant, stacked=False):
    family, wb, lsb, ws, lss = FONTS[fkey]
    mb = measure(family, wb, lsb, "PLAYWORKS")
    ms = measure(family, ws, lss, "NORTH")
    size_big = mb["size"] * CAP_BIG / mb["h"]
    size_small = ms["size"] * CAP_SMALL / ms["h"]
    W = mb["w"] * size_big / mb["size"]
    left_big = mb["left"] * size_big / mb["size"]
    Wn = ms["w"] * size_small / ms["size"]
    left_small = ms["left"] * size_small / ms["size"]
    top_big = mb["top"] * size_big / mb["size"]   # negative
    top_small = ms["top"] * size_small / ms["size"]

    if variant == "light":
        bg, mark, ink, rule = CREAM, TEAL, INK, TEAL
    elif variant == "dark":
        bg, mark, ink, rule = NAVY, TEAL_DARK, INK_DARK, TEAL_DARK
    elif variant == "mono":
        bg, mark, ink, rule = None, TEAL, TEAL, TEAL
    elif variant == "mono_dark":
        bg, mark, ink, rule = None, INK_DARK, INK_DARK, INK_DARK

    block_h = CAP_BIG + GAP + CAP_SMALL
    if not stacked:
        pad = 24
        gap_mark = 30
        tx = pad + MARK_W + gap_mark
        ty = pad + (MARK_H - block_h) / 2
        total_w = tx + W + pad
        total_h = MARK_H + 2 * pad
        mark_tf = f"translate({pad+34},{pad+46})"
    else:
        pad = 28
        gap_mark = 26
        total_w = max(W, MARK_W) + 2 * pad
        total_h = pad + MARK_H + gap_mark + block_h + pad
        tx = (total_w - W) / 2
        ty = pad + MARK_H + gap_mark
        mark_tf = f"translate({total_w/2},{pad+46})"

    big_y = ty - top_big
    small_y = ty + CAP_BIG + GAP - top_small
    rule_y = ty + CAP_BIG + GAP + CAP_SMALL / 2
    nx = tx + (W - Wn) / 2
    r1 = (tx, nx - RULE_GAP)
    r2 = (nx + Wn + RULE_GAP, tx + W)

    fill_ink = ink
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w:.2f} {total_h:.2f}">']
    if bg:
        svg.append(f'<rect width="{total_w:.2f}" height="{total_h:.2f}" fill="{bg}"/>')
    svg.append(f'<path d="{MARK}" fill="{mark}" transform="{mark_tf}"/>')
    svg.append(f'<text id="big" x="{tx-left_big:.3f}" y="{big_y:.3f}" font-family="{family}" font-weight="{wb}" '
               f'font-size="{size_big:.3f}" letter-spacing="{lsb*size_big:.3f}" fill="{fill_ink}">PLAYWORKS</text>')
    svg.append(f'<text id="small" x="{nx-left_small:.3f}" y="{small_y:.3f}" font-family="{family}" font-weight="{ws}" '
               f'font-size="{size_small:.3f}" letter-spacing="{lss*size_small:.3f}" fill="{fill_ink}">NORTH</text>')
    svg.append(f'<path d="M{r1[0]:.2f},{rule_y:.2f} H{r1[1]:.2f} M{r2[0]:.2f},{rule_y:.2f} H{r2[1]:.2f}" '
               f'stroke="{rule}" stroke-width="{RULE_W}" fill="none"/>')
    svg.append("</svg>")
    name = f"{fkey}_{'stacked' if stacked else 'horizontal'}_{variant}"
    path = os.path.join(OUT, name + ".svg")
    plain, bb = text_to_paths("\n".join(svg), path + ".tmp.svg")
    # Rebuild a clean SVG: replace the two text elements with their outlined groups.
    big = extract_group(plain, "big")
    small = extract_group(plain, "small")
    clean = []
    for line in svg:
        if line.startswith('<text id="big"'):
            clean.append(f'<g fill="{fill_ink}">{big}</g>')
        elif line.startswith('<text id="small"'):
            clean.append(f'<g fill="{fill_ink}">{small}</g>')
        else:
            clean.append(line)
    open(path, "w").write("\n".join(clean))
    os.remove(path + ".tmp.svg"); os.remove(path + ".tmp.svg.src.svg")
    return path, total_w, total_h

if __name__ == "__main__":
    keys = sys.argv[2].split(",") if len(sys.argv) > 2 else list(FONTS)
    made = []
    for k in keys:
        for stacked in (False, True):
            for v in ("light", "dark", "mono", "mono_dark"):
                p, w, h = build(k, v, stacked)
                made.append((p, w, h))
                print(p, f"{w:.0f}x{h:.0f}")
    json.dump(made, open(os.path.join(OUT, "made.json"), "w"))
