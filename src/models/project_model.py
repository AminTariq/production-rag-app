from .base_data_model import BaseDataModel
from .db_schemas import Project
from .enums.database_enums import DatabaseEnum


class ProjectModel(BaseDataModel):
    
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.dbclient[DatabaseEnum.COLLECTION_PROJECT_NAME.value]
    
    async def create_project(self, project: Project):
        
        result = await self.collection.insert_one(project.dict())
        project = result.inserted_id
        return project