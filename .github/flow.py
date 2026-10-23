"""Generates .github/flow.svg, the README animation: a top-down frame factory.

  python3 .github/flow.py .github/flow.svg

One 9 s loop: CS2 drops five frames on the belt, 1 s apart. Each rides past RAM and Convert
(where it turns into raw video) into the encoder's basket and stacks up. When all five are in,
the encoder works, takes the stack and puts out one MP4 clip, which slides into the tray.
"""
import sys

T = 9.0           # loop length, s
N = 5             # frames per clip
RIDE = 3.5        # s from CS2 to the basket
X0, XB = 120, 640  # CS2 station, basket centre
DX = XB - X0
RAM_X, CONV_X = 290, 460
ENC_AT, OUT_AT = 7.6, 8.1  # encoder starts; the clip comes out


def pc(t):
    return f"{100 * t / T:.2f}%"


def frame_css(k):
    t0 = k * 1.0
    arrive = t0 + RIDE
    sx, sy = k * 3, -k * 3  # its place in the stack
    conv = t0 + RIDE * (CONV_X - X0) / DX
    k_ride = f"""
    @keyframes ride{k} {{
      0%, {pc(t0)} {{ transform: translate(0, -22px); opacity: 0; }}
      {pc(t0 + .3)} {{ transform: translate({DX * .3 / RIDE:.1f}px, 0); opacity: 1; }}
      {pc(arrive)} {{ transform: translate({DX}px, 0); opacity: 1; }}
      {pc(arrive + .2)}, {pc(OUT_AT - .1)} {{ transform: translate({DX + sx}px, {sy}px); opacity: 1; }}
      {pc(OUT_AT + .2)}, 100% {{ transform: translate({DX + 80}px, 0) scale(.4); opacity: 0; }}
    }}
    @keyframes tga{k} {{ 0%, {pc(conv)} {{ opacity: 1; }} {pc(conv + .01)}, 100% {{ opacity: 0; }} }}
    @keyframes raw{k} {{ 0%, {pc(conv)} {{ opacity: 0; }} {pc(conv + .01)}, 100% {{ opacity: 1; }} }}
    .f{k} {{ animation: ride{k} {T}s linear infinite; }}
    .f{k} .tga {{ animation: tga{k} {T}s linear infinite; }}
    .f{k} .raw {{ animation: raw{k} {T}s linear infinite; }}"""
    return k_ride


def flashes(name, times):
    """keyframes that flash on at each time for 0.25 s."""
    steps = ["0% { opacity: 0; }"]
    for t in times:
        steps.append(f"{pc(t)} {{ opacity: 1; }} {pc(t + .25)} {{ opacity: 0; }}")
    steps.append("100% { opacity: 0; }")
    return f"@keyframes {name} {{ {' '.join(steps)} }}"


def css():
    out = [frame_css(k) for k in range(N)]
    out.append(flashes("lamp1", [k * 1.0 for k in range(N)]))
    out.append(flashes("lamp2", [k + RIDE * (RAM_X - X0) / DX for k in range(N)]))
    out.append(flashes("lamp3", [k + RIDE * (CONV_X - X0) / DX for k in range(N)]))
    # the encoder's gauge: one step per frame in the basket
    g = ["0% { transform: scaleX(0); }"]
    for k in range(N):
        a = k + RIDE
        g.append(f"{pc(a)} {{ transform: scaleX({k / N:.2f}); }} {pc(a + .15)} {{ transform: scaleX({(k + 1) / N:.2f}); }}")
    g.append(f"{pc(OUT_AT)} {{ transform: scaleX(1); }} {pc(OUT_AT + .3)}, 100% {{ transform: scaleX(0); }}")
    out.append(f"@keyframes gauge {{ {' '.join(g)} }}")
    out.append(f"@keyframes work {{ 0%, {pc(ENC_AT)} {{ opacity: 0; }} {pc(ENC_AT + .05)}, {pc(OUT_AT + .1)} {{ opacity: 1; }} {pc(OUT_AT + .2)}, 100% {{ opacity: 0; }} }}")
    out.append(f"""@keyframes eject {{
      0%, {pc(OUT_AT)} {{ transform: translate(0, 0); opacity: 0; }}
      {pc(OUT_AT + .1)} {{ opacity: 1; }}
      {pc(T - .3)} {{ transform: translate(52px, 0); opacity: 1; }}
      100% {{ transform: translate(52px, 0); opacity: 0; }}
    }}""")
    out.append(f"@keyframes rec {{ 0%, {pc(N)} {{ opacity: 1; }} {pc(N + .01)}, 100% {{ opacity: .15; }} }}")
    return "\n".join(out)


def frame(k):
    return f'''<g class="f f{k}">
      <ellipse class="glow" rx="38" ry="24"/>
      <g class="tga"><rect class="card" x="-20" y="-14" width="40" height="28" rx="2"/><path class="thin" d="M-16,8 L-6,3 L2,6 L16,-2 M8,-10 v8 M4,-6 h8"/></g>
      <g class="raw"><rect class="card" x="-20" y="-14" width="40" height="28" rx="2"/><path class="thin" d="M-15,-7 H15 M-15,0 H15 M-15,7 H15"/></g>
    </g>'''


STYLE = """
    /* Auto Tournament's Ember palette: dark first, a warm light version for light mode */
    .bg { fill: #faf6f4; }
    .dot { fill: #e6dcd8; }
    .ln, .m, .slot, .scr, .card, .clip, .arm, .tray, .roll, .stick, .belt { stroke: #2a2220; stroke-width: 1.2; stroke-linejoin: round; }
    .m, .scr, .slot, .card, .clip { fill: #ffffff; }
    .stick, .arm, .tray, .roll, .belt { fill: #f1e9e6; }
    .tread { stroke: #2a2220; stroke-opacity: .3; stroke-width: 44; stroke-dasharray: 1.2 10.8; fill: none; animation: belt .08s linear infinite; }
    .thin { fill: none; stroke: #2a2220; stroke-width: 1; stroke-linecap: round; }
    .t { fill: #2a2220; font-size: 12px; font-weight: 700; letter-spacing: 1px; }
    .s { fill: #6b625f; font-size: 10.5px; }
    .k { fill: #2a2220; font-size: 9px; }
    .num { fill: #ffffff; font-size: 10px; font-weight: 700; }
    .badge, .acc { fill: #d1512c; }
    .pipe { fill: none; stroke: #e6dcd8; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; }
    .audio { fill: none; stroke: #d1512c; stroke-width: 2; stroke-dasharray: 2 8; stroke-linecap: round; animation: flow .5s linear infinite; }
    .ledo, .gbg { fill: #e6dcd8; }
    .play { fill: #d1512c; }
    .glow { fill: url(#glow); }
    .rec { fill: #1f9d4c; }
    @media (prefers-color-scheme: dark) {
      .bg { fill: #100908; }
      .dot { fill: #322926; }
      .ln, .m, .slot, .scr, .card, .clip, .arm, .tray, .roll, .stick, .belt { stroke: #c4bcb9; stroke-opacity: .85; }
      .m, .scr, .slot, .card, .clip { fill: #100908; }
      .stick, .arm, .tray, .roll, .belt { fill: #18110e; }
      .tread, .thin { stroke: #c4bcb9; }
      .t, .k { fill: #f4edeb; }
      .s { fill: #938a87; }
      .badge, .acc, .play { fill: #ff6a3d; }
      .num { fill: #140e0c; }
      .pipe { stroke: #211815; }
      .audio { stroke: #ff6a3d; }
      .ledo, .gbg { fill: #322926; }
      .rec { fill: #3fc168; }
    }
    @keyframes belt { to { stroke-dashoffset: -12; } }
    @keyframes flow { to { stroke-dashoffset: -10; } }
    @keyframes spin { to { transform: rotate(360deg); } }
    .dial { transform-box: fill-box; transform-origin: center; animation: spin 3s linear infinite; }
    .lamp1, .lamp2, .lamp3 { opacity: 0; }
    .lamp1 { animation: lamp1 9s linear infinite; } .lamp2 { animation: lamp2 9s linear infinite; } .lamp3 { animation: lamp3 9s linear infinite; }
    .gauge { transform-box: fill-box; transform-origin: left; transform: scaleX(0); animation: gauge 9s linear infinite; }
    .work { opacity: 0; animation: work 9s linear infinite; }
    .eject { opacity: 0; animation: eject 9s linear infinite; }
    .rec { animation: rec 9s steps(1) infinite; }
"""


def svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 290" width="900" height="290" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <title>Frame by Frame: CS2 renders each frame; the frames are collected, then encoded into one clip</title>
  <!-- generated by .github/flow.py: one 9 s loop, five frames make one clip -->
  <style>{STYLE}{css()}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .f, .eject, .work {{ opacity: 0; }} }}
  </style>
  <defs>
    <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse"><circle class="dot" cx="1" cy="1" r="1"/></pattern>
    <radialGradient id="glow"><stop offset="0" stop-color="#ff6a3d" stop-opacity=".45"/><stop offset="1" stop-color="#ff6a3d" stop-opacity="0"/></radialGradient>
  </defs>

  <rect class="bg" width="900" height="290" rx="12"/>
  <rect width="900" height="290" rx="12" fill="url(#grid)"/>

  <!-- game audio: CS2's WAV, piped along the top to the encoder -->
  <path class="pipe" d="M150,52 V26 H750 V132"/>
  <path class="audio" d="M150,52 V26 H750 V132"/>
  <text class="s" x="450" y="20" text-anchor="middle">game audio (WAV)</text>

  <!-- arms out over the belt -->
  <rect class="arm" x="113" y="118" width="14" height="40" rx="2"/>
  <rect class="arm" x="283" y="118" width="14" height="40" rx="2"/>
  <rect class="arm" x="453" y="118" width="14" height="40" rx="2"/>

  <!-- 1 CS2 -->
  <rect class="m" x="70" y="52" width="100" height="70" rx="6"/>
  <rect class="scr" x="80" y="62" width="64" height="42" rx="2"/>
  <path class="thin" d="M84,94 L98,86 L110,90 L140,76 M124,68 v10 M119,73 h10"/>
  <circle class="rec" cx="158" cy="64" r="3.5"/>
  <text class="k" x="80" y="116">REC</text>

  <!-- 2 RAM -->
  <rect class="m" x="235" y="52" width="110" height="70" rx="6"/>
  {"".join(f'<rect class="stick" x="{245 + i * 13}" y="60" width="9" height="54" rx="1"/>' for i in range(7))}

  <!-- 3 Convert -->
  <rect class="m" x="410" y="52" width="100" height="70" rx="6"/>
  <g class="dial">
    <circle class="ln" cx="460" cy="85" r="24" fill="none"/>
    <circle class="thin" cx="460" cy="85" r="18" stroke-width="4" stroke-dasharray="1 4.65"/>
    <path class="thin" d="M460,85 L460,65"/>
  </g>
  <circle class="ln" cx="460" cy="85" r="5" fill="none"/>

  <!-- the belt -->
  <rect class="belt" x="60" y="152" width="530" height="48" rx="6"/>
  <path class="tread" d="M66,176 H584"/>
  <rect class="roll" x="54" y="148" width="10" height="56" rx="3"/>
  <rect class="roll" x="586" y="148" width="10" height="56" rx="3"/>

  <!-- 4 the encoder's basket, then the encoder -->
  <rect class="tray" x="602" y="138" width="80" height="76" rx="6"/>
  <text class="k" x="642" y="133" text-anchor="middle">frames</text>
  <path class="thin" d="M684,176 H698 M692,171 L698,176 L692,181"/>
  <rect class="m" x="700" y="132" width="100" height="88" rx="6"/>
  <rect class="slot" x="709" y="142" width="26" height="30" rx="2"/>
  <rect class="slot" x="737" y="142" width="26" height="30" rx="2"/>
  <rect class="slot" x="765" y="142" width="26" height="30" rx="2"/>
  <text class="k" x="722" y="184" font-size="7.5" text-anchor="middle">AV1</text>
  <text class="k" x="750" y="184" font-size="7.5" text-anchor="middle">H.265</text>
  <text class="k" x="778" y="184" font-size="7.5" text-anchor="middle">H.264</text>
  <rect class="gbg" x="709" y="196" width="82" height="8" rx="2"/>
  <rect class="acc gauge" x="709" y="196" width="82" height="8" rx="2"/>
  <rect class="acc work" x="709" y="142" width="26" height="30" rx="2" opacity=".85"/>

  <!-- 5 the clip tray -->
  <rect class="tray" x="824" y="138" width="66" height="76" rx="6"/>
  <rect class="clip" x="837" y="150" width="40" height="26" rx="3"/>
  <rect class="clip" x="837" y="158" width="40" height="26" rx="3"/>
  <path class="play" d="M852,165 L852,177 L862,171 z"/>
  <g class="eject"><rect class="clip" x="785" y="176" width="40" height="26" rx="3"/><path class="play" d="M800,183 L800,195 L810,189 z"/></g>

  <!-- frames -->
  <g transform="translate({X0},176)">
    {"".join(frame(k) for k in range(N))}
  </g>

  <!-- lamps at the arm ends (over the frames) -->
  <circle class="ledo" cx="120" cy="152" r="4"/><circle class="acc lamp1" cx="120" cy="152" r="4"/>
  <circle class="ledo" cx="290" cy="152" r="4"/><circle class="acc lamp2" cx="290" cy="152" r="4"/>
  <circle class="ledo" cx="460" cy="152" r="4"/><circle class="acc lamp3" cx="460" cy="152" r="4"/>

  <!-- steps -->
  <circle class="badge" cx="80" cy="234" r="8"/><text class="num" x="80" y="238" text-anchor="middle">1</text>
  <text class="t" x="94" y="238">RENDER</text><text class="s" x="94" y="253">CS2, frame by frame</text>
  <circle class="badge" cx="250" cy="234" r="8"/><text class="num" x="250" y="238" text-anchor="middle">2</text>
  <text class="t" x="264" y="238">RAM</text><text class="s" x="264" y="253">TGA in /dev/shm</text>
  <circle class="badge" cx="420" cy="234" r="8"/><text class="num" x="420" y="238" text-anchor="middle">3</text>
  <text class="t" x="434" y="238">CONVERT</text><text class="s" x="434" y="253">TGA to raw video</text>
  <circle class="badge" cx="612" cy="234" r="8"/><text class="num" x="612" y="238" text-anchor="middle">4</text>
  <text class="t" x="626" y="238">ENCODE</text><text class="s" x="626" y="253">all frames + audio</text>
  <circle class="badge" cx="790" cy="234" r="8"/><text class="num" x="790" y="238" text-anchor="middle">5</text>
  <text class="t" x="804" y="238">CLIP</text><text class="s" x="804" y="253">one MP4</text>
  <text class="s" x="450" y="280" text-anchor="middle">Each frame takes as long as the GPU needs, so a slow GPU makes the same clip as a fast one. It just takes longer.</text>
</svg>
'''


if __name__ == "__main__":
    open(sys.argv[1], "w").write(svg())
