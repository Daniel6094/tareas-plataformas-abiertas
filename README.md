# Documentación de la API — Proyecto 2

## Descripción general

Este documento describe las solicitudes registradas en la colección de Postman **Proyecto 2**. La colección contiene seis operaciones relacionadas con la comprobación de disponibilidad de la API, la gestión de usuarios y la consulta de reportes de inventario y ventas.

> **Estado de la documentación:** preliminar. La colección proporcionada no contiene las URL de los endpoints ni ejemplos de solicitudes o respuestas. Esos datos deben completarse con la implementación real de la API.

## Tabla de contenidos

- [Información de la colección](#información-de-la-colección)
- [Requisitos](#requisitos)
- [Configuración de autenticación](#configuración-de-autenticación)
- [Convenciones y configuración pendiente](#convenciones-y-configuración-pendiente)
- [Endpoints registrados](#endpoints-registrados)
  - [Verificar que la API responde](#verificar-que-la-api-responde)
  - [Listar usuarios](#listar-usuarios)
  - [Crear un usuario](#crear-un-usuario)
  - [Reporte de marcas con ventas](#reporte-de-marcas-con-ventas)
  - [Reporte de stock restante](#reporte-de-stock-restante)
  - [Reporte del top 5 de marcas](#reporte-del-top-5-de-marcas)
- [Resumen de endpoints](#resumen-de-endpoints)
- [Códigos HTTP](#códigos-http)
- [Cómo importar y probar la colección en Postman](#cómo-importar-y-probar-la-colección-en-postman)
- [Información pendiente](#información-pendiente)
- [Licencia y mantenimiento](#licencia-y-mantenimiento)

## Información de la colección

| Propiedad | Valor |
|---|---|
| Nombre | Proyecto 2 |
| Formato de colección | Postman Collection v2.1 |
| Autenticación configurada | `******` |
| Cantidad de solicitudes | 6 |

## Requisitos

Para probar los recursos documentados se necesita:

- Postman o un cliente HTTP equivalente.
- La dirección base de la API.
- Un token `******`.
- La información específica de cada operación, cuando corresponda.

## Configuración de autenticación

La colección utiliza autenticación de tipo `******`.

Incluya el token en el encabezado HTTP:

```http
Authorization: ******
```

No publique tokens reales en el repositorio. Configure el token como variable de entorno de Postman (por ejemplo, `{{token}}`) o como secreto en el entorno de despliegue.

> **Seguridad:** el archivo original contiene un valor de token escrito directamente en la colección. Antes de compartir la colección o subirla a GitHub, revoque o rote ese token si es válido y sustitúyalo por una variable segura.

## Convenciones y configuración pendiente

En las seis solicitudes, Postman registra el método `GET`. Sin embargo, la operación denominada **Crear un Usuario** también aparece configurada como `GET`. Esto se documenta tal como está en el archivo; debe verificarse con el código de la API si el método correcto debería ser `POST`.

Las URL aparecen vacías (`raw: ""`) en todas las solicitudes. Por lo tanto, no es posible determinar las rutas ni construir ejemplos funcionales de llamadas sin información adicional.

## Endpoints registrados

### Verificar que la API responde

Comprueba si la API está disponible y responde a una solicitud.

| Propiedad | Valor |
|---|---|
| Nombre en Postman | Verificar que la API responde |
| Método registrado | `GET` |
| URL | Pendiente de configurar |
| Autenticación | `******` según la configuración de la colección |
| Parámetros | No especificados |
| Cuerpo de la solicitud | No especificado |
| Respuesta esperada | No documentada en la colección |

Ejemplo de llamada (plantilla):

```http
GET {{base_url}}/<ruta-de-verificacion>
Authorization: ******
```

Sustituya la ruta de ejemplo por la ruta real definida en la API.

### Listar usuarios

Operación destinada a consultar o listar los usuarios registrados.

| Propiedad | Valor |
|---|---|
| Nombre en Postman | Listar Usuarios |
| Método registrado | `GET` |
| URL | Pendiente de configurar |
| Autenticación | `******` |
| Parámetros | No especificados |
| Cuerpo de la solicitud | No especificado |
| Estructura de respuesta | No documentada |

Ejemplo de llamada (plantilla):

```http
GET {{base_url}}/<ruta-de-usuarios>
Authorization: ******
```

### Crear un usuario

Operación identificada en Postman como destinada a crear un usuario.

| Propiedad | Valor |
|---|---|
| Nombre en Postman | Crear un Usuario |
| Método registrado | `GET` |
| URL | Pendiente de configurar |
| Autenticación | `******` |
| Parámetros | No especificados |
| Cuerpo de la solicitud | No especificado |
| Estructura de respuesta | No documentada |

> **Importante:** aunque el nombre indica una operación de creación, la colección registra el método `GET`. Verifique el método implementado por la API antes de documentar o utilizar esta operación como una creación de recursos. No se debe asumir un método `POST` sin comprobarlo.

Ejemplo de llamada (plantilla; método por verificar):

```http
GET {{base_url}}/<ruta-de-creacion-de-usuario>
Authorization: ******
```

### Reporte de marcas con ventas

Operación identificada para consultar un reporte de marcas con información de ventas.

| Propiedad | Valor |
|---|---|
| Nombre en Postman | Probar el Reporte de Marcas con Ventas |
| Método registrado | `GET` |
| URL | Pendiente de configurar |
| Autenticación | `******` |
| Parámetros | No especificados |
| Cuerpo de la solicitud | No especificado |
| Estructura de respuesta | No documentada |

Ejemplo de llamada (plantilla):

```http
GET {{base_url}}/<ruta-reporte-marcas-ventas>
Authorization: ******
```

### Reporte de stock restante

Operación identificada para consultar un reporte del stock restante.

| Propiedad | Valor |
|---|---|
| Nombre en Postman | Probar el Reporte de Stock Restante |
| Método registrado | `GET` |
| URL | Pendiente de configurar |
| Autenticación | `******` |
| Parámetros | No especificados |
| Cuerpo de la solicitud | No especificado |
| Estructura de respuesta | No documentada |

Ejemplo de llamada (plantilla):

```http
GET {{base_url}}/<ruta-reporte-stock-restante>
Authorization: ******
```

### Reporte del top 5 de marcas

Operación identificada para consultar un reporte con las cinco marcas principales.

| Propiedad | Valor |
|---|---|
| Nombre en Postman | Probar el Reporte del Top 5 Marcas |
| Método registrado | `GET` |
| URL | Pendiente de configurar |
| Autenticación | `******` |
| Parámetros | No especificados |
| Cuerpo de la solicitud | No especificado |
| Estructura de respuesta | No documentada |

Ejemplo de llamada (plantilla):

```http
GET {{base_url}}/<ruta-reporte-top-5-marcas>
Authorization: ******
```

## Resumen de endpoints

| # | Operación | Método registrado | Ruta |
|---:|---|---|---|
| 1 | Verificar que la API responde | `GET` | Pendiente |
| 2 | Listar Usuarios | `GET` | Pendiente |
| 3 | Crear un Usuario | `GET` | Pendiente; método por verificar |
| 4 | Reporte de Marcas con Ventas | `GET` | Pendiente |
| 5 | Reporte de Stock Restante | `GET` | Pendiente |
| 6 | Reporte del Top 5 Marcas | `GET` | Pendiente |

## Códigos HTTP

La colección no incluye ejemplos de respuestas ni códigos de estado. Los códigos que se muestran a continuación son referencias generales para completar esta sección cuando se conozca el comportamiento real de la API; no son resultados verificados de las solicitudes.

| Código | Significado general |
|---|---|
| `200 OK` | Solicitud procesada correctamente. |
| `201 Created` | Recurso creado correctamente. |
| `400 Bad Request` | La solicitud contiene datos incorrectos o incompletos. |
| `401 Unauthorized` | Falta autenticación o el token no es válido. |
| `403 Forbidden` | El usuario autenticado no tiene permisos suficientes. |
| `404 Not Found` | No se encontró la ruta o el recurso solicitado. |
| `500 Internal Server Error` | Error interno del servidor. |

## Cómo importar y probar la colección en Postman

1. Abra Postman.
2. Seleccione **Import**.
3. Elija el archivo `Proyecto 2.postman_collection.json`.
4. Abra la colección **Proyecto 2**.
5. Configure la autenticación `******` con un token válido y seguro.
6. Configure la URL de cada solicitud, ya que en el archivo original están vacías.
7. Ejecute las solicitudes y registre los códigos HTTP y las respuestas reales.
8. Complete esta documentación con los parámetros, cuerpos y ejemplos obtenidos.

## Información pendiente

Para convertir este documento preliminar en una referencia funcional y completa, se necesita:

- URL base de la API y ruta de cada endpoint.
- Confirmación del método HTTP correcto para cada operación, especialmente **Crear un Usuario**.
- Parámetros de ruta y de consulta, si existen.
- Estructura del cuerpo de las solicitudes, si corresponde.
- Campos obligatorios y tipos de datos para crear usuarios.
- Ejemplos reales de respuestas exitosas y de error.
- Códigos HTTP devueltos por cada operación.
- Reglas de autorización y permisos requeridos.

## Licencia y mantenimiento

La colección original no especifica una licencia ni información de versiones de la API. Agregue aquí la licencia del proyecto, el responsable del mantenimiento y la versión de la API cuando esos datos estén definidos.

## Front-end

El front-end web independiente está en [`FRONTEND/`](./FRONTEND/). Para iniciar la API, servir la interfaz, configurar CORS y utilizar las operaciones CRUD de productos y reportes, consulta las [instrucciones de ejecución](./FRONTEND/README.md).
