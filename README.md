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
1. Inicié la búsqueda con `git bisect start`.
2. Marqué el commit con el error como `git bisect bad`.
3. Marqué un commit bueno previo como `git bisect good`.
4. Seguí el proceso hasta identificar el commit defectuoso.
5. Finalicé con `git bisect reset`.

## Uso del hook
- Configuré un hook pre-commit en `.git/hooks/pre-commit` para imprimir un mensaje al intentar un commit.

