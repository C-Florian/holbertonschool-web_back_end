function getCurrentYear() {
  const date = new Date();
  return date.getFullYear(); // ex: 2025
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
    // Les clés de l'objet sont "calculées" avec des backticks et ${...}
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };

  return budget;
}