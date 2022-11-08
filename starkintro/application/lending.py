import starkbank
import starkinfra
from starkintro.application import BaseApp
from starkintro.domain.value_objects.creditpreview_notification import CreditPreviewNotification
from starkintro.domain.value_objects.creditpreview_notification import CreditPreviewNotification


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

        for preview in previews:
            print(preview)


    def create_individual_identity(self):
        ...