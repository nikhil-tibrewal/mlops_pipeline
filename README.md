# End-to-End MLOps Pipeline on GCP using Airflow, sklearn and MLFlow

---

## Architecture Overview

```mermaid
graph TD
    A[User Query] --> B[Streamlit Interface]
    B --> C[LangChain Retriever]
    C --> D[FAISS Vectorstore]
    D --> E[Relevant Context Chunks]
    E --> F[OpenAI LLM]
    F --> G[Response]
    G --> B
```

Stack:
- Airflow to orchestrate a pipeline
- sklearn to train a simple classification model
- MLflow to log model + metrics
- MLflow Serve to deploy the trained model as a REST API
