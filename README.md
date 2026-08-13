# BMI Calculator

Calculadora de Índice de Masa Corporal (BMI) con soporte para sistema métrico e imperial, que además del BMI y su categoría, calcula el rango de peso ideal del usuario según su altura.

## Características

- Soporta ambos sistemas de medida: métrico (kg, cm) e imperial (lbs, inches).
- Calcula el BMI, la categoría (Underweight, Normal, Overweight, Obesity) y el rango de peso ideal.
- Validación robusta de inputs: rechaza texto no numérico, valores negativos y cero.
- Arquitectura de tres capas: Motor Core (funciones puras), Interfaz (validación e input/output) y Ensamblaje (main).

## Estructura del proyecto

```
bmi_calculator/
├── requirements.py    # Constantes del proyecto (límites de categoría, factor imperial)
├── calculate.py        # Motor Core + funciones de interfaz
└── main.py              # Punto de entrada, ensamblaje del programa
```

## Fórmulas utilizadas

**Métrico:**
```
BMI = weight_kg / (height_m)²
```

**Imperial:**
```
BMI = 703 × weight_lbs / (height_inches)²
```

**Peso ideal:** rango de peso que da un BMI entre 18.5 y 25.0 para la altura ingresada.

## Categorías (estándar OMS)

| Categoría   | Rango de BMI     |
|-------------|------------------|
| Underweight | < 18.5           |
| Normal      | 18.5 – 24.9      |
| Overweight  | 25.0 – 29.9      |
| Obesity     | ≥ 30.0           |

## Cómo ejecutar

```bash
python main.py
```

El programa pedirá:
1. Sistema de medida (`metric` o `imperial`)
2. Altura (en cm o inches según el sistema elegido)
3. Peso (en kg o lbs según el sistema elegido)

Y mostrará el BMI, la categoría y el rango de peso ideal.

## Requisitos

- Python 3.x (sin dependencias externas)

## Limitaciones conocidas

- No hay persistencia de datos entre ejecuciones.
- No soporta conversión automática entre sistemas (el usuario debe ingresar los datos en las unidades del sistema elegido).
- No calcula BMI ajustado por edad, sexo o composición corporal — usa la fórmula estándar únicamente.

## Nota de Riesgo

Ver [RISK_NOTE.md](./RISK_NOTE.md).
