import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def cubic_feet(area, depth):
    if not (area > 0):
        raise ValueError("the area must be above zero")
    if not (depth > 0):
        raise ValueError("the depth must be above zero")
    return area * depth / 12

def coverage_truth(area, depth):
    cuft = cubic_feet(area, depth)
    yards = cuft / 27
    if yards <= 1:
        verdict = "a few wheelbarrows honestly"
    elif yards <= 5:
        verdict = "a small delivery honestly"
    elif yards <= 15:
        verdict = "a truckload honestly"
    else:
        verdict = "several truckloads honestly"
    rounded = math.floor(yards * 10 + 0.5) / 10
    return f"{area} {plural(area, 'square foot', 'square feet')} at {depth} {plural(depth, 'inch', 'inches')} is {fixed1(cuft)} cubic feet - {fixed1(yards)} cubic {plural(1 if rounded == 1 else 2, 'yard', 'yards')}, {verdict}."

def bag_truth(area, depth, bag):
    cuft = cubic_feet(area, depth)
    if not (bag > 0):
        raise ValueError("the bag size must be above zero")
    bags = math.ceil(cuft / bag - 1e-9)
    if bags <= 20:
        verdict = "a trunk of bags honestly"
    elif bags <= 80:
        verdict = "a pallet of bags honestly"
    elif bags <= 200:
        verdict = "a few pallets honestly"
    else:
        verdict = "many pallets honestly"
    bag_part = f"1 of the {bag}-cubic-foot bags" if bags == 1 else f"{bags} of the {bag}-cubic-foot bags"
    return f"{area} {plural(area, 'square foot', 'square feet')} at {depth} {plural(depth, 'inch', 'inches')} is {bag_part} - {verdict}."

def settle_truth(area, depth, settle):
    cuft = cubic_feet(area, depth)
    if not (settle >= 0):
        raise ValueError("the settle norm must be zero or more")
    if not (settle < 100):
        raise ValueError("the settle norm must be less than 100")
    loose_yards = cuft / (1 - settle / 100) / 27
    yards = cuft / 27
    extra = loose_yards - yards
    rounded_extra = math.floor(extra * 10 + 0.5) / 10
    if rounded_extra == 0:
        tail = "no settle allowance to speak of honestly."
    else:
        if rounded_extra <= 0.5:
            verdict = "a light allowance honestly"
        elif rounded_extra <= 2:
            verdict = "a working allowance honestly"
        else:
            verdict = "a generous allowance honestly"
        tail = f"{fixed1(extra)} {plural(1 if rounded_extra == 1 else 2, 'yard', 'yards')} of settle allowance, {verdict}."
    return f"To finish at {depth} {plural(depth, 'inch', 'inches')} over {area} {plural(area, 'square foot', 'square feet')} at the {settle}% settle norm, order {fixed1(loose_yards)} cubic yards - {tail}"

FNS = {"coverageTruth": coverage_truth, "bagTruth": bag_truth, "settleTruth": settle_truth}

cases = [
 {"fn":"coverageTruth","args":[1000,3]},
 {"fn":"coverageTruth","args":[100,1]},
 {"fn":"coverageTruth","args":[400,2]},
 {"fn":"coverageTruth","args":[2000,4]},
 {"fn":"coverageTruth","args":[20000,6]},
 {"fn":"coverageTruth","args":[97,3]},
 {"fn":"coverageTruth","args":[0,3]},
 {"fn":"coverageTruth","args":[1000,0]},
 {"fn":"bagTruth","args":[1000,3,0.75]},
 {"fn":"bagTruth","args":[100,1,0.75]},
 {"fn":"bagTruth","args":[50,2,1]},
 {"fn":"bagTruth","args":[500,3,2]},
 {"fn":"bagTruth","args":[5000,4,0.75]},
 {"fn":"bagTruth","args":[1,1,1]},
 {"fn":"bagTruth","args":[3,1,0.75]},
 {"fn":"bagTruth","args":[1000,3,0]},
 {"fn":"bagTruth","args":[0,3,0.75]},
 {"fn":"settleTruth","args":[1000,3,15]},
 {"fn":"settleTruth","args":[200,2,10]},
 {"fn":"settleTruth","args":[5000,6,20]},
 {"fn":"settleTruth","args":[120,1,5]},
 {"fn":"settleTruth","args":[1000,3,0]},
 {"fn":"settleTruth","args":[1000,3,-5]},
 {"fn":"settleTruth","args":[1000,3,100]},
 {"fn":"settleTruth","args":[0,3,15]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
