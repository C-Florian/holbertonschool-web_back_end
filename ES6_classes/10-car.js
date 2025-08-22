export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Permet aux sous-classes de contrôler la "species"
  static get [Symbol.species]() {
    return this;
  }

  // Doit retourner une nouvelle instance de la même classe (ex: TestCar)
  // avec des propriétés undefined (car aucun argument n'est passé)
  cloneCar() {
    const C = this.constructor[Symbol.species];
    return new C();
  }
}
