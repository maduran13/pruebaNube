# Proyecto-Grupo29-202120

### Requisitos

* Instalación de  [Python](https://www.python.org/)
* Instalación de  [Redis](https://redis.io/)
* Instalación de  [Celery](https://docs.celeryproject.org/en/stable/)
```
cd Proyecto-Grupo29-202120/
pip install -r flaskr/requirements.txt
```
* Instalación de  python3.8-venv
`apt install python3.8-venv`

#### Ejecución BackEnd

`flask run`

### Ejecucion en el servidor

```
Comandos:

Listar servicios en systemctl: 
* systemctl list-units --type=service

Enable, Restart, Start o Stop servicio backend:
* sudo systemctl enable backend.service
* sudo systemctl start backend.service
* sudo systemctl restart backend.service
* sudo systemctl stop backend.service

Daemon reload:
* sudo systemctl daemon-reload


Ver logs servicio backend:
* journalctl -u backend

Borrado de logs:
* sudo journalctl --rotate
* sudo journalctl --vacuum-time=1s

Service Systemd file:

* sudo vi /etc/systemd/system/backend.service
```

### Construcción de Systemd BackEnd

```
[Unit]
Description=BackEnd web application
After=network.target

[Service]
User=estudiante
WorkingDirectory=/home/estudiante/Workspaces/Proyecto-Grupo29-202120
Environment=FLASK_APP=app.py
Environment=FLASK_DEBUG=1
Environment=FLASK_ENV=development
ExecStart=/home/estudiante/Workspaces/Proyecto-Grupo29-202120/venv/bin/flask run -h 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

### Construcción de Systemd Celery

```
[Unit]
Description=Celery application
After=network.target

[Service]
User=estudiante
WorkingDirectory=/home/estudiante/Workspaces/Proyecto-Grupo29-202120/flaskr
ExecStart=/home/estudiante/Workspaces/Proyecto-Grupo29-202120/venv/bin/celery -A tasks worker -l info
Restart=always

[Install]
WantedBy=multi-user.target
```

### Construcción de Systemd Celery Beat

```
[Unit]
Description=Celery Beat application
After=network.target

[Service]
User=estudiante
WorkingDirectory=/home/estudiante/Workspaces/Proyecto-Grupo29-202120/flaskr
ExecStart=/home/estudiante/Workspaces/Proyecto-Grupo29-202120/venv/bin/celery -A tasks beat
Restart=always

[Install]
WantedBy=multi-user.target
```
#   p r u e b a N u b e  
 