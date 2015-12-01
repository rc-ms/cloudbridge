"""
Services implemented by the Azure provider.
"""
from cloudbridge.cloud.base.services import BaseKeyPairService
from cloudbridge.cloud.base.services import BaseSecurityGroupService
from cloudbridge.cloud.base.services import BaseSecurityService


class AzureSecurityService(BaseSecurityService):

    def __init__(self, provider):
        super(BaseSecurityService, self).__init__(provider)

        # Initialize provider services
        self._key_pairs = AzureKeyPairService(provider)
        self._security_groups = AzureSecurityGroupService(provider)

    @property
    def key_pairs(self):
        return self._key_pairs

    @property
    def security_groups(self):
        return self._security_groups


class AzureKeyPairService(BaseKeyPairService):

    def __init__(self, provider):
        super(AzureKeyPairService, self).__init__(provider)

    def get(self, keypair_id):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def list(self, limit=None, marker=None):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def find(self, name, limit=None, marker=None):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def create(self, name):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")


class AzureSecurityGroupService(BaseSecurityGroupService):

    def __init__(self, provider):
        super(AzureSecurityGroupService, self).__init__(provider)

    def get(self, sg_id):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def list(self, limit=None, marker=None):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def create(self, name, description):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def find(self, name, limit=None, marker=None):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")

    def delete(self, group_id):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this method")
