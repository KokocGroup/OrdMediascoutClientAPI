from enum import StrEnum


class ContractSubjectType(StrEnum):
    Distribution = 'Distribution'
    OrgDistribution = 'OrgDistribution'
    Representation = 'Representation'
    Mediation = 'Mediation'
    Other = 'Other'
