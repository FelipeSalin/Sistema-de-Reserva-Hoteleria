-- Borrado de Tablas
DROP TABLE transaccion CASCADE CONSTRAINTS;
DROP TABLE factura CASCADE CONSTRAINTS;
DROP TABLE metodo_pago CASCADE CONSTRAINTS;
DROP TABLE reserva CASCADE CONSTRAINTS;
DROP TABLE cliente CASCADE CONSTRAINTS;
DROP TABLE habitacion CASCADE CONSTRAINTS;
DROP TABLE hotel CASCADE CONSTRAINTS;


-- Creación de Tablas

CREATE TABLE hotel
(
    hotel_id NUMERIC(4),
    nombre VARCHAR2(200) NOT NULL,
    direccion VARCHAR2(50) NOT NULL,
    catego VARCHAR(30) NOT NULL,
    CONSTRAINT pk_hot_id PRIMARY KEY (hotel_id)
);

CREATE TABLE habitacion
(
    habitacion_id NUMERIC(3),
    hotel_hotel_id NUMERIC(4) NOT NULL,
    tipo VARCHAR2(50) NOT NULL,
    capacidad VARCHAR2(50) NOT NULL,
    precio NUMERIC(7) NOT NULL,
    CONSTRAINT pk_hab_id PRIMARY KEY (habitacion_id),
    CONSTRAINT fk_hab_hot FOREIGN KEY (hotel_hotel_id) REFERENCES hotel (hotel_id),
    CONSTRAINT chk_hab_tipo CHECK (tipo IN ('Turista', 'Premium'))
);

CREATE TABLE cliente
(
    cliente_id NUMERIC(4),
    nombre VARCHAR2(20) NOT NULL,
    apellido VARCHAR2(20) NOT NULL,
    correo_electronico VARCHAR2(30) NOT NULL,
    telefono VARCHAR2(12) NOT NULL,
    CONSTRAINT pk_cli_id PRIMARY KEY (cliente_id)
);

CREATE TABLE reserva
(
    reserva_id NUMERIC(4),
    cliente_cliente_id NUMERIC(4) NOT NULL,
    habitacion_habitacion_id NUMERIC(3) NOT NULL,
    fecha_entrada DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    cantidad_personas NUMERIC(2) NOT NULL,
    CONSTRAINT pk_reserva_id PRIMARY KEY (reserva_id),
    CONSTRAINT fk_reserva_clienteid FOREIGN KEY (cliente_cliente_id) REFERENCES cliente (cliente_id),
    CONSTRAINT fk_reserva_habitacionid FOREIGN KEY (habitacion_habitacion_id) REFERENCES habitacion (habitacion_id)
);

CREATE TABLE metodo_pago (
    id_metodo_pago NUMBER PRIMARY KEY,
    nombre         VARCHAR2(50) NOT NULL,
    descripcion    VARCHAR2(100) NOT NULL
);

CREATE TABLE factura (
    numfactura NUMERIC(8),
    descripcion VARCHAR2(50) NOT NULL,
    id_metodo_pago NUMBER NOT NULL,
    monto_total NUMBER NOT NULL,
    
    CONSTRAINT pk_factura_num PRIMARY KEY (numfactura),
    CONSTRAINT fk_metpag_fact FOREIGN KEY (id_metodo_pago) REFERENCES metodo_pago (id_metodo_pago)
);

CREATE TABLE transaccion (
    id_transaccion   NUMBER PRIMARY KEY,
    numfactura       NUMBER NOT NULL,
    fecha_pago       DATE NOT NULL,
    monto            NUMBER(10,2) NOT NULL,
    id_metodo_pago   NUMBER NOT NULL,
    CONSTRAINT fk_trans_factura FOREIGN KEY (numfactura) REFERENCES factura(numfactura),
    CONSTRAINT fk_trans_metodo FOREIGN KEY (id_metodo_pago) REFERENCES metodo_pago(id_metodo_pago)
);

-- Inserts

INSERT INTO hotel
    VALUES (1, 'Hotel Pacific Reef Santiago', 'Santiago 123', '4 estrellas');
INSERT INTO hotel
    VALUES (2, 'Hotel Pacific Reef Valdivia', 'Valdivia 123', '4 estrellas');
INSERT INTO hotel
    VALUES (3, 'Hotel Pacific Reef Viña del Mar', 'Viña del Mar 123', '4 estrellas');

INSERT INTO habitacion
    VALUES (001, '1', 'Turista', '4 Personas', 50000);
INSERT INTO habitacion
    VALUES (002, '2', 'Premium', '6 Personas', 100000);
INSERT INTO habitacion
    VALUES (003, '3', 'Turista', '4 Personas', 50000);
    
INSERT INTO cliente
    VALUES (100, 'Diego', 'Lorca', 'dieloco@gmail.com', '+56912345678');
INSERT INTO cliente
    VALUES (101, 'Bastián', 'Peralta', 'bastianp@gmail.com', '+56912345679');
INSERT INTO cliente
    VALUES (102, 'Alonso', 'Soto', 'alonsoto@gmail.com', '+56912345670');
    
INSERT INTO reserva
    VALUES (500, 100, 001, '20-04-2026', '24-04-2026', 4);
INSERT INTO reserva
    VALUES (501, 101, 002, '01-04-2026', '05-04-2026', 6);
INSERT INTO reserva
    VALUES (502, 102, 002, '10-03-2026', '13-03-2026', 4);
    
INSERT INTO metodo_pago
    VALUES (1, 'Tarjeta de Crédito', 'Se realiza el pago con tarjeta de crédito');
INSERT INTO metodo_pago
    VALUES (2, 'Tarjeta de Débito', 'Se realiza el pago con tarjeta de débito');
    
INSERT INTO factura
    VALUES (1000, 'Reserva de habitación por 4 días', 1, 200000);
INSERT INTO factura
    VALUES (1001, 'Reserva de habitación por 5 días', 2, 500000);
INSERT INTO factura
    VALUES (1002, 'Reserva de habitación por 3 días', 1, 150000);
    
INSERT INTO transaccion
    VALUES (50, 1000, '11-04-2026', 200000, 1);
INSERT INTO transaccion
    VALUES (51, 1001, '28-03-2026', 500000, 2);
INSERT INTO transaccion
    VALUES (52, 1002, '02-03-2026', 150000, 1);

COMMIT;
