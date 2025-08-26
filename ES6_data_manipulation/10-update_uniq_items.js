export default function updateUniqueItems(aMap) {
  if (!(aMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  aMap.forEach((qty, item) => {
    if (qty === 1) {
      aMap.set(item, 100);
    }
  });

  return aMap;
}
