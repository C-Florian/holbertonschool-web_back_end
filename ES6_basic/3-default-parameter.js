export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  // La magie est ici : si on n'envoie pas expansion1989 ou expansion2019,
  // ils prendront par défaut 89 et 19.
  return initialNumber + expansion1989 + expansion2019;
}