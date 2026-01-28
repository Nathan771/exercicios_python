# Copilot Instructions for Python Exercises Repository

This repository contains standalone Python programming exercises (ex1.py to ex27.py) implementing basic programming concepts for beginners.

## Code Patterns

- **User Input**: Use `input()` for stdin, often with Portuguese prompts. Convert to appropriate types immediately.
  ```python
  num = float(input("Digite a primeira nota: "))  # From ex2.py
  ```

- **Output**: Use `print()` with f-strings for formatted output.
  ```python
  print(f"A média das notas é: {media}")  # From ex2.py
  ```

- **Error Handling**: Handle invalid inputs with try-except blocks for ValueError.
  ```python
  try:
      num = float(input("Digite um número: "))
  except ValueError:
      print("Digite apenas números! ")  # From ex2.py
  ```

- **Data Storage**: Use lists for sequences, dictionaries for key-value pairs.
  ```python
  lista = [num, num2, num3, num4]  # From ex2.py
  produtos.append({"Produto": nome_produtos, "Preço": preco})  # From ex27.py
  ```

- **Calculations**: Use built-in functions like `max()`, `min()`, `sum()`, and basic operators.
  ```python
  media = sum(lista) / 4  # From ex2.py
  area = (raio**2 * 3.14)  # From ex10.py
  ```

- **Control Flow**: Use if-else for conditionals, for loops for iteration.
  ```python
  if num % 2 == 0:
      print("Esse número é par! ")  # From ex1.py
  ```

- **Functions**: Define functions for organization, call at script end.
  ```python
  def notas():
      # implementation
  notas()  # From ex2.py
  ```

## Developer Workflows

- **Running Exercises**: Execute with `python exX.py` in terminal.
- **No Dependencies**: Uses only Python standard library (e.g., `time` for delays in ex3.py).
- **No Tests or Builds**: Each file is a self-contained script.

## Project Conventions

- **Language**: Code in English (keywords), prompts/comments in Portuguese.
- **Naming**: Variables often in Portuguese (e.g., `lista`, `media`, `produtos`).
- **Style**: Procedural, no classes; 4-space indentation.
- **Imports**: Minimal, only when needed (e.g., `import time`).

Reference files: [ex1.py](ex1.py), [ex2.py](ex2.py), [ex3.py](ex3.py), [ex10.py](ex10.py), [ex27.py](ex27.py)</content>
<parameter name="filePath">/home/nathanfefe/Documents/exercicios_python/.github/copilot-instructions.md