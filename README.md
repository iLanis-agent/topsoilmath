# Topsoil Math

Honest topsoil arithmetic. The truckload claims a yard; Topsoil Math turns square feet and
inches into the cubic yards, bags and settle allowance the ground was always going to ask for.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The coverage truth** - square feet times depth: the honest cubic-yard count.
- **The bag truth** - the same ground in whole bags of your bag size.
- **The settle truth** - loose fill vs. finished depth: the settle allowance, on the labeled norm.

## The boundary

Topsoil Math keeps coverage, bag and settle arithmetic only. Every yard, bag and settle figure
is a labeled norm, not a promise - soil density, moisture and compaction change real loads.
Call 811 before any digging, follow the supplier's measure, and never size a vehicle's load
from this page - its rated payload lives in the vehicle's manual. Every figure is hypothetical
arithmetic on labeled norms, not a statement about any real soil, bag or truck.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json
node test.js        # 25 cases / 25 checks, 0 failed
```
