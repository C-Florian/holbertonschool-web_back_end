export default function hasValuesFromArray(aSet, array) {
  if (!(aSet instanceof Set) || !Array.isArray(array)) return false;
  return array.every((v) => aSet.has(v));
}
