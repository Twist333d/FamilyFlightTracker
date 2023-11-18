from pydantic import BaseModel, Field

class FlightData(BaseModel):
    flight_number: str = Field(..., pattern="^[A-Za-z]{2}\d{1,4}$")

