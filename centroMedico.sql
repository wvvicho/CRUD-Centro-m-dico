CREATE DATABASE IF NOT EXISTS CentroMedico CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
CREATE USER IF NOT EXISTS 'adminSalud'@'localhost' IDENTIFIED BY 'SaludVida';
GRANT ALL PRIVILEGES ON CentroMedico.* TO 'adminSalud'@'localhost'; 