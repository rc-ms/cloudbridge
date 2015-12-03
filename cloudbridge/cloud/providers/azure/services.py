"""
Services implemented by the Azure provider.
"""
from cloudbridge.cloud.base.resources import ClientPagedResultList
from cloudbridge.cloud.base.services import BaseKeyPairService
from cloudbridge.cloud.base.services import BaseSecurityGroupService
from cloudbridge.cloud.base.services import BaseSecurityService
from cloudbridge.cloud.interfaces.resources import CreateResourceException
from cloudbridge.cloud.providers.azure import helpers
from cloudbridge.cloud.providers.azure.resources import AzureKeyPair


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
        return next((kp for kp in self if kp.id == keypair_id), None)

    def list(self, limit=None, marker=None):
        certs = self.provider.sms.list_service_certificates(
            self.provider.service_name)
        results = [AzureKeyPair(self.provider, cert)
                   for cert in certs]
        return ClientPagedResultList(self.provider, results,
                                     limit=limit, marker=marker)

    def find(self, name, limit=None, marker=None):
        results = [kp for kp in self if kp.name == name]
        return ClientPagedResultList(self.provider, results,
                                     limit=limit, marker=marker)

    def create(self, name):
        pfx_cert, digest, pk = helpers.generate_key_pair()
        # add_service_certificate does not behave as advertised:
        # http://stackoverflow.com/questions/18117578/
        # azure-add-certificate-to-cloudservice
        op = self.provider.sms.add_service_certificate(
            self.provider.service_name, pfx_cert, "pfx", "")
        result = self.provider.sms.wait_for_operation_status(op.request_id)
        if result.status == 'Succeeded':
            kp_id = AzureKeyPair.format_kp_id("sha1", digest)
            kp = self.get(kp_id)
            kp.material = pk
            return kp
        else:
            raise CreateResourceException(
                "Could not create keypair: %s", result)


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
