from Repository.intervention_repository import InterventionRepository


class InterventionGetAllUseCase:
    def __init__(self, repo: InterventionRepository):
        self.session = None
        self.repository = repo

    def execute(self):
        return self.repository.get_all()
