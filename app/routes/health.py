from datetime import datetime
from fastapi import APIRouter

# from db import get_supabase_client, get_pinecone_index


router = APIRouter()


@router.get("/health")
async def health_check():
    services = {}
    
    # try:
    #     client = get_supabase_client()
    #     client.table("documents").select("id").limit(1).execute()
    #     services["supabase"] = "connected"
    # except Exception:
    #     services["supabase"] = "error"
    
    # try:
    #     get_pinecone_index()
    #     services["pinecone"] = "connected"
    # except Exception:
    #     services["pinecone"] = "error"
    
    # status = "ok" if all(v == "connected" for v in services.values()) else "degraded"
    status = "ok"
    
    return {
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "services": services
    }
