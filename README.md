# PC Performance Optimizer

A polished Windows-focused desktop app for improving PC performance and reducing distractions.

## Features

- Performance Score card with live CPU, RAM, and disk health
- Focus Mode toggle to minimize distractions
- Debloat checklist of safe cleanup recommendations
- Restore Changes button to undo optimization actions
- Startup app detection and lightweight cleanup suggestions
- Modern dark-mode interface

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

## Project structure

```text
PC-Performance-Optimizer/
├── main.py
├── requirements.txt
├── README.md
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── performance.py
│   │   ├── focus_manager.py
│   │   └── debloat.py
│   └── ui/
│       ├── __init__.py
│       └── main_window.py
└── LICENSE
```

## Safety notes

This app focuses on safe recommendations and cleanup flows. It does not remove core system components automatically without confirmation.
