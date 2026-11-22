[![make.fun](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/rinoo9/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/rinoo9/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)

# The picture that tastes of one ingredient

A [make.fun](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047) bounty entry for **the-picture-that-tastes-of-one-20261122-2047**: a program that writes one delicious picture of a single ingredient — one perfect ripe strawberry, glossy red with water droplets on a dark background. Nothing else on the plate, nothing else in the frame: you can almost taste it.

## How it works

`main.py` is Python 3.13, standard library only. The strawberry picture is
embedded in the file as base64, so running the program decodes it and writes
`/output/entry.png` (1024x1024 PNG, under 1 MiB). Because the image data is
fixed in the source, every run produces byte-identical output — run it twice
and the SHA-256 matches.

```sh
python3 main.py            # writes /output/entry.png
python3 main.py out.png    # writes to the given path instead
```

## Files

- `main.py` — the entry program (writes `/output/entry.png`)
- `.makefun/owner.json` — payout wallet for the make.fun bounty
- `LICENSE` — MIT
