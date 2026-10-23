<div align="center">
  <img src=".github/logo-128.png" alt="Frame by Frame" width="96" />
  <h1>Frame by Frame</h1>
  <p><strong>A native CS2 plugin that records demos one frame at a time, on any GPU</strong></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg" alt="License: PolyForm Noncommercial 1.0.0" /></a>
    <a href="https://docs.autotournament.gg"><img src="https://img.shields.io/badge/docs-docs.autotournament.gg-blue" alt="Docs" /></a>
    <a href="https://discord.gg/n7gHYau7aW"><img src="https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white" alt="Discord" /></a>
  </p>
</div>

<br />

> [!CAUTION]
> **Early development.** Frame by Frame changes often. Expect breaking changes between releases.

Frame by Frame lets [Auto Tournament](https://github.com/Auto-Tournament/auto-tournament)'s highlight recorder export a CS2 demo as every single frame plus the game's own audio. The game renders each frame at its own pace, so a weak GPU or an iGPU gets the same clip as a fast one. It just takes longer. And because every frame is captured, you pick the frame rate: 60, 120 or 240 fps.

CS2 can already do this with `startmovie`, but the command is hidden in retail builds. Frame by Frame makes CS2 unhide it. That's all it does inside the game. The recorder drives everything else through the game console.

**No Metamod. No CounterStrikeSharp. No hooks.**

## Why it keeps working after CS2 updates

Frame by Frame loads straight into CS2 through a `gameinfo.gi` entry, then loads Valve's real server module and passes everything through, the same way [Ready Up](https://github.com/Auto-Tournament/ready-up) does. It patches nothing in the engine and hooks no functions.

It makes exactly one call: `ICvar::StripDevelopmentFlags()`, CS2's own function that unhides developer-only commands. Before calling it, the plugin checks that the function really is that one: its code must contain the flag mask it clears. If a CS2 update moves it, the check fails and the plugin logs it and does nothing. The game keeps running normally and only the movie commands stay hidden.

## How a recording works

1. The recorder adds `Game csgo/frame-by-frame` above `Game csgo` in `gameinfo.gi` and starts CS2 with `-insecure`.
2. The game console shows `[Frame by Frame] movie commands unhidden`.
3. Over the console, the recorder plays the demo, seeks with `demo_gototick <tick> 0 1`, sets `host_framerate`, runs `startmovie <name> tga wav` and resumes. At the end tick it runs `endmovie` (`demo_pauseatservertick` can pause there).
4. TGA frames land in `csgo/frame-by-frame/movie/<date>/` and the WAV in `csgo/movie/<date>/`.

## Install

The Auto Tournament recorder installs Frame by Frame on its own (in progress). To try it by hand, put a release's `frame-by-frame` folder in `game/csgo/`, add the line from step 1 to `gameinfo.gi` and start CS2 with `-insecure`.

## Build

Builds run in Valve's Steam Runtime "sniper" SDK, the same as CS2:

```bash
docker run --rm -v "$PWD:/src" -w /src registry.gitlab.steamos.cloud/steamrt/sniper/sdk:latest \
  sh -c 'cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build && cd build && ctest'
```

The plugin is `build/libserver.so`.

## Credits

Frame by Frame is inspired by the CS2 plugin in [CS Demo Manager](https://github.com/akiver/cs-demo-manager) by AkiVer, which showed that `startmovie` can be unlocked for frame-exact demo exports. Frame by Frame is our own code, written from scratch. None of CS Demo Manager's code is used.

Thanks to DaalbuCZ for trying CS Demo Manager's plugin with the Auto Tournament recorder ([#1054](https://github.com/Auto-Tournament/auto-tournament/pull/1054), [#1269](https://github.com/Auto-Tournament/auto-tournament/pull/1269)), which showed the edge cases a native recorder has to handle, like a `gameinfo.gi` left behind after a crash.

## Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md). Pull requests need the [Auto Tournament CLA](https://github.com/Auto-Tournament/auto-tournament/blob/main/CLA.md).

## License

[PolyForm Noncommercial License 1.0.0](LICENSE). Commercial use needs a license from Auto Tournament.
