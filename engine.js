// Topsoil Math engine - hypothetical arithmetic on labeled norms only.
// Coverage, bag and settle figures are illustrative norms; soil density,
// moisture and compaction change real loads.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function cubicFeet(area, depth) {
  if (!(area > 0)) throw new Error("the area must be above zero");
  if (!(depth > 0)) throw new Error("the depth must be above zero");
  return area * depth / 12;
}

function coverageTruth(area, depth) {
  const cuft = cubicFeet(area, depth);
  const yards = cuft / 27;
  let verdict;
  if (yards <= 1) verdict = "a few wheelbarrows honestly";
  else if (yards <= 5) verdict = "a small delivery honestly";
  else if (yards <= 15) verdict = "a truckload honestly";
  else verdict = "several truckloads honestly";
  return `${area} ${plural(area, "square foot", "square feet")} at ${depth} ${plural(depth, "inch", "inches")} is ${fixed1(cuft)} cubic feet - ${fixed1(yards)} cubic ${plural(Math.round(yards * 10) / 10 === 1 ? 1 : 2, "yard", "yards")}, ${verdict}.`;
}

function bagTruth(area, depth, bag) {
  const cuft = cubicFeet(area, depth);
  if (!(bag > 0)) throw new Error("the bag size must be above zero");
  const bags = Math.ceil(cuft / bag - 1e-9);
  let verdict;
  if (bags <= 20) verdict = "a trunk of bags honestly";
  else if (bags <= 80) verdict = "a pallet of bags honestly";
  else if (bags <= 200) verdict = "a few pallets honestly";
  else verdict = "many pallets honestly";
  const bagPart = bags === 1 ? `1 of the ${bag}-cubic-foot bags` : `${bags} of the ${bag}-cubic-foot bags`;
  return `${area} ${plural(area, "square foot", "square feet")} at ${depth} ${plural(depth, "inch", "inches")} is ${bagPart} - ${verdict}.`;
}

function settleTruth(area, depth, settle) {
  const cuft = cubicFeet(area, depth);
  if (!(settle >= 0)) throw new Error("the settle norm must be zero or more");
  if (!(settle < 100)) throw new Error("the settle norm must be less than 100");
  const looseYards = cuft / (1 - settle / 100) / 27;
  const yards = cuft / 27;
  const extra = looseYards - yards;
  const roundedExtra = Math.round(extra * 10) / 10;
  let tail;
  if (roundedExtra === 0) tail = "no settle allowance to speak of honestly.";
  else {
    let verdict;
    if (roundedExtra <= 0.5) verdict = "a light allowance honestly";
    else if (roundedExtra <= 2) verdict = "a working allowance honestly";
    else verdict = "a generous allowance honestly";
    tail = `${fixed1(extra)} ${plural(roundedExtra === 1 ? 1 : 2, "yard", "yards")} of settle allowance, ${verdict}.`;
  }
  return `To finish at ${depth} ${plural(depth, "inch", "inches")} over ${area} ${plural(area, "square foot", "square feet")} at the ${settle}% settle norm, order ${fixed1(looseYards)} cubic yards - ${tail}`;
}

if (typeof module !== "undefined") {
  module.exports = { cubicFeet, coverageTruth, bagTruth, settleTruth };
}
