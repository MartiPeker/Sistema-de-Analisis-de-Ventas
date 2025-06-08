# 🧠 Sistema de Análisis de Ventas

Proyecto de análisis de ventas para una startup con múltiples sucursales, utilizando programación orientada a objetos, patrones de diseño y visualización de datos.

---

## 🛠️ Características Implementadas

### 📄 Modelado relacional en MySQL
- Base de datos `sales_company` con tablas normalizadas.
- Claves primarias y relaciones que aseguran integridad referencial.
- Modelos SQLAlchemy en `src/orm/`.

### 🔌 Conexión a base de datos con SQLAlchemy
- Implementación del patrón **Singleton** en `DBConnection`.
- `scoped_session` para entornos multi-hilo o múltiples procesos.
- Configuración flexible vía `config.py`.

### 🧠 Patrones de Diseño

| Patrón      | Aplicación |
|-------------|------------|
| **Singleton** | Conexión única a la base de datos. |
| **Factory**   | `SalesSummaryFactory` genera objetos desde Series de pandas. |
| **Strategy**  | Análisis por producto y ciudad intercambiables. |
| **Builder**   | `ReportBuilder` encadena estrategias de análisis. |

### 📊 Análisis de datos en Jupyter Notebook
- Consultas y análisis convertidos a `DataFrames`.
- Visualizaciones con `matplotlib`.

### ✅ Pruebas unitarias con `unittest`
- Validación de patrones de diseño (`Singleton`, `Strategy`, `Builder`).
- Test en carpeta `tests/`.

---

## 📁 Estructura del Proyecto

```
ventas_project/
├── README.md
├── requirements.txt
├── data/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── load_data.py
│   ├── db/
│   │   ├── connection.py
│   │   └── schema.sql
│   ├── orm/
│   │   ├── base.py
│   │   ├── customer.py ...
│   ├── analysis/
│   │   ├── builder.py
│   │   ├── context.py
│   │   └── strategies...
│   └── factory/
│       └── sales_summary.py
├── tests/
│   ├── test_db_connection.py
│   ├── test_strategies.py
│   └── test_builder.py
```

---

## 🚀 Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar aplicación
```bash
python src/main.py
```

### 3. Correr tests
```bash
pytest tests/
```

### 4. Notebook
```bash
jupyter notebook analisis_ventas.ipynb
```