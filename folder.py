from pathlib import Path

ROOT = Path("practice")

DIRECTORIES = [
    "python/algorithms",
    "python/asyncio",
    "python/typing",
    "python/design_patterns",

    "backend/fastapi",
    "backend/sqlalchemy",
    "backend/redis",
    "backend/docker",
    "backend/testing",

    "ai_backend/rag",
    "ai_backend/embeddings",
    "ai_backend/vector_db",
    "ai_backend/chunking",
    "ai_backend/llm_serving",

    "system_design/rate_limiter",
    "system_design/task_queue",
    "system_design/pubsub",
    "system_design/caching",
]

for directory in DIRECTORIES:
    path = ROOT / directory
    path.mkdir(parents=True, exist_ok=True)

    # Keep empty directories tracked by Git
    (path / ".gitkeep").touch(exist_ok=True)

readme = ROOT / "README.md"

readme.write_text(
    """# Practice Repository

Daily backend engineering, AI backend, system design, and Python practice.

## Structure

### Python
- Algorithms
- Asyncio
- Typing
- Design Patterns

### Backend
- FastAPI
- SQLAlchemy
- Redis
- Docker
- Testing

### AI Backend
- RAG
- Embeddings
- Vector Databases
- Chunking
- LLM Serving

### System Design
- Rate Limiter
- Task Queue
- Pub/Sub
- Caching
""",
    encoding="utf-8",
)

print("Repository structure created successfully.")