import pandas as pd
RESSOURCES = {'gold':0, 'solds':0}
POPULATION = {'peons':0, 'specs':0, 'elites':0, 'thieves':0, 'wizards':0}
SCIENCES = {'alchemy':0, 'tools':0, 'population':0, 'production':0, 'bookkeeping':0, 'artisan':0,
            'strategy':0, 'siege':0, 'tactician':0, 'valor':0, 'heroism':0, 'resilience':0,
            'crime':0, 'channeling':0, 'shielding':0, 'cunning':0, 'invocation':0}
BUILDINGS = {'homes':0, 'farms':0, 'mills':0, 'banks':0, 'tgs':0, 'armouries':0,
            'barracks':0, 'forts':0, 'gs':0, 'hospitals':0, 'guilds':0, 'towers':0,
            'tds':0, 'wts':0, 'universities':0, 'libraries':0, 'stables':0, 'dongeons':0}

class Province():
    def __init__(self) -> None:
        self.ressources = pd.DataFrame([RESSOURCES])
        self.population = pd.DataFrame([POPULATION])
        self.buildings = pd.DataFrame([BUILDINGS])
        self.sciences = pd.DataFrame([SCIENCES])

    def tick(self):
        pass

    def _new_births(self):
        pass

    def _train_wizards(self):
        pass

    def _draft_soldiers(self):
        pass

    def _collect_taxes(self):
        pass

nko = Province()
print(nko.ressources)