const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const path = require('path');

// Esto le dice a Express que entregue los archivos de estas carpetas automáticamente
app.use('/CSS', express.static(path.join(__dirname, '../CSS')));
app.use('/assets', express.static(path.join(__dirname, '../assets')));
app.use(express.static(path.join(__dirname, '../frontend')));

/*//imagen de habitacione en reserva 
function actualizarPreview() {
    const id = document.getElementById("habitacion_id").value;
    const imgElement = document.getElementById("room-img");
    const titleElement = document.getElementById("room-title");
    const descElement = document.getElementById("room-desc");

    // "Diccionario" de habitaciones
    const habitaciones = {
        "1": { nombre: "Suite Junior", img: "suite1.png", precio: "$100" },
        "2": { nombre: "Suite Ejecutiva", img: "suite2.png", precio: "$150" },
        "3": { nombre: "Suite Presidencial", img: "suite3.png", precio: "$250" },
        "4": { nombre: "Suite Familiar", img: "suite4.png", precio: "$180" },
        "5": { nombre: "Suite Master", img: "suite5.png", precio: "$200" }
    };

    if (habitaciones[id]) {
        imgElement.src = `../assets/imagen/${habitaciones[id].img}`;
        titleElement.innerText = habitaciones[id].nombre;
        descElement.innerText = `Precio sugerido: ${habitaciones[id].precio} por noche`;
    } else {
        // Estado por defecto si el ID no existe
        imgElement.src = "../assets/iconos/icono1.png"; 
        titleElement.innerText = "Habitación no encontrada";
        descElement.innerText = "Ingresa un ID del 1 al 5";
    }
}*/



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

/*/// Ver las reservas
app.get('/reservas', (req, res) => {
    db.query("SELECT * FROM reserva", (err, result) => {
        if (err) return res.send(err);
        res.json(result);
    });
});

app.listen(3000, () => {
    console.log("Servidor corriendo en puerto 3000");
});*/