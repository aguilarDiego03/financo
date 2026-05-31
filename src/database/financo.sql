-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.4.7 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.13.0.7147
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para financo
CREATE DATABASE IF NOT EXISTS `financo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `financo`;

-- Volcando estructura para tabla financo.calculos_rendimiento
CREATE TABLE IF NOT EXISTS `calculos_rendimiento` (
  `id_calculo` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `monto_inicial` decimal(12,2) NOT NULL,
  `porcentaje_interes` decimal(5,2) NOT NULL,
  `tiempo_meses` int NOT NULL,
  `rendimiento_final` decimal(12,2) NOT NULL,
  `fecha_calculo` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_calculo`),
  KEY `fk_calculo_usuario` (`id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla financo.calculos_rendimiento: 2 rows
/*!40000 ALTER TABLE `calculos_rendimiento` DISABLE KEYS */;
INSERT INTO `calculos_rendimiento` (`id_calculo`, `id_usuario`, `monto_inicial`, `porcentaje_interes`, `tiempo_meses`, `rendimiento_final`, `fecha_calculo`) VALUES
	(1, 1, 10000.00, 8.50, 12, 10850.00, '2026-05-13 10:42:35'),
	(3, 3, 1000.00, 10.00, 12, 1100.00, '2026-05-31 16:24:36');
/*!40000 ALTER TABLE `calculos_rendimiento` ENABLE KEYS */;

-- Volcando estructura para tabla financo.metas_financieras
CREATE TABLE IF NOT EXISTS `metas_financieras` (
  `id_meta` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `nombre_meta` varchar(150) NOT NULL,
  `monto_objetivo` decimal(12,2) NOT NULL,
  `monto_actual` decimal(12,2) NOT NULL,
  `fecha_limite` date DEFAULT NULL,
  `estado` varchar(50) NOT NULL,
  PRIMARY KEY (`id_meta`),
  KEY `fk_meta_usuario` (`id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla financo.metas_financieras: 2 rows
/*!40000 ALTER TABLE `metas_financieras` DISABLE KEYS */;
INSERT INTO `metas_financieras` (`id_meta`, `id_usuario`, `nombre_meta`, `monto_objetivo`, `monto_actual`, `fecha_limite`, `estado`) VALUES
	(1, 2, 'Comprar Laptop', 25000.00, 8000.00, '2026-12-31', 'En progreso'),
	(2, 3, 'Mazatlan', 15000.00, 500.00, NULL, 'En progreso');
/*!40000 ALTER TABLE `metas_financieras` ENABLE KEYS */;

-- Volcando estructura para tabla financo.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `foto_perfil` varchar(255) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla financo.usuarios: 3 rows
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id_usuario`, `nombre`, `correo`, `contraseña`, `fecha_registro`, `foto_perfil`, `estado`) VALUES
	(1, 'Juan Perez', 'juan@gmail.com', '123456', '2026-05-13 10:42:35', NULL, 1),
	(2, 'Maria Lopez', 'maria@gmail.com', 'abcdef', '2026-05-13 10:42:35', NULL, 1),
	(3, 'Diego', 'aguil4r.dgx@gmail.com', '$2b$12$JtP.mi7ZFqM/ECRRgRR5mugMgknVlECaG2EIUFz27zoK.pvgeUgH2', '2026-05-31 16:23:24', NULL, 1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
