"""
DataTypes used by this provider
"""
from cloudbridge.cloud.base.resources import BaseKeyPair


class AzureKeyPair(BaseKeyPair):

    def __init__(self, provider, cert, material=None):
        super(AzureKeyPair, self).__init__(provider, None)
        self._cert = cert
        self._material = material

    @staticmethod
    def format_kp_id(thumbprint_algorithm, thumbprint):
        return "%s-%s" % (thumbprint_algorithm,
                          thumbprint.upper())

    @property
    def id(self):
        return AzureKeyPair.format_kp_id(self._cert.thumbprint_algorithm,
                                         self._cert.thumbprint)

    @property
    def name(self):
        return self.id

    def delete(self):
        op = self._provider.sms.delete_service_certificate(
            self._provider.service_name,
            self._cert.thumbprint_algorithm,
            self._cert.thumbprint)
        result = self._provider.sms.wait_for_operation_status(op.request_id)
        return result.status == 'Succeeded'

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value
