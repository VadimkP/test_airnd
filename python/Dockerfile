FROM python:3.10 AS main
COPY python/requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10-slim
WORKDIR /app

COPY --from=main /root/.local /root/.local
COPY ./python .
ENV PATH=/root/.local:$PATH

CMD ["python3", "-u", "app.py"]