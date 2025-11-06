CREATE DATABASE IF NOT EXISTS CentroMedico;
CREATE USER IF NOT EXISTS 'adminSalud'@'localhost' IDENTIFIED BY 'SaludVida';
GRANT ALL PRIVILEGES ON CentroMedico.* TO 'adminSalud'@'localhost'; 