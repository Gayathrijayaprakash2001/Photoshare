# Photoshare

A full‑stack web app that lets users upload, categorize, and browse photos through a sleek, responsive interface.

1) Back‑end: Django 5 handles routing, business logic, and file uploads. Images are stored in the server’s media directory, while metadata is saved in MySQL for fast, reliable querying.

2) Database schema:
* Category (id, name) – simple table for image tags.
* Photo (id, image path, description, category_id FK, created_at).

3) Front‑end: Pure HTML templating with Bootstrap 5 components. The gallery is rendered as horizontal, scrollable cards; each card shows a thumbnail, description, and a “View” button that opens a detailed page for the photo.

Key features:
* Add Photo form – drag‑and‑drop or file picker, choose existing category or create one inline.
* Dynamic filtering – sidebar lists categories; clicking filters the gallery without reloading (Ajax enhancement optional).
* Responsive design – looks great on desktop and mobile thanks to Bootstrap’s grid and utility classes.
* Secure uploads – CSRF protection, server‑side file‑type/size checks, and unique filenames to prevent collisions.
* Exensible auth – ready for Django’s built‑in authentication so only logged‑in users can add, edit, or delete photos.

