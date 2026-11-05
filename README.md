# orbit-hermite-gap-check

## Français

Comparer interpolation orbitale et lacunes de mesures.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m orbit_hermite_gap_check examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Hermite cubique 3D position/vitesse, désaccord avec interpolation linéaire et contrôle leave-one-out. SciPy fournit le moteur général ; ici les refus de lacunes et l’exemple orbital sont explicites.

### Limites

Même repère et unités déclarés par appelant. Désaccord entre interpolants non équivalent à erreur vraie. Pas de propagation gravitationnelle.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compare orbital interpolation and observation gaps.

Synthetic data; no network access or secret required.

```sh
python -m orbit_hermite_gap_check examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

3D position/velocity cubic Hermite, linear disagreement and leave-one-out checks. SciPy provides the general engine; this package makes gap refusals and an orbital example explicit.

### Limits

Caller supplies a common frame and units. Interpolant disagreement is not true error. No gravitational propagation.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comparar interpolación orbital y huecos de medición.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m orbit_hermite_gap_check examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Hermite cúbico 3D posición/velocidad, diferencia lineal y pruebas leave-one-out. SciPy ofrece motor general; este paquete explicita rechazos de huecos y ejemplo orbital.

### Límites

El usuario aporta marco y unidades comunes. Desacuerdo entre interpolantes no es error real. Sin propagación gravitatoria.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicHermiteSpline.html
