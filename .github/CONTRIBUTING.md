# Contributing to Frame by Frame

Frame by Frame is part of [Auto Tournament](https://github.com/Auto-Tournament). Docs live at **[docs.autotournament.gg](https://docs.autotournament.gg)**.

## Reporting bugs

[Open an issue](https://github.com/Auto-Tournament/frame-by-frame/issues/new/choose) with:

- your CS2 build (`version` in the game console) and the Frame by Frame release
- the `[Frame by Frame]` lines from the game console
- the relevant part of the console log

## Pull requests

1. Fork the repo and create a branch.
2. Build in the Steam Runtime sniper SDK (see the README) and run `ctest`.
3. Keep the engine surface as small as it is now. Anything new that touches the engine needs an identity check like the one in `src/strip.h`, so a CS2 update turns it off instead of calling the wrong code.
4. Open a pull request against `master`.

The [contribution rules](https://github.com/Auto-Tournament/.github/blob/main/CONTRIBUTING.md) apply to every PR: keep it small, say what you ran and what you saw, say if an AI tool wrote any of it (and read every line), and leave the UI and docs to the maintainer.

By contributing you agree to the [Auto Tournament CLA](https://github.com/Auto-Tournament/auto-tournament/blob/main/CLA.md), and your contribution is licensed under the [PolyForm Noncommercial License 1.0.0](../LICENSE).
