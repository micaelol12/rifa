# Este arquivo torna 'routers' um pacote Python.
from .rifa_router import router as rifa_router
from .numeros_router import router as numeros_router

__all__ = ['rifa_router','numeros_router']