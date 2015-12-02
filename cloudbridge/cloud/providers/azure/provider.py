"""
Provider implementation based on Azure-SDK.
"""
import os
from azure.servicemanagement import ServiceManagementService

from cloudbridge.cloud.base import BaseCloudProvider
from cloudbridge.cloud.providers.azure.services import AzureSecurityService


class AzureCloudProvider(BaseCloudProvider):

    PROVIDER_ID = 'azure'

    def __init__(self, config):
        super(AzureCloudProvider, self).__init__(config)

        # connection variables
        self._subscription_id = self._get_config_value(
            'azure_subscription_id',
            os.environ.get('AZURE_SUBSCRIPTION_ID', None))
        self._certificate_path = self._get_config_value(
            'azure_cert_path',
            os.environ.get('AZURE_CERT_PATH', None))
        self.service_name = self._get_config_value(
            'azure_service_name',
            os.environ.get('AZURE_SERVICE_NAME', None))

        # service connections, lazily initialized
        self._sms = None

        # Initialize provider services
        self._security = None

    @property
    def compute(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def security(self):
        if not self._security:
            self._security = AzureSecurityService(self)
        return self._security

    @property
    def block_store(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def object_store(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def sms(self):
        if not self._sms:
            self._sms = self._connect_sms()
        return self._sms

    def _connect_sms(self):
        return ServiceManagementService(self._subscription_id,
                                        self._certificate_path)
