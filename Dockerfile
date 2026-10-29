# 1. 使用 Python 3.11 作為基礎 Image
FROM python:3.11-slim

# 2. 設定容器內的工作目錄
WORKDIR /app

# 3. 複製依賴清單
COPY requirements.txt .

# 4. 安裝 Python 套件
RUN python -m pip install --no-cache-dir -r requirements.txt

# 5. 複製應用程式
COPY app/ ./app/

# 6. 建立非 root 使用者
RUN useradd --create-home appuser \
    && chown -R appuser:appuser /app

# 7. 使用非 root 使用者執行程式
USER appuser

# 8. 宣告應用程式使用的連接埠
EXPOSE 8000

# 9. 啟動 FastAPI
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]