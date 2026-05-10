# Start the Web Dashboard

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API and Web dashboard:

```bash
python -m uvicorn api_server:app --reload
```

Open:

```text
http://127.0.0.1:8000/
```

Windows helper:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start_web_ui.ps1
```
