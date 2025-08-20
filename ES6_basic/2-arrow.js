export default function getNeighborhoodsList() {
  // 1) Une "propriété" de l'objet courant (this)
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  // 2) On remplace la fonction classique par UNE ARROW FUNCTION
  //    Avantage: l'arrow garde le "this" du dessus (lexical this).
  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
