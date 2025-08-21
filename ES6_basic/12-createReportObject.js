export default function createReportObject(employeesList) {
  // employeesList est un objet comme :
  // { engineering: ['Bob', 'Jane'], marketing: ['Sylvie'] }

  return {
    // On recopie l'objet reçu dans la clé allEmployees
    allEmployees: { ...employeesList },

    // Méthode ES6 pour compter le nombre de départements
    getNumberOfDepartments(allEmployees) {
      // Object.keys(allEmployees) renvoie un tableau des clés (noms de départements)
      // .length = combien de clés il y a
      return Object.keys(allEmployees).length;
    },
  };
}