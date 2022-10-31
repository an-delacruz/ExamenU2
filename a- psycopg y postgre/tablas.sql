create database examen;
--use in postgresql
use examen;

-- PostrgreSQL
create table if not exists contrato(
    id serial primary key,
    no_contrato serial not null,
    costo integer not null,
    fecha_inicio date not null,
    fecha_fin date not null
)

create table if not exists persona(
    id serial primary key,
    nombre varchar(50) not null,
    edad integer not null,
    correo varchar(50) not null unique
)

create table if not exists contrato_persona(
    id serial primary key,
    id_contrato integer not null,
    id_persona integer not null,
    foreign key (id_contrato) references contrato(id),
    foreign key (id_persona) references persona(id)
)