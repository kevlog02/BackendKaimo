import os
import google.generativeai as genai
from typing import List, Dict
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("WARNING: GEMINI_API_KEY no encontrada en .env")

class GeminiService:
    """Servicio para generar respuestas con Gemini AI"""
    
    def __init__(self):
        if GEMINI_API_KEY:
            self.model = genai.GenerativeModel('gemini-pro')
            self.enabled = True
        else:
            self.model = None
            self.enabled = False
    
    def generate_message_suggestions(self, context: str, conversation_history: List[Dict] = None) -> List[str]:
        """Generar sugerencias de mensajes"""
        if not self.enabled:
            return self._get_default_suggestions()
        
        prompt = f"""Eres un asistente que ayuda a clientes a comunicarse con técnicos de servicios del hogar.

Contexto: {context}

Genera 3 sugerencias de mensajes cortos y profesionales que el cliente podría enviar al técnico. 
Cada mensaje debe ser:
- Claro y directo
- Profesional pero amigable
- Máximo 2-3 líneas
- En español

Formato: Devuelve solo las 3 sugerencias separadas por "|||" sin numeración ni viñetas.

Ejemplo de formato de respuesta:
Hola, ¿podrías darme un presupuesto para reparar una tubería?|||Me interesa contratar tus servicios, ¿cuándo tienes disponibilidad?|||¿Cuánto cobrarías por una revisión general?
"""
        
        try:
            response = self.model.generate_content(prompt)
            suggestions_text = response.text.strip()
            suggestions = [s.strip() for s in suggestions_text.split("|||")]
            return suggestions[:3]
        except Exception as e:
            print(f"Error generando sugerencias: {e}")
            return self._get_default_suggestions()
    
    def generate_smart_reply(self, last_message: str, user_role: str) -> str:
        """Generar una respuesta inteligente"""
        if not self.enabled:
            return "Gracias por tu mensaje. Me pondré en contacto contigo pronto."
        
        role_context = "técnico" if user_role == "technician" else "cliente"
        
        prompt = f"""Eres un asistente que ayuda a {role_context}s a responder mensajes de manera profesional.

Mensaje recibido: "{last_message}"

Genera UNA respuesta profesional, cordial y útil en español. La respuesta debe ser:
- Directa y clara (máximo 2-3 líneas)
- Profesional pero amigable
- Relevante al mensaje recibido

Devuelve SOLO la respuesta, sin explicaciones adicionales.
"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error generando respuesta: {e}")
            return "Gracias por tu mensaje. Me pondré en contacto contigo pronto."
    
    def generate_service_description(self, category: str, brief_description: str) -> str:
        """Generar una descripción detallada de servicio"""
        if not self.enabled:
            return brief_description
        
        prompt = f"""Mejora la siguiente descripción de un servicio de {category}:

Descripción original: {brief_description}

Genera una descripción más clara, profesional y detallada que incluya:
- Qué se necesita específicamente
- Detalles importantes para el técnico
- Máximo 3-4 líneas

Devuelve SOLO la descripción mejorada en español, sin títulos ni formato adicional.
"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error mejorando descripción: {e}")
            return brief_description
    
    def _get_default_suggestions(self) -> List[str]:
        """Sugerencias por defecto cuando Gemini no está disponible"""
        return [
            "Hola, me interesa contratar tus servicios. ¿Podrías darme más información?",
            "¿Cuál es tu disponibilidad para realizar este trabajo?",
            "¿Podrías darme un presupuesto aproximado?"
        ]

# Instancia global del servicio
gemini_service = GeminiService()