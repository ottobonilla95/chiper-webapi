# models
from models.auditory_log import AuditoryLogModel

# schemas
from schemas.auditory_log import AuditoryLogSchema


auditory_log_Schema = AuditoryLogSchema()


class Auditory():

    @classmethod
    def log_error(cls, proccess, module,method,message):
        auditory =  auditory_log_Schema.load(
                                                {
                                                    "proccess":proccess,
                                                    "module":module,
                                                    "method":method,
                                                    "message":message
                                                }
                                            )

        auditory.save_to_db()