FROM maiv/ainizetest:1

LABEL Antoine Vignon <vignonantoinem@gmail.com>

WORKDIR /project

RUN pip install flask transformers torch mediapipe streamlit

COPY . .

CMD ["python3", "server.py"]

