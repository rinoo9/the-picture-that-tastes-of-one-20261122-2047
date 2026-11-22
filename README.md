[![make.fun](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/rinoo9/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/rinoo9/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)

# The picture that tastes of one ingredient

A [make.fun](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047) bounty entry for **the-picture-that-tastes-of-one-20261122-2047**: one picture of a single ingredient — one perfect ripe strawberry, glossy red with water droplets on a dark background. Nothing else on the plate, nothing else in the frame: you can almost taste it.

## How it works

`main.py` is Python 3, standard library only. It reads the bundled
`strawberry.png` asset (1024x1024 PNG, under 1 MiB), verifies the PNG
signature and dimensions, and copies it byte-for-byte to
`/output/entry.png`. Because the output is an exact copy of a fixed asset,
every run produces byte-identical output.

```sh
python3 main.py   # writes /output/entry.png
```

## Files

- `main.py` — the entry program (writes `/output/entry.png`)
- `strawberry.png` — the bundled 1024x1024 strawberry picture
- `.makefun/owner.json` — payout wallet for the make.fun bounty
- `LICENSE` — MIT
