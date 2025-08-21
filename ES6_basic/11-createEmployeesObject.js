export default function createEmployeesObject(departmentName, employees) {
  // On crée un objet dont la clé est le nom du département
  // et la valeur est le tableau d'employés
  return {
    [departmentName]: employees,
  };
}