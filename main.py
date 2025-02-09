from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import data_input, score_calculation, visualization, export

app = FastAPI()

# Enable CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dynamic-scorecard-frontend.vercel.app",  # Your Vercel frontend URL
        "http://localhost:3000"  # Localhost for testing (optional)
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include Routers
app.include_router(data_input.router)
app.include_router(score_calculation.router)
app.include_router(visualization.router)
app.include_router(export.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Dynamic Scorecard Tool is running"}
