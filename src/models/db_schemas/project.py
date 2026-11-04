from bson.objectid import ObjectId
from pydantic import BaseModel, Field, field_validator


class Project(BaseModel):
    _id: ObjectId | None
    project_id: str = Field(..., min_length=1)
    
    @field_validator("project_id")
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError("project_id cannot be empty or whitespace")
        
        return value
    
    class Config:
        arbitrary_types_allowed = True