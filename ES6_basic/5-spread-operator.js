export default function concatArrays(array1, array2, string) {
  // On déplie array1, array2 et string (chaîne décomposée en lettres)
  return [...array1, ...array2, ...string];
}