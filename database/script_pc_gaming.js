
// ==========================================
// 1. SELECCIÓN DE LA BASE DE DATOS
// ==========================================
db = db.getSiblingDB('pc_gaming_db');

// Limpieza de colecciones previas
db.usuarios.drop();
db.marcas.drop();
db.productos.drop();
db.ventas.drop();

// ==========================================
// 2. OPERACIONES CRUD: COLECCIÓN USUARIOS
// ==========================================

// Insertar un usuario
db.usuarios.insertOne({
  _id: ObjectId("65f1a2b3c4d5e6f7a8b9c011"),
  nombre: "Esteban Quirós",
  email: "esteban.quiros@email.com",
  rol: "Cliente",
  activo: true
});

// Insertar varios usuarios
db.usuarios.insertMany([
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c012"),
    nombre: "Valeria Hernández",
    email: "valeria.h@email.com",
    rol: "Cliente",
    activo: true
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c013"),
    nombre: "Gabriel Solano",
    email: "gabriel.s@email.com",
    rol: "Administrador",
    activo: true
  }
]);

// Actualizar un usuario
db.usuarios.updateOne(
  { email: "esteban.quiros@email.com" },
  { $set: { rol: "Vendedor" } }
);

// Eliminar un usuario
db.usuarios.deleteOne({ email: "valeria.h@email.com" });


// ==========================================
// 3. OPERACIONES CRUD: COLECCIÓN MARCAS
// ==========================================

// Insertar una marca
db.marcas.insertOne({
  _id: ObjectId("65f1a2b3c4d5e6f7a8b9c021"),
  nombre: "ASUS ROG",
  pais_origen: "Taiwán",
  estado: "Activo"
});

// Insertar varias marcas
db.marcas.insertMany([
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c022"),
    nombre: "Corsair",
    pais_origen: "EEUU",
    estado: "Activo"
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c023"),
    nombre: "Logitech G",
    pais_origen: "Suiza",
    estado: "Activo"
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c024"),
    nombre: "Razer",
    pais_origen: "EEUU",
    estado: "Activo"
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c025"),
    nombre: "MSI",
    pais_origen: "Taiwán",
    estado: "Activo"
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c026"),
    nombre: "HyperX",
    pais_origen: "EEUU",
    estado: "Inactivo"
  }
]);

// Actualizar una marca
db.marcas.updateOne(
  { nombre: "HyperX" },
  { $set: { estado: "Activo" } }
);

// Eliminar una marca
db.marcas.deleteOne({ nombre: "HyperX" });


// ==========================================
// 4. OPERACIONES CRUD: COLECCIÓN PRODUCTOS
// ==========================================

// Insertar un producto
db.productos.insertOne({
  _id: ObjectId("65f1a2b3c4d5e6f7a8b9c031"),
  nombre: "Tarjeta de Video RTX 4070 12GB",
  marca_id: ObjectId("65f1a2b3c4d5e6f7a8b9c021"),
  marca_nombre: "ASUS ROG",
  categoria: "Componentes",
  precio: 450000,
  stock: 10
});

// Insertar varios productos
db.productos.insertMany([
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c032"),
    nombre: "Teclado Mecánico K70 RGB PRO",
    marca_id: ObjectId("65f1a2b3c4d5e6f7a8b9c022"),
    marca_nombre: "Corsair",
    categoria: "Periféricos",
    precio: 95000,
    stock: 25
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c033"),
    nombre: "Mouse Inalámbrico G Pro X Superlight",
    marca_id: ObjectId("65f1a2b3c4d5e6f7a8b9c023"),
    marca_nombre: "Logitech G",
    categoria: "Periféricos",
    precio: 85000,
    stock: 18
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c034"),
    nombre: "Audífonos BlackShark V2 Pro",
    marca_id: ObjectId("65f1a2b3c4d5e6f7a8b9c024"),
    marca_nombre: "Razer",
    categoria: "Audio",
    precio: 110000,
    stock: 15
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c035"),
    nombre: "Tarjeta Madre MAG B650 Tomahawk",
    marca_id: ObjectId("65f1a2b3c4d5e6f7a8b9c025"),
    marca_nombre: "MSI",
    categoria: "Componentes",
    precio: 165000,
    stock: 8
  }
]);

// Actualizar un producto
db.productos.updateOne(
  { nombre: "Tarjeta de Video RTX 4070 12GB" },
  { $set: { precio: 435000, stock: 12 } }
);

// Eliminar un producto
db.productos.deleteOne({ _id: ObjectId("65f1a2b3c4d5e6f7a8b9c035") });


// ==========================================
// 5. OPERACIONES CRUD: COLECCIÓN VENTAS
// ==========================================

// Insertar una venta
db.ventas.insertOne({
  _id: ObjectId("65f1a2b3c4d5e6f7a8b9c041"),
  fecha: ISODate("2026-03-15T10:00:00Z"),
  usuario_id: ObjectId("65f1a2b3c4d5e6f7a8b9c011"),
  detalles: [
    {
      producto_id: ObjectId("65f1a2b3c4d5e6f7a8b9c031"),
      producto_nombre: "Tarjeta de Video RTX 4070 12GB",
      marca_nombre: "ASUS ROG",
      cantidad: 1,
      precio_unitario: 435000,
      subtotal: 435000
    }
  ],
  total: 435000
});

// Insertar varias ventas
db.ventas.insertMany([
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c042"),
    fecha: ISODate("2026-03-15T15:30:00Z"),
    usuario_id: ObjectId("65f1a2b3c4d5e6f7a8b9c011"),
    detalles: [
      {
        producto_id: ObjectId("65f1a2b3c4d5e6f7a8b9c032"),
        producto_nombre: "Teclado Mecánico K70 RGB PRO",
        marca_nombre: "Corsair",
        cantidad: 2,
        precio_unitario: 95000,
        subtotal: 190000
      },
      {
        producto_id: ObjectId("65f1a2b3c4d5e6f7a8b9c033"),
        producto_nombre: "Mouse Inalámbrico G Pro X Superlight",
        marca_nombre: "Logitech G",
        cantidad: 1,
        precio_unitario: 85000,
        subtotal: 85000
      }
    ],
    total: 275000
  },
  {
    _id: ObjectId("65f1a2b3c4d5e6f7a8b9c043"),
    fecha: ISODate("2026-03-16T11:00:00Z"),
    usuario_id: ObjectId("65f1a2b3c4d5e6f7a8b9c013"),
    detalles: [
      {
        producto_id: ObjectId("65f1a2b3c4d5e6f7a8b9c034"),
        producto_nombre: "Audífonos BlackShark V2 Pro",
        marca_nombre: "Razer",
        cantidad: 3,
        precio_unitario: 110000,
        subtotal: 330000
      }
    ],
    total: 330000
  }
]);

// Actualizar una venta
db.ventas.updateOne(
  { _id: ObjectId("65f1a2b3c4d5e6f7a8b9c041") },
  { $set: { estado_pago: "Completado" } }
);

// Eliminar una venta
db.ventas.deleteOne({ _id: ObjectId("65f1a2b3c4d5e6f7a8b9c043") });


// ==========================================
// 6. CONSULTAS DE LECTURA (SELECTS / AGGREGATIONS)
// ==========================================

// Obtener la cantidad vendida de productos por fecha y filtrarla con una fecha específica (2026-03-15)
db.ventas.aggregate([
  {
    $match: {
      fecha: {
        $gte: ISODate("2026-03-15T00:00:00Z"),
        $lt: ISODate("2026-03-16T00:00:00Z")
      }
    }
  },
  { $unwind: "$detalles" },
  {
    $group: {
      _id: { $dateToString: { format: "%Y-%m-%d", date: "$fecha" } },
      total_productos_vendidos: { $sum: "$detalles.cantidad" }
    }
  }
]);

// Obtener la lista de todas las marcas que tienen al menos una venta
db.ventas.aggregate([
  { $unwind: "$detalles" },
  {
    $group: {
      _id: "$detalles.marca_nombre"
    }
  },
  {
    $project: {
      _id: 0,
      marca: "$_id"
    }
  }
]);

// Obtener productos vendidos y su cantidad restante en stock
db.ventas.aggregate([
  { $unwind: "$detalles" },
  {
    $group: {
      _id: "$detalles.producto_id",
      nombre_producto: { $first: "$detalles.producto_nombre" },
      cantidad_vendida: { $sum: "$detalles.cantidad" }
    }
  },
  {
    $lookup: {
      from: "productos",
      localField: "_id",
      foreignField: "_id",
      as: "info_producto"
    }
  },
  { $unwind: "$info_producto" },
  {
    $project: {
      _id: 1,
      nombre_producto: 1,
      cantidad_vendida: 1,
      stock_restante: "$info_producto.stock"
    }
  }
]);

// Obtener listado de las 5 marcas más vendidas y su cantidad de ventas
db.ventas.aggregate([
  { $unwind: "$detalles" },
  {
    $group: {
      _id: "$detalles.marca_nombre",
      total_unidades_vendidas: { $sum: "$detalles.cantidad" }
    }
  },
  { $sort: { total_unidades_vendidas: -1 } },
  { $limit: 5 }
]);