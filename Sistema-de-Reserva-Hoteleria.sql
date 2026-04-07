-- Borrado de Tablas
DROP TABLE transaccion CASCADE CONSTRAINTS;
DROP TABLE metodo_pago CASCADE CONSTRAINTS;
DROP TABLE metodo_pago CASCADE CONSTRAINTS;
DROP TABLE reserva CASCADE CONSTRAINTS;
DROP TABLE cliente CASCADE CONSTRAINTS;
DROP TABLE habitacion CASCADE CONSTRAINTS;
DROP TABLE hotel CASCADE CONSTRAINTS;


-- Creación de Tablas

CREATE TABLE hotel
(
    hotel_id NUMERIC(4),
    nombre VARCHAR2(30) NOT NULL,
    direccion VARCHAR2(50) NOT NULL,
    catego VARCHAR(30) NOT NULL,
    CONSTRAINT pk_hot_id PRIMARY KEY (hotel_id)
);

CREATE TABLE habitacion
(
    habitacion_id NUMERIC(3),
    hotel_hotel_id NUMERIC(4) NOT NULL,
    tipo VARCHAR2(2) NOT NULL,
    capacidad NUMERIC(2) NOT NULL,
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

COMMIT;
