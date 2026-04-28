const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "1234",
    database: "hotel"
});

// Generar conexion a la BD
db.connect(err => {
    if (err) throw err;
    console.log("Conectado a BD");
});


// Registrar cliente
app.post('/cliente', (req, res) => {
    const { cliente_id, nombre, apellido, correo_electronico, telefono } = req.body;

    const sql = `
    INSERT INTO cliente 
    (cliente_id, nombre, apellido, correo_electronico, telefono) 
    VALUES (?, ?, ?, ?, ?)
    `;

    db.query(sql, [cliente_id, nombre, apellido, correo_electronico, telefono],
        (err, result) => {
            if (err) return res.send(err);
            res.send("Cliente registrado");
        });
});


// Crear reserva
app.post('/reserva', (req, res) => {
    const { cliente_id, habitacion_id, fecha_entrada, fecha_salida, cantidad_personas } = req.body;

    const sql = `
    INSERT INTO reserva 
    (cliente_cliente_id, habitacion_habitacion_id, fecha_entrada, fecha_salida, cantidad_personas)
    VALUES (?, ?, ?, ?, ?)
    `;

    db.query(sql, [cliente_id, habitacion_id, fecha_entrada, fecha_salida, cantidad_personas],
        (err, result) => {
            if (err) return res.send(err);
            res.send("Reserva creada");
        });
});

// Busca al cliente registrado
app.post('/login', (req, res) => {
    const { correo } = req.body;

    const sql = "SELECT * FROM cliente WHERE correo_electronico = ?";

    db.query(sql, [correo], (err, result) => {
        if (err) return res.send(err);

        if (result.length > 0){
            res.send("Login correcto");
        } else {
            res.send("Usuario no existe");
        }
    });
});

// Ver las reservas
app.get('/reservas', (req, res) => {
    db.query("SELECT * FROM reserva", (err, result) => {
        if (err) return res.send(err);
        res.json(result);
    });
});

app.listen(3000, () => {
    console.log("Servidor corriendo en puerto 3000");
});