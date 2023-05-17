## Public: 
Las propiedades y métodos públicos se pueden acceder desde cualquier lugar fuera de la clase.

## Private:
Las propiedades y métodos privados solo se pueden acceder dentro de la clase.

## Protected:
Las propiedades y métodos protegidos se pueden acceder desde dentro de la clase y sus subclases.

---
Python solo tiene la distinción entre públicos y privados. La especificacipon de privacidad en python se hace en el nombre de la variable o método. 
Si el nombre comienza con un guión bajo, el método o variable es privado. De lo contrario, es público.

### Ejemplo: 

clase MedioTransporte:
  - _velocidad: int
  - _color: str
  - _marca: str
  - _modelo: str
  - _placa: str
  - _acelerar(): void
  - _frenar(): void

clase Carro hereda de MedioTransporte:
    - _numeroPuertas: int
    - _numeroAsientos: int

clase Bicicleta hereda de MedioTransporte:
    - _numeroCambios: int
    
clase Moto hereda de MedioTransporte:
    - _cilindraje: int


---

Lógica del problema != Lógica asociada al programa. 

