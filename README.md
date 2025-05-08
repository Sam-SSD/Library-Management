![Library management system banner](https://github.com/user-attachments/assets/b71cf61c-3eb0-41a1-820e-e84f4ca650fd)

# 📚 Sistema de Gestión de Biblioteca

### 📘 English version  
[Click here to view the README in English](./README_EN.md)

---

## 📌 Descripción del Proyecto

Este proyecto está diseñado para simular un **sistema de gestión de biblioteca**, donde los usuarios pueden agregar, prestar, devolver y gestionar libros a través de un menú interactivo en consola. El sistema está construido con **Python**, siguiendo principios de **programación orientada a objetos (OOP)** y diseño **modular**.

---

## 🎯 Funcionalidades

- **Agregar nuevos libros** con título, autor, género y cantidad de copias disponibles.
- **Evitar títulos duplicados** (la comparación no distingue mayúsculas).
- **Prestar y devolver libros**, actualizando el estado de disponibilidad.
- **Eliminar libros** solo si todas sus copias están disponibles.
- **Listar libros** agrupados por género.
- **Ver resumen del inventario** con estadísticas: total, disponibles y prestados.

---

## 🧠 Lógica Implementada

- La clase `Library` encapsula toda la lógica y los datos relacionados con los libros.
- El archivo `utils.py` centraliza las validaciones de entrada (nombres, números, géneros).
- El flujo del programa se organiza en `main.py`, con una función dedicada por acción (`handle_add_book()`, etc.).
- Se usan propiedades (`@property`) para calcular en tiempo real los totales del inventario.
- Todos los libros se almacenan como diccionarios estructurados dentro de una lista.

---

## ✅ Validaciones Realizadas

- **Título** y **autor**: deben ser cadenas no vacías y no numéricas.
- **Género**: debe estar dentro de la lista predefinida de géneros válidos.
- **Copias**: debe ser un número entero positivo.
- No se permiten títulos duplicados (comparación no sensible a mayúsculas).
- Todos los datos son validados antes de ser procesados.

---

## 📁 Estructura del Proyecto

```
library_app/
├── main.py       # Menú interactivo y control del flujo del programa
├── library.py    # Clase Library con toda la lógica de negocio
└── utils.py      # Validación de entradas del usuario
```

---

## 🧩 Descripción de Archivos

- **`main.py`**  
  Contiene el punto de entrada y funciones como `handle_add_book`, `handle_borrow_book`, etc., para modularizar la interacción con el usuario.

- **`library.py`**  
  Define la clase `Library`, que gestiona el registro, búsqueda, préstamo, devolución, eliminación, listado y resumen de libros.

- **`utils.py`**  
  Proporciona funciones reutilizables para validar entradas como cadenas, números y géneros válidos.

---

## 💡 Justificación Técnica

- El uso de `@property` permite calcular estadísticas dinámicas del inventario.
- El diseño modular mejora la mantenibilidad y la escalabilidad del proyecto.
- Las validaciones están centralizadas y son robustas.
- La organización clara del código facilita futuras integraciones con interfaces gráficas o APIs.

---

## 🚀 Posibles Mejoras Futuras

- Permitir la edición de datos de libros (título, autor, género).
- Agregar campos adicionales como descripción o ISBN.
- Implementar filtros por autor o estado de disponibilidad.
- Exportar/importar inventario desde archivos (CSV, JSON).
- Integrar interfaz gráfica con Tkinter o aplicación web con Flask.

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener **Python 3.10 o superior** instalado.
2. Clona el repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Library-Management.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Library-Management/library_app
   ```

4. Ejecuta el sistema desde el archivo principal:

   ```bash
   python main.py
   ```

5. Usa el menú interactivo para gestionar los libros de tu biblioteca.

---
