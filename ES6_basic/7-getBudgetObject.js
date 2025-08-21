export default function getBudgetObject(income, gdp, capita) {
  // Au lieu de "income: income", on peut écrire simplement "income"
  const budget = { income, gdp, capita };
  return budget;
}