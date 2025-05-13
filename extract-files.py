#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/sony',
    'vendor/qcom/opensource/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/sony/sm8450-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/vendor.somc.camera.device@3.2-impl.so', 'vendor/lib64/vendor.somc.camera.device@3.3-impl.so',
     'vendor/lib64/vendor.somc.camera.device@3.4-impl.so', 'vendor/lib64/vendor.somc.camera.device@3.5-impl.so',
     'vendor/bin/hw/vendor.somc.hardware.camera.provider@1.0-service'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V2-ndk_platform.so', 'vendor.qti.hardware.display.config-V2-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'pdx223',
    'sony',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()
