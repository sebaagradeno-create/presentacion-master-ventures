# Presentación Master Ventures 2.0

Ecosistema Inmobiliario, Constructivo & IA — Automatizame.uy

## ?? URL de Producción (Única)
- [https://presentacion.automatizameuy.com](https://presentacion.automatizameuy.com)

## ?? Estructura del Proyecto
- `public/index.html` — Landing page interactiva y presentación ejecutiva.
- `public/audios/` — Audios interactivos de los perfiles (inversor, comprador, inmobiliaria).
- `docker-compose.yml` — Configuración Nginx para despliegue en VPS (puerto 8765).

## ?? Despliegue en Servidor VPS
El sitio corre bajo un contenedor Docker con Nginx (`master-ventures-presentation`) y ruteado con proxy Traefik SSL.
