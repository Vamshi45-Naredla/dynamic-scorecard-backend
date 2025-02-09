from fastapi import APIRouter
import matplotlib.pyplot as plt
import matplotlib
import io
from fastapi.responses import StreamingResponse
from database import fake_db  # ✅ Use in-memory list instead of MongoDB

matplotlib.use("Agg")  # ✅ Fix Matplotlib backend

router = APIRouter()

@router.get("/visualize_scores")
async def visualize_scores():
    try:
        # ✅ Fetch scores from in-memory list
        if not fake_db:
            return {"error": "No data available"}

        names = [item["name"] for item in fake_db]
        values = [item["score"] for item in fake_db]

        # ✅ Generate bar chart
        plt.figure(figsize=(6, 4))
        plt.bar(names, values, color="skyblue")
        plt.xlabel("Names")
        plt.ylabel("Scores")
        plt.title("Performance Scores")

        # ✅ Save image to memory
        img = io.BytesIO()
        plt.savefig(img, format="png")
        plt.close()  # Close plot to free memory
        img.seek(0)

        return StreamingResponse(img, media_type="image/png")

    except Exception as e:
        return {"error": str(e)}
