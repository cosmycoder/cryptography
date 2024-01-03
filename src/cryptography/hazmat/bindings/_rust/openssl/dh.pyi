# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

import typing

from cryptography.hazmat.primitives.asymmetric import dh

MIN_MODULUS_SIZE: int

class DHPrivateKey: ...
class DHPublicKey: ...
class DHParameters: ...

class DHPrivateNumbers:
    def __init__(self, x: int, public_numbers: DHPublicNumbers) -> None: ...
    def private_key(self, backend: typing.Any = None) -> dh.DHPrivateKey: ...
    @property
    def x(self) -> int: ...
    @property
    def public_numbers(self) -> DHPublicNumbers: ...

class DHPublicNumbers:
    def __init__(
        self, y: int, parameter_numbers: DHParameterNumbers
    ) -> None: ...
    def public_key(self, backend: typing.Any = None) -> dh.DHPublicKey: ...
    @property
    def y(self) -> int: ...
    @property
    def parameter_numbers(self) -> DHParameterNumbers: ...

class DHParameterNumbers:
    def __init__(self, p: int, g: int, q: int | None = None) -> None: ...
    def parameters(self, backend: typing.Any = None) -> dh.DHParameters: ...
    @property
    def p(self) -> int: ...
    @property
    def g(self) -> int: ...
    @property
    def q(self) -> int | None: ...

def generate_parameters(generator: int, key_size: int) -> dh.DHParameters: ...
def from_pem_parameters(
    data: bytes, backend: typing.Any = None
) -> dh.DHParameters: ...
def from_der_parameters(
    data: bytes, backend: typing.Any = None
) -> dh.DHParameters: ...
