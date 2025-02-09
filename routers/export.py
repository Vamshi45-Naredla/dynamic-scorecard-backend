from fastapi import APIRouter
from database import fake_db  # Import in-memory storage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/export_pdf")
async def export_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.drawString(100, 750, "Performance Scorecard")

    y = 730
    for item in fake_db:
        pdf.drawString(100, y, f"{item.name}: {item.score}")
        y -= 20

    pdf.save()
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=scorecard.pdf"})
