# Dca-Scv
Repositorio para la practica de DCA de sistemas de control de versiones
### Enlace del repositorio:
https://github.com/jcsc15-ua/Dca-Scv.git

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
![alt text](<Captura de pantalla 2024-12-26 a las 13.16.40.png>)

### Contenido de .git/hooks/pre-commit:
```
#!/bin/bash
echo "Ejecutando comprobación 1: Validar sintaxis de Python"
FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

for file in $FILES; do
    if ! python -m py_compile "$file"; then
        echo "Error de sintaxis en $file"
        exit 1
    fi
done

echo "Ejecutando comprobación 2: Validar que los commits no contengan palabras prohibidas"
if git diff --cached | grep -i "palabra-prohibida"; then
    echo "Error: Se detectó una palabra prohibida en los cambios."
    exit 1
fi

echo "Todas las comprobaciones pasaron. Commit permitido."
```
### Dar los permisos al hook
chmod +x .git/hooks/pre-commit
