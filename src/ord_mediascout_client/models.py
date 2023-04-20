# generated by datamodel-codegen:
#   filename:  https://demo.mediascout.ru/swagger/v1/swagger.json
#   timestamp: 2023-04-19T12:32:32+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra


def capitalize(s: str) -> str:
    return s[0].upper() + s[1:]


class ClearInvoiceDataWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None


class ClientRelationshipType(Enum):
    DirectClient = 'DirectClient'
    InitialContractClient = 'InitialContractClient'


class ContractStatus(Enum):
    Created = 'Created'
    Active = 'Active'
    Testing = 'Testing'
    Deleted = 'Deleted'


class ContractSubjectTypeWebApi(Enum):
    Distribution = 'Distribution'
    OrgDistribution = 'OrgDistribution'
    Representation = 'Representation'
    Mediation = 'Mediation'
    Other = 'Other'


class ContractType(Enum):
    ServiceAgreement = 'ServiceAgreement'
    MediationContract = 'MediationContract'
    AdditionalAgreement = 'AdditionalAgreement'
    SelfPromotionContract = 'SelfPromotionContract'
    VirtualFinalContract = 'VirtualFinalContract'


class CounterpartyStatus(Enum):
    Created = 'Created'
    Active = 'Active'


class CreatedCreativeWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[str] = None
    erid: Optional[str] = None
    creativeGroupId: Optional[str] = None
    creativeGroupName: Optional[str] = None


class CreativeForm(Enum):
    Banner = 'Banner'
    Text = 'Text'
    TextGraphic = 'TextGraphic'
    Video = 'Video'
    Audio = 'Audio'
    AudioBroadcast = 'AudioBroadcast'
    VideoBroadcast = 'VideoBroadcast'
    Other = 'Other'


class CreativeMediaDataItemWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    fileName: Optional[str] = None
    fileContentBase64: Optional[str] = None
    srcUrl: Optional[str] = None
    description: Optional[str] = None
    isArchive: Optional[bool] = None


class CreativeStatus(Enum):
    Created = 'Created'
    Active = 'Active'


class CreativeTextDataItemWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    textData: Optional[str] = None


class CreativeType(Enum):
    CPM = 'CPM'
    CPC = 'CPC'
    CPA = 'CPA'
    Other = 'Other'


class CreativeWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    creativeGroupId: Optional[str] = None
    creativeGroupName: Optional[str] = None
    finalContractId: Optional[str] = None
    initialContractId: Optional[str] = None
    type: Optional[CreativeType] = None
    form: Optional[CreativeForm] = None
    advertiserUrl: Optional[str] = None
    advertiserUrls: Optional[List[str]] = None
    description: Optional[str] = None
    targetAudience: Optional[str] = None
    isNative: Optional[bool] = None
    isSocial: Optional[bool] = None
    okvedCodes: Optional[List[str]] = None
    mediaData: Optional[List[CreativeMediaDataItemWebApiDto]] = None
    textData: Optional[List[CreativeTextDataItemWebApiDto]] = None
    id: Optional[str] = None
    erid: Optional[str] = None
    status: Optional[CreativeStatus] = None


class EditCreativeWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None
    erid: Optional[str] = None
    creativeGroupId: Optional[str] = None
    creativeGroupName: Optional[str] = None
    advertiserUrls: Optional[List[str]] = None


class EntityIdWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None


class GetClientsWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None
    inn: Optional[str] = None
    status: Optional[CounterpartyStatus] = None


class GetCreativeGroupsWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    initialContractId: Optional[str] = None
    finalContractId: Optional[str] = None
    creativeGroupName: Optional[str] = None


class GetCreativesWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    creativeId: Optional[str] = None
    erid: Optional[str] = None
    initialContractId: Optional[str] = None
    initialContractNumber: Optional[str] = None
    finalContractId: Optional[str] = None
    finalContractNumber: Optional[str] = None
    status: Optional[CreativeStatus] = None


class GetFinalContractsWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    finalContractId: Optional[str] = None
    clientId: Optional[str] = None
    status: Optional[ContractStatus] = None


class GetInitialContractsWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    initialContractId: Optional[str] = None
    finalContractId: Optional[str] = None
    contractorId: Optional[str] = None
    contractorInn: Optional[str] = None
    contractorName: Optional[str] = None
    clientId: Optional[str] = None
    clientInn: Optional[str] = None
    clientName: Optional[str] = None
    status: Optional[ContractStatus] = None


class GetOuterContractsWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    outerContractId: Optional[str] = None
    status: Optional[ContractStatus] = None
    contractorId: Optional[str] = None
    clientId: Optional[str] = None


class InvoiceInitialContractItemWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    initialContractId: Optional[str] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None


class InvoicePartyRole(Enum):
    Rr = 'Rr'
    Ors = 'Ors'
    Rd = 'Rd'
    Ra = 'Ra'


class InvoiceStatus(Enum):
    Creating = 'Creating'
    Created = 'Created'
    Deleted = 'Deleted'
    Registering = 'Registering'
    RegistrationRequired = 'RegistrationRequired'
    Active = 'Active'


class InvoiceSummaryWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None
    status: Optional[InvoiceStatus] = None
    amount: Optional[float] = None
    initialContractsCount: Optional[int] = None
    initialContractsAmount: Optional[float] = None
    creativesCount: Optional[int] = None
    platformsCount: Optional[int] = None
    impsFactCount: Optional[int] = None
    impsPlanCount: Optional[int] = None
    impsAmount: Optional[float] = None


class LegalForm(Enum):
    JuridicalPerson = 'JuridicalPerson'
    IndividualEntrepreneur = 'IndividualEntrepreneur'
    PhysicalPerson = 'PhysicalPerson'
    InternationalJuridicalPerson = 'InternationalJuridicalPerson'
    InternationalPhysicalPerson = 'InternationalPhysicalPerson'


class MediationActionType(Enum):
    Contracting = 'Contracting'
    Distribution = 'Distribution'
    CommercialRepresentation = 'CommercialRepresentation'
    Other = 'Other'


class OuterContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    contractorId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[ContractStatus] = None


class PlatformType(Enum):
    Site = 'Site'
    Application = 'Application'
    InformationSystem = 'InformationSystem'


class SelfPromotionContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[ContractStatus] = None


class Severity(Enum):
    Error = 'Error'
    Warning = 'Warning'
    Info = 'Info'


class ValidationFailure(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize

    propertyName: Optional[str] = None
    errorMessage: Optional[str] = None
    attemptedValue: Optional[Any] = None
    customState: Optional[Any] = None
    severity: Optional[Severity] = None
    errorCode: Optional[str] = None
    formattedMessagePlaceholderValues: Optional[Dict[str, Any]] = None


class BadRequestWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize

    errorType: Optional[str] = None
    errorItems: Optional[List[ValidationFailure]] = None


class ClientWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    createMode: Optional[ClientRelationshipType] = None
    legalForm: Optional[LegalForm] = None
    inn: Optional[str] = None
    name: Optional[str] = None
    mobilePhone: Optional[str] = None
    epayNumber: Optional[str] = None
    regNumber: Optional[str] = None
    oksmNumber: Optional[str] = None
    id: Optional[str] = None
    status: Optional[CounterpartyStatus] = None


class CreateClientWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    createMode: Optional[ClientRelationshipType] = None
    legalForm: Optional[LegalForm] = None
    inn: Optional[str] = None
    name: Optional[str] = None
    mobilePhone: Optional[str] = None
    epayNumber: Optional[str] = None
    regNumber: Optional[str] = None
    oksmNumber: Optional[str] = None


class CreateCreativeWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    finalContractId: Optional[str] = None
    initialContractId: Optional[str] = None
    type: Optional[CreativeType] = None
    form: Optional[CreativeForm] = None
    advertiserUrls: Optional[List[str]] = None
    description: Optional[str] = None
    targetAudience: Optional[str] = None
    isNative: Optional[bool] = None
    isSocial: Optional[bool] = None
    okvedCodes: Optional[List[str]] = None
    mediaData: Optional[List[CreativeMediaDataItemWebApiDto]] = None
    textData: Optional[List[CreativeTextDataItemWebApiDto]] = None


class CreateFinalContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    clientId: Optional[str] = None


class CreateInitialContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    contractorId: Optional[str] = None
    clientId: Optional[str] = None
    finalContractId: Optional[str] = None


class CreateOuterContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    contractorId: Optional[str] = None


class CreatePlatformWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    name: Optional[str] = None
    type: Optional[PlatformType] = None
    url: Optional[str] = None
    isOwner: Optional[bool] = None

class CreativeGroupWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid

    creativeGroupId: Optional[str] = None
    finalContractId: Optional[str] = None
    initialContractId: Optional[str] = None
    creativeGroupName: Optional[str] = None
    type: Optional[CreativeType] = None
    form: Optional[CreativeForm] = None
    isSocial: Optional[bool] = None
    isNative: Optional[bool] = None
    targetAudience: Optional[str] = None
    description: Optional[str] = None
    okvedCodes: Optional[str] = None


class EditFinalContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    clientId: Optional[str] = None
    id: Optional[str] = None


class EditInitialContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    contractorId: Optional[str] = None
    clientId: Optional[str] = None
    finalContractId: Optional[str] = None
    id: Optional[str] = None


class EditInvoiceDataWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None
    number: Optional[str] = None
    date: Optional[date] = None
    contractorRole: Optional[InvoicePartyRole] = None
    clientRole: Optional[InvoicePartyRole] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    finalContractId: Optional[str] = None


class EditOuterContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    contractorId: Optional[str] = None
    id: Optional[str] = None


class EditPlatformWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    name: Optional[str] = None
    type: Optional[PlatformType] = None
    url: Optional[str] = None
    isOwner: Optional[bool] = None
    id: Optional[str] = None


class FinalContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    clientId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[ContractStatus] = None


class GetInvoicesWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    invoiceId: Optional[str] = None
    number: Optional[str] = None
    dateStart: Optional[date] = None
    dateEnd: Optional[date] = None
    finalContractId: Optional[str] = None
    status: Optional[InvoiceStatus] = None


class InitialContractWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    isAgentActingForPublisher: Optional[bool] = None
    type: Optional[ContractType] = None
    subjectType: Optional[ContractSubjectTypeWebApi] = None
    actionType: Optional[MediationActionType] = None
    parentMainContractId: Optional[str] = None
    contractorId: Optional[str] = None
    clientId: Optional[str] = None
    finalContractId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[ContractStatus] = None
    contractorInn: Optional[str] = None
    contractorName: Optional[str] = None
    clientInn: Optional[str] = None
    clientName: Optional[str] = None


class InvoiceStatisticsByPlatformsItemWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    initialContractId: Optional[str] = None
    erid: Optional[str] = None
    platformUrl: Optional[str] = None
    platformName: Optional[str] = None
    platformType: Optional[PlatformType] = None
    platformOwnedByAgency: Optional[bool] = None
    impsPlan: Optional[int] = None
    impsFact: Optional[int] = None
    startDatePlan: Optional[date] = None
    startDateFact: Optional[date] = None
    endDatePlan: Optional[date] = None
    endDateFact: Optional[date] = None
    amount: Optional[float] = None
    price: Optional[float] = None
    vatIncluded: Optional[bool] = None


class InvoiceWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    contractorRole: Optional[InvoicePartyRole] = None
    clientRole: Optional[InvoicePartyRole] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    finalContractId: Optional[str] = None
    initialContractsData: Optional[List[InvoiceInitialContractItemWebApiDto]] = None
    statisticsByPlatforms: Optional[List[InvoiceStatisticsByPlatformsItemWebApiDto]] = None
    id: Optional[str] = None
    status: Optional[InvoiceStatus] = None


class PlatformCardWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    name: Optional[str] = None
    type: Optional[PlatformType] = None
    url: Optional[str] = None
    isOwner: Optional[bool] = None
    id: Optional[str] = None


class SupplementInvoiceWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    invoiceId: Optional[str] = None
    initialContractsData: Optional[List[InvoiceInitialContractItemWebApiDto]] = None
    statisticsByPlatforms: Optional[List[InvoiceStatisticsByPlatformsItemWebApiDto]] = None


class CreateInvoiceWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    number: Optional[str] = None
    date: Optional[date] = None
    contractorRole: Optional[InvoicePartyRole] = None
    clientRole: Optional[InvoicePartyRole] = None
    amount: Optional[float] = None
    vatIncluded: Optional[bool] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    finalContractId: Optional[str] = None
    initialContractsData: Optional[List[InvoiceInitialContractItemWebApiDto]] = None
    statisticsByPlatforms: Optional[List[InvoiceStatisticsByPlatformsItemWebApiDto]] = None


class EditInvoiceStatisticsWebApiDto(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True

    id: Optional[str] = None
    initialContractsData: Optional[List[InvoiceInitialContractItemWebApiDto]] = None
    statisticsByPlatforms: Optional[List[InvoiceStatisticsByPlatformsItemWebApiDto]] = None
