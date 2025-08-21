import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);

  const fullBudget = {
    ...budget, // on recopie income, gdp, capita
    // Avant : getIncomeInDollars: function(income) { ... }
    // Maintenant : syntaxe méth