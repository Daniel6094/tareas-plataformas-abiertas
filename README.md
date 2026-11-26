# Front-end — Prueba de conexión con la API

Página sencilla para demostrar que el front-end se conecta a la API y puede realizar consultas GET con `fetch()`. Las respuestas se muestran como filas en una tabla HTML generada dinámicamente. Está construida con HTML, CSS y JavaScript nativo, sin dependencias de front-end.

## Ejecución local

1. Inicia MongoDB y configura la conexión de base de datos de la API.
2. En una terminal, instala las dependencias e inicia la API:

   ```bash
   cd API/v1
   pip install -r requirements.txt
   python run.py
   ```

3. En otra terminal, desde la raíz del repositorio, inicia un servidor estático:

   ```bash
   python -m http.server 5500 --directory FRONTEND
   ```

4. Abre <http://127.0.0.1:5500>.
5. Ingresa `http://127.0.0.1:5000/api/v1` como URL base y el token configurado en la API. Pulsa **Probar conexión**; se consulta la lista de productos para validar la URL, el token y el acceso a la base de datos. Una vez conectada, selecciona una consulta y pulsa **Consultar** para mostrar el código HTTP y los registros recibidos en una tabla.

El servidor de API permite por defecto los orígenes `http://127.0.0.1:5500` y `http://localhost:5500`. Si sirves el front-end desde otro origen, configura `FRONTEND_ORIGINS` en la terminal donde inicias la API con una lista separada por comas; por ejemplo:

```bash
FRONTEND_ORIGINS=http://127.0.0.1:5500,http://localhost:5500 python run.py
```

La URL y el token se guardan en el almacenamiento local del navegador para conservar la configuración. No uses credenciales de producción en una demostración compartida.

## Endpoints utilizados

| Consulta | Método | Endpoint |
|---|---|---|
| Listar productos y comprobar conexión | `GET` | `/api/v1/productos/` |
| Listar marcas | `GET` | `/api/v1/marcas/` |
| Reporte de stock restante | `GET` | `/api/v1/productos/reportes/stock-restante` |
| Reporte de marcas con ventas | `GET` | `/api/v1/marcas/reportes/marcas-con-ventas` |
| Reporte top 5 de marcas | `GET` | `/api/v1/marcas/reportes/top-5-marcas` |
