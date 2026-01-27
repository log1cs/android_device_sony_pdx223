#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
TARGET_SUPPORTS_OMX_SERVICE := false
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from pdx223 device
$(call inherit-product, device/sony/pdx223/device.mk)

# Inherit some common AOSP stuff.
$(call inherit-product, vendor/custom/config/common_full_phone.mk)

PRODUCT_NAME := custom_pdx223
PRODUCT_DEVICE := pdx223
PRODUCT_MANUFACTURER := Sony
PRODUCT_BRAND := Sony
PRODUCT_MODEL := XQ-CT72

PRODUCT_GMS_CLIENTID_BASE := android-sonymobile

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="XQ-CT72-user 14 64.2.A.2.265 064002A002026500519766968 release-keys" \
    BuildFingerprint=Sony/XQ-CT72/XQ-CT72:14/64.2.A.2.265/064002A002026500519766968:user/release-keys \
    DeviceName=XQ-CT72 \
    DeviceProduct=XQ-CT72 \
    SystemDevice=XQ-CT72 \
    SystemName=XQ-CT72
