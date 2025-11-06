CREATE DATABASE IF NOT EXISTS CentroMedico;
CREATE USER 'adminSalud'@'localhost' IDENTIFIED BY 'SaludVida';
GRANT ALL PRIVILEGES ON CentroMedico.* TO 'adminSalud'@'localhost'; 