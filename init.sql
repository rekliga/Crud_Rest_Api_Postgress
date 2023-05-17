-- Creamos la base de datos que usara la api
-- Insertar un ejemplo de usuario 
--INSERT INTO usuarios (nombre, email, imagen)
--VALUES ('Juan', 'juan@example.com', pg_read_binary_file('C:/ruta/a/la/imagen.jpg'));
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    password VARCHAR(100),
    email VARCHAR(100),
    imagen BYTEA
);



-- Crear la tabla publicaciones
CREATE TABLE publicaciones (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    priority INTEGER,
    status VARCHAR(50),
    time_since_published INTERVAL,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES usuarios (id)
);

---- Insertar un ejemplo de publicación INSERT INTO publicaciones (title, description, priority, status, time_since_published, user_id) VALUES ('Título de ejemplo', 'Descripción de ejemplo', 1, 'Activo', INTERVAL '2 days', 1);





