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
    ('vendor/lib64/camx.device@3.4-ext-impl.so', 'vendor/lib64/camx.device@3.5-ext-impl.so', 'vendor/lib64/camx.device@3.6-ext-impl.so',
     'vendor/lib64/camx.provider@2.4-external.so', 'vendor/lib64/camx.provider@2.4-impl.so', 'vendor/lib64/camx.provider@2.4-legacy.so',
     'vendor/lib64/camx.provider@2.5-external.so', 'vendor/lib64/camx.provider@2.5-legacy.so', 'vendor/lib64/camx.provider@2.6-legacy.so',
     'vendor/lib64/camx.provider@2.7-legacy.so'): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib64/libcammw.so': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V2-ndk_platform.so', 'vendor.qti.hardware.display.config-V2-ndk.so'),
    ('vendor/lib64/libsomc_camerahal.so', 'vendor/lib64/libsomc_chokoballpal.so'): blob_fixup()
        .replace_needed('libui.so', 'libui-v34.so'),
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
