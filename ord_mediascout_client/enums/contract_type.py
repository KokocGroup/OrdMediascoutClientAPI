from enum import StrEnum


class ContractType(StrEnum):
    ServiceAgreement = 'ServiceAgreement'
    MediationContract = 'MediationContract'
    AdditionalAgreement = 'AdditionalAgreement'
    SelfPromotionContract = 'SelfPromotionContract'
    VirtualFinalContract = 'VirtualFinalContract'
