"""
Helper functions
"""
import base64
import hashlib
import socket

from OpenSSL import crypto


def _generate_cert(keys):
    """
    Generate self-signed certificate for Azure
    """
    cert = crypto.X509()
    cert.get_subject().O = "azure"
    cert.get_subject().OU = "cloudbridge"
    cert.get_subject().CN = socket.gethostname()
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(keys)
    cert.sign(keys, 'sha1')
    return cert


def _to_pfx_cert(cert, keys):
    """
    Generate pfx cert for export to Azure
    """
    p12 = crypto.PKCS12()
    p12.set_privatekey(keys)
    p12.set_certificate(cert)
    return p12.export()


def _cert_digest(cert):
    """
    Generate azure server reported digest.
    """
    public_cert = crypto.dump_certificate(crypto.FILETYPE_ASN1, cert)
    h = hashlib.sha1()
    h.update(public_cert)
    return h.hexdigest()


def generate_key_pair():
    """
    Generate a new private key and pfx certificate for Azure
    """
    keys = crypto.PKey()
    keys.generate_key(crypto.TYPE_RSA, 1024)

    cert = _generate_cert(keys)
    pfx = base64.b64encode(_to_pfx_cert(cert, keys))
    digest = _cert_digest(cert)

    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, keys)
    return (pfx, digest, private_key)
