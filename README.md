# Dca-Scv
Repositorio para la practica de DCA de sistemas de control de versiones

# Proyecto Prueba con Git

## Alias configurados
- Alias globales:
  - `s`: `status`
  - `lg`: `log --oneline --graph --all`
  - `co`: `checkout`

- Alias locales:
  - `br`: `branch`
  - `cm`: `commit -m`

## Uso de git bisect

- Inicialicé el proceso con `git bisect start`.
- Marqué el commit actual como malo (`git bisect bad`) y un commit previo funcional como bueno (`git bisect good 403f51842188595951eb9e07eabad526988ec26e`).
- Probé cada commit con `python main.py`:
  - Si el resultado era correcto, usé `git bisect good`.
  - Si el resultado era incorrecto, usé `git bisect bad`.
- Identifiqué el commit defectuoso con hash `8ff41f787dccab64c216798df07c302135d36aee`.
- Finalicé el proceso con `git bisect reset`.
- Añadí un nuevo commit con los cambios para solucionar el error y el proceso en el readme.


## Uso del hook
- Configuré un hook pre-commit en `.git/hooks/pre-commit` para imprimir un mensaje al intentar un commit.

