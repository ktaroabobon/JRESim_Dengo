import usb.core
import usb.util

if __name__ == '__main__':
    # ベンダーIDとプロダクトIDを指定します。
    # これらの値はデバイスによりますので、適切な値に置き換えてください。
    VENDOR_ID = 0x0ae4
    PRODUCT_ID = 0x0003

    # デバイスを検索します。
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

    if dev is None:
        raise ValueError('Device not found')

    # デバイスを初期化します。
    dev.set_configuration()

    # エンドポイントを取得します。
    cfg = dev.get_active_configuration()
    intf = cfg[(0, 0)]

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match= \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT)

    assert ep is not None

    # デバイスからデータを読み取ります。
    # ここでは、8バイトのデータを読み取るようにしています。
    data = dev.read(ep.bEndpointAddress, 8)

    print(data)
