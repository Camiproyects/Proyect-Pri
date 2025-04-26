## config.py
# Configuración global del sistema

WHATSAPP_NUMERO_ADMIN = "+573101234567"  # Número donde se enviarán alertas
RESPALDO_HORA = "03:45"  # Hora de respaldo automático

# Configuración de OCR
OCR_MODEL = "EasyOCR"  # Modelo OCR utilizado
IDIOMA_OCR = "es"  # Idioma del OCR

# Configuración de WhatsApp
WHATSAPP_API_URL = "https://api.whatsapp.com/send"  # API de WhatsApp
47
5
# Configuración de informes
HORARIO_INFORME_DIARIO = "20:00"  # Hora de envío del informe diario
HORARIO_INFORME_SEMANAL = "08:00"  # Hora de envío del informe semanal (sábado)

## captura_ocr.py
# Módulo de captura de datos desde la cámara
import cv2
import easyocr

def capturar_frame():
    """Captura un frame desde la cámara del teléfono."""
    cap = cv2.VideoCapture(0)  # Conectar a la cámara
    ret, frame = cap.read()
    cap.release()
    if ret:
        return frame
    return None

def procesar_ocr(frame):
    """Procesa la imagen capturada y extrae texto manuscrito."""
    reader = easyocr.Reader([IDIOMA_OCR])
    resultado = reader.readtext(frame, detail=0)
    return resultado

if __name__ == "__main__":
    frame = capturar_frame()
    if frame is not None:
        texto = procesar_ocr(frame)
        print("Texto detectado:", texto)
