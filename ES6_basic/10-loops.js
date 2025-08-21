export default function appendToEachArrayValue(array, appendString) {
  const result = [];

  // On parcourt directement les valeurs du tableau avec for...of
  for (const value of array) {
    result.push(appendString + value);
  }

  return result;
}