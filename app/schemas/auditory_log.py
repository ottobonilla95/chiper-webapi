from ma import ma
from models.auditory_log import AuditoryLogModel

class AuditoryLogSchema (ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuditoryLogModel
        load_instance = True