from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    apellido: Optional[str] = None
    email: EmailStr
    password: str = Field(min_length=3)
    
class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"