"""Generates .github/flow.svg, the README animation: who hands what to whom.

  python3 .github/flow.py .github/flow.svg

A belt between every pair of processes. The recorder sends CS2 its commands; CS2 renders a
frame at a time onto the belt to RAM, which queues them; Convert takes them one by one (its
light shows STOP while it works, GO when it's ready for the next) and drops each into a
basket; Encode picks each out and adds it to the end of the clip's stack. When the clip's
frames are all in, Encode puts out one MP4 for the platform. Game audio has its own belt.

The timings are simulated below, so edit this script, not the SVG.
"""
import sys

N = 5              # frames in the clip
RENDER = 0.75      # s between frames out of CS2: faster than Convert, so RAM queues
RIDE = 0.45        # s along a belt
CONV = 1.0         # s Convert works on one frame
FIRST = 1.2        # the first frame leaves CS2

# where things are (centres of a frame card); seen from above, a piece rides on the belt's centre line
BELT_Y = 151
CS2_OUT, RAM_IN = (366, BELT_Y), (414, BELT_Y)
QUEUE_Y, QUEUE_X0, QUEUE_DX = 158, 562, 27   # slot 0 (next out) is the rightmost
CONV_IN, CONV_END, CONV_AT = (600, BELT_Y), (652, BELT_Y), (752, 158)
CHUTE_TOP, BASKET_Y = (768, 222), 300
BASKET_X = [748, 786, 822, 762, 806]
STACK_X, STACK_Y0, STACK_DY = 947, 300, 13
CLIP_FROM, CLIP_TO = (1078, BELT_Y), (1160, 168)
# belts, and the audio along its belt, run as fast as the pieces ride
SPEED = (RAM_IN[0] - CS2_OUT[0]) / RIDE   # px/s
DASH = 16                                 # px between treads


def simulate():
    frames, conv_free = [], 0.0
    for k in range(N):
        emit = FIRST + k * RENDER
        queued = emit + RIDE + .2
        start = max(queued, conv_free)
        at_conv = start + .2 + RIDE + .2
        done = at_conv + CONV
        conv_free = done + .2
        landed = conv_free + .35
        picked = landed + .45
        stacked = picked + .45
        frames.append(dict(emit=emit, queued=queued, start=start, at_conv=at_conv, done=done,
                           chute=conv_free, landed=landed, picked=picked, stacked=stacked))
    return frames


F = simulate()
ENC = F[-1]["stacked"] + .25          # the encoder starts on the whole clip
OUT = ENC + .9                        # the MP4 comes out
ARRIVE = OUT + .7                     # it reaches the platform
T = round(ARRIVE + 1.3, 2)            # one loop


def pc(t):
    return f"{100 * min(max(t, 0), T) / T:.3f}%"


def keyframes(name, pts):
    """pts: [(t, css)], held between points; the first and last are held to 0% and 100%."""
    pts = sorted(pts, key=lambda p: p[0])
    body = [f"0% {{ {pts[0][1]} }}"] + [f"{pc(t)} {{ {css} }}" for t, css in pts] + [f"100% {{ {pts[-1][1]} }}"]
    return f"@keyframes {name} {{ {' '.join(body)} }}"


def at(x, y):
    return f"transform: translate({x}px, {y}px);"


def queue_slot(k, t):
    """frame k's place in RAM's queue at time t: how many earlier frames are still waiting."""
    return sum(1 for j in range(k) if F[j]["queued"] <= t < F[j]["start"])


def frame_css(k):
    f = F[k]
    pos = [(f["emit"], at(*CS2_OUT)), (f["emit"] + RIDE, at(*RAM_IN)),
           (f["queued"], at(QUEUE_X0 - QUEUE_DX * queue_slot(k, f["queued"]), QUEUE_Y))]
    # shuffle right as earlier frames leave the queue
    for j in range(k):
        m = F[j]["start"]
        if f["queued"] < m < f["start"]:
            pos.append((m, at(QUEUE_X0 - QUEUE_DX * queue_slot(k, m - .01), QUEUE_Y)))
            pos.append((m + .2, at(QUEUE_X0 - QUEUE_DX * queue_slot(k, m + .01), QUEUE_Y)))
    pos.append((f["start"], at(QUEUE_X0, QUEUE_Y)))
    pos += [(f["start"] + .2, at(*CONV_IN)), (f["start"] + .2 + RIDE, at(*CONV_END)),
            (f["at_conv"], at(*CONV_AT)), (f["done"], at(*CONV_AT)),
            (f["chute"], at(*CHUTE_TOP)), (f["landed"], at(BASKET_X[k], BASKET_Y)),
            (f["picked"], at(BASKET_X[k], BASKET_Y)), (f["stacked"], at(STACK_X, STACK_Y0 - STACK_DY * k)),
            (OUT, at(STACK_X, STACK_Y0 - STACK_DY * k))]
    vis = [(0, "opacity: 0;"), (f["emit"], "opacity: 0;"), (f["emit"] + .1, "opacity: 1;"),
           (OUT - .3, "opacity: 1;"), (OUT, "opacity: 0;")]
    tga = [(0, "opacity: 1;"), (f["done"] - .01, "opacity: 1;"), (f["done"], "opacity: 0;")]
    raw = [(0, "opacity: 0;"), (f["done"] - .01, "opacity: 0;"), (f["done"], "opacity: 1;"),
           (f["stacked"] - .01, "opacity: 1;"), (f["stacked"], "opacity: 0;")]
    bar = [(0, "opacity: 0;"), (f["stacked"] - .01, "opacity: 0;"), (f["stacked"], "opacity: 1;")]
    return "\n    ".join([
        keyframes(f"p{k}", pos), keyframes(f"v{k}", vis),
        keyframes(f"t{k}", tga), keyframes(f"r{k}", raw), keyframes(f"b{k}", bar),
        f".f{k} {{ animation: p{k} {T}s linear infinite; }}",
        f".f{k} > g {{ animation: v{k} {T}s linear infinite; }}",
        f".f{k} .tga {{ animation: t{k} {T}s linear infinite; }}",
        f".f{k} .raw {{ animation: r{k} {T}s linear infinite; }}",
        f".f{k} .bar {{ animation: b{k} {T}s linear infinite; }}",
    ])


def flash(name, spans, on="opacity: 1;", off="opacity: 0;"):
    pts = [(0, off)]
    for a, b in spans:
        pts += [(a - .01, off), (a, on), (b, on), (b + .01, off)]
    return keyframes(name, pts)


def css():
    out = [frame_css(k) for k in range(N)]
    out.append(flash("stop", [(F[k]["at_conv"], F[k]["done"]) for k in range(N)]))
    go = [(0, F[0]["at_conv"] - .02)] + [(F[k]["done"] + .02, F[k + 1]["at_conv"] - .02) for k in range(N - 1)]
    go.append((F[-1]["done"] + .02, T - .02))
    out.append(flash("go", go))
    out.append(flash("emit", [(F[k]["emit"] - .15, F[k]["emit"] + .1) for k in range(N)]))
    out.append(flash("enc", [(ENC, OUT)]))
    out.append(flash("play", [(ARRIVE, T - .2)]))
    out.append(keyframes("seek", [(0, "opacity: 0; " + at(186, BELT_Y)), (.15, "opacity: 1; " + at(186, BELT_Y)),
                                  (.75, "opacity: 1; " + at(214, BELT_Y)), (.9, "opacity: 0; " + at(218, BELT_Y))]))
    out.append(keyframes("clip", [(0, "opacity: 0; " + at(*CLIP_FROM)), (OUT - .01, "opacity: 0; " + at(*CLIP_FROM)),
                                  (OUT, "opacity: 1; " + at(*CLIP_FROM)), (ARRIVE, "opacity: 1; " + at(*CLIP_TO)),
                                  (T - .2, "opacity: 1; " + at(*CLIP_TO)), (T, "opacity: 0; " + at(*CLIP_TO))]))
    run = DASH / SPEED
    out.append(f"@keyframes belt {{ to {{ stroke-dashoffset: -{DASH}; }} }} @keyframes beltv {{ to {{ stroke-dashoffset: {DASH}; }} }}")
    out.append(f".tread, .audio {{ animation: belt {run:.3f}s linear infinite; }} .treadv {{ animation-name: beltv; }}")
    out.append(f".stop {{ animation: stop {T}s linear infinite; }} .go {{ animation: go {T}s linear infinite; }}")
    out.append(f".emit {{ animation: emit {T}s linear infinite; }} .enc {{ animation: enc {T}s linear infinite; }}")
    out.append(f".playon {{ animation: play {T}s linear infinite; }}")
    out.append(f".seek {{ animation: seek {T}s linear infinite; }} .clipm {{ animation: clip {T}s linear infinite; }}")
    return "\n    ".join(out)


STYLE = """
    /* Ready Up's colours, from its grenade logo: blue on near-black, with a light version */
    .bg { fill: #f5f6f8; }
    .dot { fill: #dcdfe5; }
    .box { fill: #ffffff; stroke: #1d1d1f; stroke-width: 1.5; }
    .hot { stroke: #2f6bff; }
    .belt { fill: #eceef2; stroke: #1d1d1f; stroke-width: 1.5; }
    .tread { fill: none; stroke: #1d1d1f; stroke-opacity: .28; stroke-dasharray: 4 12; }
    .slot { fill: none; stroke: #939291; stroke-dasharray: 3 3; }
    .h { fill: #1d1d1f; font-size: 13px; font-weight: 700; }
    .s { fill: #5d5b5b; font-size: 10px; }
    .x { fill: #1d1d1f; font-size: 9px; }
    .acc { fill: #2f6bff; }
    .acct { fill: #16398f; font-size: 9px; }
    .chip { fill: none; stroke: #939291; } .chipa { fill: none; stroke: #2f6bff; }
    .lamp { fill: #dcdfe5; } .red { fill: #d93a32; } .grn { fill: #1f9d4c; }
    .tga1 { fill: #6f93b8; } .tga2 { fill: #9b7a52; } .edge { fill: none; stroke: #1d1d1f; stroke-width: 1; }
    .rawf { fill: #ffffff; } .rawl { stroke: #2f6bff; stroke-width: 1.6; }
    .barf { fill: #eceef2; stroke: #1d1d1f; stroke-width: 1; }
    .basket { fill: none; stroke: #1d1d1f; stroke-width: 1.5; }
    .hatch { stroke: #dcdfe5; }
    .wave { fill: none; stroke: #2f6bff; stroke-width: 1.6; }
    .audio { fill: none; stroke: #2f6bff; stroke-width: 2; stroke-dasharray: 3 13; stroke-linecap: round; }
    .glow { fill: url(#glow); }
    @media (prefers-color-scheme: dark) {
      .bg { fill: #131315; }
      .dot { fill: #282828; }
      .box { fill: #1d1d1f; stroke: #c7c4c3; }
      .hot { stroke: #6b95ff; }
      .edge { stroke: #c7c4c3; }
      .belt { fill: #282828; stroke: #c7c4c3; }
      .tread { stroke: #c7c4c3; }
      .slot, .chip { stroke: #4d4d4d; }
      .h, .x { fill: #f4f4f5; }
      .s { fill: #939291; }
      .acc { fill: #6b95ff; } .acct { fill: #6b95ff; }
      .chipa, .rawl, .wave, .audio { stroke: #6b95ff; }
      .lamp { fill: #2a2929; } .red { fill: #f2645f; } .grn { fill: #3fc168; }
      .rawf { fill: #282828; }
      .barf { fill: #282828; stroke: #c7c4c3; }
      .basket { stroke: #c7c4c3; }
      .hatch { stroke: #282828; }
    }
"""


def box(x, y, w, h, hot=False):
    return f'<rect class="box{" hot" if hot else ""}" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>'


def hbelt(x, y, w, h=18):
    return (f'<rect class="belt" x="{x}" y="{y}" width="{w}" height="{h}"/>'
            f'<path class="tread" stroke-width="{h - 4}" d="M{x},{y + h / 2} H{x + w}"/>')


def vbelt(x, y, h, w=16, up=False):
    """a vertical belt; it runs down unless up."""
    return (f'<rect class="belt" x="{x}" y="{y}" width="{w}" height="{h}"/>'
            f'<path class="tread{" treadv" if up else ""}" stroke-width="{w - 4}" d="M{x + w / 2},{y} V{y + h}"/>')


def card():
    return ('<g class="tga"><rect class="tga1" x="-11" y="-8" width="22" height="9"/><rect class="tga2" x="-11" y="1" width="22" height="7"/>'
            '<rect class="edge" x="-11" y="-8" width="22" height="16" rx="1.5"/></g>'
            '<g class="raw"><rect class="rawf" x="-11" y="-8" width="22" height="16" rx="1.5"/>'
            '<path class="rawl" d="M-8,-4 H8 M-8,0 H8 M-8,4 H8"/><rect class="edge" x="-11" y="-8" width="22" height="16" rx="1.5"/></g>'
            '<g class="bar"><rect class="barf" x="-30" y="-5" width="60" height="10" rx="2"/></g>')


def label(x, y, text, cls="s", anchor="middle"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>'


def svg():
    o = []
    # belts first, so the boxes sit over their ends
    o.append(hbelt(170, 142, 60) + label(200, 118, "commands", "x"))
    o.append(hbelt(360, 142, 60) + label(390, 118, "a frame", "x"))
    o.append(hbelt(590, 142, 70) + label(625, 118, "one by one", "x"))
    o.append(vbelt(760, 206, 54))
    o.append(hbelt(1070, 142, 40) + label(1090, 118, "mp4", "acct"))
    # audio: CS2 down, along the bottom, up into Encode
    o.append(vbelt(287, 206, 150) + hbelt(287, 356, 700, 16) + vbelt(971, 326, 30, up=True))
    o.append('<path class="audio" d="M295,206 V364 H979 V326"/>')
    o.append('<path class="wave" d="M330,344 C333,337 335,337 338,344 S343,351 346,344 S351,337 354,344 S359,351 362,344"/>')
    o.append(label(370, 347, "game audio (WAV), from CS2 to the encoder", "acct", "start"))

    o.append(box(40, 96, 130, 110) + label(52, 118, "RECORDER", "h", "start")
             + label(52, 138, "drives the game", "s", "start") + label(52, 152, "over its console", "s", "start"))
    o.append(box(230, 96, 130, 110) + label(242, 118, "CS2", "h", "start")
             + label(242, 138, "renders one frame", "s", "start") + label(242, 152, "at a time, at its", "s", "start")
             + label(242, 166, "own pace", "s", "start")
             + '<circle class="lamp" cx="344" cy="114" r="4"/><circle class="grn emit" cx="344" cy="114" r="4"/>')
    o.append(box(420, 96, 170, 110) + label(432, 118, "RAM", "h", "start") + label(432, 190, "queue · oldest out first", "s", "start"))
    o += [f'<rect class="slot" x="{QUEUE_X0 - QUEUE_DX * i - 11}" y="{QUEUE_Y - 8}" width="22" height="16" rx="1.5"/>' for i in range(5)]
    o.append(box(660, 96, 150, 110) + label(700, 118, "CONVERT", "h", "start") + label(700, 138, "TGA to", "s", "start")
             + label(700, 152, "raw video", "s", "start"))
    o.append('<rect class="box" x="668" y="104" width="24" height="58" rx="6"/>'
             '<circle class="lamp" cx="680" cy="121" r="6"/><circle class="red stop" cx="680" cy="121" r="6"/>'
             '<circle class="lamp" cx="680" cy="145" r="6"/><circle class="grn go" cx="680" cy="145" r="6"/>')
    o.append(label(680, 178, "STOP·GO", "x"))
    # the basket
    o.append('<path class="basket" d="M720,256 V312 Q720,326 734,326 H846 Q860,326 860,312 V256"/>')
    o += [f'<path class="hatch" d="M{x},258 L{x + 60},322"/>' for x in range(722, 800, 14)]
    o.append(label(790, 342, "basket of raw frames"))
    # the encoder
    o.append(box(900, 96, 170, 230, hot=True) + label(912, 118, "ENCODE", "h", "start"))
    o.append('<rect class="chipa" x="912" y="128" width="30" height="16" rx="3"/><rect class="acc enc" x="912" y="128" width="30" height="16" rx="3" opacity=".35"/>'
             '<rect class="chip" x="946" y="128" width="40" height="16" rx="3"/><rect class="chip" x="990" y="128" width="40" height="16" rx="3"/>'
             + label(927, 139, "AV1", "acct") + label(966, 139, "H.265", "s") + label(1010, 139, "H.264", "s"))
    o.append(label(912, 166, "the clip so far", "s", "start"))
    o.append(label(985, 236, "each new frame", "s", "start") + label(985, 248, "goes on top", "s", "start"))
    # the platform
    o.append(box(1110, 96, 100, 110) + label(1122, 118, "PLATFORM", "h", "start")
             + '<rect class="box hot" x="1122" y="150" width="76" height="40" rx="5"/>'
             + '<path class="acc" d="M1155,163 L1155,177 L1167,170 z"/>'
             + '<rect class="acc playon" x="1122" y="150" width="76" height="40" rx="5" opacity=".25"/>')

    # the moving pieces
    o.append('<g class="seek"><rect class="box" x="-14" y="-8" width="28" height="14" rx="3"/>'
             '<text class="x" x="0" y="2" text-anchor="middle" font-size="8">seek</text></g>')
    o += [f'<g class="f{k}"><g><ellipse class="glow" rx="22" ry="14"/>{card()}</g></g>' for k in range(N)]
    o.append('<g class="clipm"><ellipse class="glow" rx="26" ry="16"/><rect class="box hot" x="-14" y="-10" width="28" height="20" rx="3"/>'
             '<path class="acc" d="M-4,-5 L-4,5 L5,0 z"/></g>')

    o.append(label(40, 404, "A slow GPU fills the belts slower, never with worse frames.", "s", "start"))
    moving = ", ".join(f".f{k} > g" for k in range(N))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 420" width="1240" height="420" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <title>Frame by Frame: who hands what to whom, from the recorder's commands to one MP4 on the platform</title>
  <!-- generated by .github/flow.py: edit the script, not this file -->
  <style>{STYLE}
    {css()}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .seek, .clipm, {moving}, .stop, .enc, .playon, .emit {{ opacity: 0; }} }}
  </style>
  <defs>
    <pattern id="grid" width="18" height="18" patternUnits="userSpaceOnUse"><circle class="dot" cx="1" cy="1" r="1"/></pattern>
    <radialGradient id="glow"><stop offset="0" stop-color="#2f6bff" stop-opacity=".5"/><stop offset="1" stop-color="#2f6bff" stop-opacity="0"/></radialGradient>
  </defs>
  <rect class="bg" width="1240" height="420" rx="14"/>
  <rect width="1240" height="420" rx="14" fill="url(#grid)"/>
  <text class="s" x="40" y="44" letter-spacing="2">FRAME BY FRAME · WHO HANDS WHAT TO WHOM</text>
  {"".join(o)}
</svg>
'''


if __name__ == "__main__":
    open(sys.argv[1], "w").write(svg())
    print(f"loop {T}s;", " ".join(f"f{k}: out {f['emit']:.2f} conv {f['start']:.2f} stacked {f['stacked']:.2f}" for k, f in enumerate(F)))
