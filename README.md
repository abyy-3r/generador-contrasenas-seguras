<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=26&pause=1000&color=FF69B4&center=true&vCenter=true&width=750&lines=%E2%98%BD+GENERADOR+DE+CONTRASE%C3%91AS+SEGURAS+%E2%98%BE;Sistema+Criptogr%C3%A1fico+y+Evaluador+de+Fortaleza" alt="Título animado" />

![Python](https://img.shields.io/badge/PYTHON-3.15-ff69b4?style=for-the-badge&logo=python&logoColor=white)
![UIDE](https://img.shields.io/badge/UIDE-L%C3%93GICA_DE_PROGRAMACI%C3%93N-c39bd3?style=for-the-badge)
![Status](https://img.shields.io/badge/ESTADO-EN_DESARROLLO-f8a5c2?style=for-the-badge)

<br>

**✮ Sistema modular en consola desarrollado en Python, enfocado en la creación de claves seguras y el análisis lógico de su entropía. ✮**

</div>

## 📌 Descripción del Proyecto
Este proyecto implementa un sistema modular en consola desarrollado en **Python** bajo un enfoque estructurado y algorítmico. Su objetivo es automatizar la creación de credenciales robustas y auditar su nivel de seguridad frente a ataques de fuerza bruta, equilibrando la entropía matemática con los criterios de usabilidad del usuario.

El núcleo del sistema opera mediante un menú interactivo en tiempo real que coordina dos módulos funcionales principales:
- 🔑 **Generador Personalizado:** Valida los parámetros de entrada (longitud entre 8 y 64 caracteres y tipos de caracteres requeridos) mediante bucles de control (`while`) y construye la clave carácter por carácter utilizando aleatoriedad criptográfica segura.
- 🛡️ **Evaluador de Fortaleza:** Analiza la longitud y diversidad de caracteres de una contraseña mediante estructuras condicionales encadenadas (`if`, `elif`, `else`) y operadores lógicos (`and`) para diagnosticar su nivel de seguridad (**Débil**, **Media** o **Fuerte**).

## 🛠️ Tecnologías y Librerías Utilizadas
- **Lenguaje:** Python 3.15
- **Paradigma:** Programación Estructurada y Modular
- **Entorno de Desarrollo:** Visual Studio Code / draw.io
- **Librerías Nativas:**
  - `secrets`: Generación de números y selección de caracteres criptográficamente seguros (CSPRNG), superior al módulo `random` para seguridad informática.
  - `string`: Gestión estándar de conjuntos de caracteres (mayúsculas, minúsculas, dígitos y puntuación).

## 🚀 Preparación del Entorno e Instalación
Este proyecto utiliza exclusivamente librerías estándar de Python, por lo que **no requiere instalar dependencias externas ni entornos virtuales**.

1. **Clonar o descargar el repositorio:**
   ```bash
   git clone [https://github.com/abyy-3r/generador-contrasenas-seguras.git](https://github.com/abyy-3r/generador-contrasenas-seguras.git)
   cd generador-contrasenas-seguras
   ```
   *(También puedes descargarlo directamente desde GitHub haciendo clic en **Code → Download ZIP**).*

2. **Verificar la instalación de Python:**
   ```bash
   py --version
   ```

## 💻 Ejecución del Sistema
1. Abre una terminal en la carpeta raíz del proyecto (`Generador_Contrasenas`).
2. Ejecuta el archivo principal:
   ```bash
   py codigo/generador.py
   ```
3. **Flujo de uso en consola:**
   - Selecciona la opción `1` para configurar y generar una nueva contraseña.
   - Ingresa la longitud deseada (entre `8` y `64` caracteres).
   - Responde con `s` o `n` para incluir mayúsculas, minúsculas, números y símbolos.
   - Selecciona la opción `2` para evaluar la seguridad de una clave existente o `3` para finalizar.

## 📂 Estructura del Repositorio
```text
generador-contrasenas-seguras/
├── README.md                                  # Documentación técnica del proyecto
├── codigo/
│   └── generador.py                           # Código fuente principal (menú, validaciones y lógica)
└── diagramas/
    ├── flujo_generar_contrasena.png           # Diagrama de flujo algorítmico: Generación
    ├── flujo_evaluar_fortaleza.png            # Diagrama de flujo algorítmico: Evaluación
    ├── Generador seguro de contraseñas-Diagrama de arquitectura .drawio (1).png
    └── Generador seguro de contraseñas-Diagramas funcionales (casos de uso u otros) .drawio (1).png
```

## 👩‍💻 Información Académica
- **Autora:** Briana Abigail Dueñas Granda
- **Institución:** Universidad Internacional del Ecuador (UIDE)
- **Carrera:** Ingeniería en Ciencia de Datos
- **Asignatura:** Lógica de Programación (Aprendizaje Autónomo 2 — 2026)
