"""
Services implemented by the Azure provider.
"""
from cloudbridge.cloud.base.services import BaseSecurityService


class AzureSecurityService(BaseSecurityService):

    def __init__(self, provider):
        super(BaseSecurityService, self).__init__(provider)
