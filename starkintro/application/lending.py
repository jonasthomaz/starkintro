import starkinfra
from starkinfra.creditnote import Transfer, Invoice
from starkinfra.creditsigner import CreditSigner
from starkintro.application import BaseApp
from starkintro.domain.enumatetor import IndividualIdentityStatus
from starkintro.domain.value_objects.creditpreview_notification import CreditPreviewNotification
from starkintro.domain.value_objects.identity_notification import IdentityNotification


class Lending(BaseApp):

    @staticmethod
    def create_credit_preview(notification: CreditPreviewNotification):
        previews = starkinfra.creditpreview.create([
            starkinfra.CreditPreview(
                type="credit-note",
                credit=starkinfra.creditpreview.CreditNotePreview(
                    initial_amount=notification.initial_amount(),
                    initial_due=notification.initial_due(),
                    interval=notification.interval(),
                    nominal_amount=notification.nominal_amount(),
                    nominal_interest=notification.nominal_interest(),
                    rebate_amount=notification.rebate_amount(),
                    scheduled=notification.scheduled(),
                    tax_id=notification.tax_id(),
                    type=notification.type(),
                )
            )
        ])

        return previews

    @staticmethod
    def create_individual_identity(notification: IdentityNotification):
        identities = starkinfra.individualidentity.create([
            starkinfra.IndividualIdentity(
                name=notification.name(),
                tax_id=notification.tax_id(),
                tags=notification.tags()
            )
        ])

        return identities

    @staticmethod
    def add_document_to_identity(identity_id: int, document: dict, filename: str):
        with open(filename, 'rb') as file:
            rgFront = file.read()

        documents = starkinfra.individualdocument.create([
            starkinfra.individualdocument(
                type="identity-front",
                content=rgFront,
                content_type="image/png",
                identity_id=identity_id,
                tags=["breaking", "bad"]
            )
        ])

        return documents

    @staticmethod
    def send_identity_to_validate(identity_id: int):
        return starkinfra.individualidentity.update(f"{identity_id}", IndividualIdentityStatus.processing)

    @staticmethod
    def create_credit_notes():
        notes = starkinfra.creditnote.create([
            starkinfra.CreditNote(
                template_id="5707012469948416",
                name="Jaime Lannister",
                tax_id="012.345.678-90",
                nominal_amount=100000,
                scheduled="2022-07-15",
                invoices=[
                    Invoice(
                        due="2023-07-25",
                        amount=120000,
                    )
                ],
                tags=["test", "testing"],
                payment=Transfer(
                    bank_code="00000000",
                    branch_code="1234",
                    account_number="129340-1",
                    name="Jaime Lannister",
                    tax_id="012.345.678-90",
                ),
                signers=[
                    CreditSigner(
                        name="Jaime Lannister",
                        contact="jaime.lannister@gmail.com",
                        method="link"
                    )
                ],
                external_id="1234",
                street_line_1="Rua ABC",
                street_line_2="Ap 123",
                district="Jardim Paulista",
                city="São Paulo",
                state_code="SP",
                zip_code="01234-567",
            )
        ])

        return notes
