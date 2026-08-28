# 🐕 Rover.exe - Reviving Windows XP Nostalgia

<div align="center">

![Rover](https://img.shields.io/badge/Rover-XP%20Legacy-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Alpha-orange?style=for-the-badge)

**El perrito más icónico de Windows XP está de vuelta.**

*Built with Python | Compiled to .exe with GitHub Actions*

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Contributing](#contributing)

</div>

---

## 🐕 ¿Qué es Rover.exe?

Rover era ese perrito adorable que aparecía en Windows XP para ayudarte a buscar archivos. Ahora lo traemos de vuelta en 2026 con Python puro y compilado a `.exe` automáticamente.

**Nostalgia + Código Moderno = Rover.exe**

---

## ✨ Features

- ✅ **Perrito interactivo** - Aparece en tu pantalla y reacciona a clics
- ✅ **Búsqueda de archivos** - Como el original, pero mejorado
- ✅ **Sonidos retro** - Ladridos y efectos de sonido de Windows XP
- ✅ **Compilado automáticamente** - GitHub Actions convierte Python → .exe
- ✅ **Lightweight** - No pesa nada, corre en cualquier PC
- ✅ **Customizable** - Cambia el comportamiento del perrito

---

## 🚀 Installation

### Opción 1: Descargar el .exe (RECOMENDADO)

1. Ir a [Releases](https://github.com/anyelo888ra-ux/rover-exe/releases)
2. Descargar `rover.exe`
3. Ejecutar y listo ✨

### Opción 2: Desde Python

```bash
# Clonar el repo
git clone https://github.com/anyelo888ra-ux/rover-exe.git
cd rover-exe

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python rover.py
```

---

## 📖 Usage

### Ejecutar Rover
```bash
python rover.py
```

### Interactuar con el perrito
- **Click izquierdo** → El perrito reacciona
- **Click derecho** → Menú contextual
- **ESC** → Cerrar

### Opciones de línea de comandos
```bash
python rover.py --size small      # Tamaño pequeño
python rover.py --speed fast      # Movimiento rápido
python rover.py --sound off       # Sin sonidos
python rover.py --help            # Ver todas las opciones
```

---

## 🛠️ Cómo se compila a .exe

Usamos **GitHub Actions** para compilar automáticamente:

```yaml
# Cuando hagas push → GitHub Action se ejecuta
# Python + PyInstaller → rover.exe
# Descargable en Releases
```

**No necesitas instalar nada en tu PC.** Nosotros compilamos por ti. 🚀

---

## 📦 Estructura del Proyecto

```
rover-exe/
├── rover.py                    # Script principal (TODO)
├── requirements.txt            # Dependencias (Tkinter, etc)
├── .github/workflows/
│   └── build.yml              # GitHub Actions build config
├── README.md                   # Este archivo
└── LICENSE                     # MIT License
```

---

## 🔧 Tech Stack

- **Python 3.8+** - Lenguaje principal
- **Tkinter** - GUI para la ventana del perrito
- **PyInstaller** - Compilar a .exe
- **GitHub Actions** - Automatizar compilación

---

## 📝 Ejemplos de Código

### Ejecutar el Rover con configuración custom

```python
rover = Rover(
    size="medium",
    speed=5,
    sounds=True,
    behavior="search"
)
rover.run()
```

---

## 🎮 Modo de Juego (Beta)

Próximamente: Rover busca archivos en tu PC y los muestra de forma gamificada.

---

## 🤝 Contributing

¿Quieres mejorar a Rover?

1. Fork el repo
2. Crea una rama: `git checkout -b feature/mi-feature`
3. Commit: `git commit -m "Add mi-feature"`
4. Push: `git push origin feature/mi-feature`
5. Abre un Pull Request

---

## 👥 Colaboradores

- **@anyelo888ra-ux** - Creador
- **@claude** - AI Collaborator (XD)
- **@dependabot[bot]** - Dependency updates

---

## 📄 License

Este proyecto está bajo la licencia **MIT**. Ver [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- Microsoft por crear el Rover original (Windows XP ❤️)
- La comunidad de Python
- GitHub Actions por el CI/CD gratuito

---

## 🔗 Links

- 🐙 [GitHub](https://github.com/anyelo888ra-ux/rover-exe)
- 📺 [YouTube - c00lkidd_v2yt](https://youtube.com/@c00lkidd_v2yt)
- 🎮 [Twitch](https://twitch.tv/c00lkidd_v2ytofficial)

---

<div align="center">

**Hecho con ❤️ por c00lkidd**

*"Bringing back nostalgia, one bark at a time" 🐕*

</div>
