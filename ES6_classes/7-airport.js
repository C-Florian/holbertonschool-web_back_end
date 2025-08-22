export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  // Permet d’obtenir:
  // - console.log(airport) -> Airport [SFO] { ... }
  // - airport.toString()   -> [object SFO]
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
