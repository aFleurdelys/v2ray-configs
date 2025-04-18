from bs4 import BeautifulSoup
import requests
import urllib.parse

def get_v2ray_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 搜索所有可能包含配置的标签
        divs = soup.find_all('div', class_='tgme_widget_message_text')
        divs2 = soup.find_all('div', class_='tgme_widget_message_text js-message_text before_footer')
        spans = soup.find_all('span', class_='tgme_widget_message_text')
        codes = soup.find_all('code')
        span = soup.find_all('span')
        main = soup.find_all('div')

        all_tags = divs + spans + codes + divs2 + span + main

        v2ray_configs = []
        for tag in all_tags:
            text = tag.get_text().strip()
            # 支持更多协议类型
            if any(text.startswith(p) for p in ['vmess://', 'vless://', 'ss://', 'trojan://', 'tuic://']):
                v2ray_configs.append(text)

        return v2ray_configs
    else:
        print(f"Failed to fetch URL (Status Code: { response.status_code })")
        return None

def save_all_configs(configs):
    with open("Subs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))

if __name__ == "__main__":
    telegram_urls = [
        "https://t.me/s/v2line",
        "https://t.me/s/forwardv2ray",
        "https://t.me/s/inikotesla",
        "https://t.me/s/PrivateVPNs",
        "https://t.me/s/VlessConfig",
        "https://t.me/s/V2pedia",
        "https://t.me/s/v2rayNG_Matsuri",
        "https://t.me/s/PrivateVPNs",
        "https://t.me/s/proxystore11",
        "https://t.me/s/DirectVPN",
        "https://t.me/s/VmessProtocol",
        "https://t.me/s/OutlineVpnOfficial",
        "https://t.me/s/networknim",
        "https://t.me/s/beiten",
        "https://t.me/s/MsV2ray",
        "https://t.me/s/foxrayiran",
        "https://t.me/s/DailyV2RY",
        "https://t.me/s/yaney_01",
        "https://t.me/s/FreakConfig",
        "https://t.me/s/EliV2ray",
        "https://t.me/s/ServerNett",
        "https://t.me/s/proxystore11",
        "https://t.me/s/v2rayng_fa2",
        "https://t.me/s/v2rayng_org",
        "https://t.me/s/V2rayNGvpni",
        "https://t.me/s/custom_14",
        "https://t.me/s/v2rayNG_VPNN",
        "https://t.me/s/v2ray_outlineir",
        "https://t.me/s/v2_vmess",
        "https://t.me/s/FreeVlessVpn",
        "https://t.me/s/vmess_vless_v2rayng",
        "https://t.me/s/PrivateVPNs",
        "https://t.me/s/freeland8",
        "https://t.me/s/vmessiran",
        "https://t.me/s/Outline_Vpn",
        "https://t.me/s/vmessq",
        "https://t.me/s/WeePeeN",
        "https://t.me/s/V2rayNG3",
        "https://t.me/s/ShadowsocksM",
        "https://t.me/s/shadowsocksshop",
        "https://t.me/s/v2rayan",
        "https://t.me/s/ShadowSocks_s",
        "https://t.me/s/VmessProtocol",
        "https://t.me/s/napsternetv_config",
        "https://t.me/s/Easy_Free_VPN",
        "https://t.me/s/V2Ray_FreedomIran",
        "https://t.me/s/V2RAY_VMESS_free",
        "https://t.me/s/v2ray_for_free",
        "https://t.me/s/V2rayN_Free",
        "https://t.me/s/free4allVPN",
        "https://t.me/s/vpn_ocean",
        "https://t.me/s/configV2rayForFree",
        "https://t.me/s/FreeV2rays",
        "https://t.me/s/DigiV2ray",
        "https://t.me/s/v2rayNG_VPN",
        "https://t.me/s/freev2rayssr",
        "https://t.me/s/v2rayn_server",
        "https://t.me/s/Shadowlinkserverr",
        "https://t.me/s/iranvpnet",
        "https://t.me/s/vmess_iran",
        "https://t.me/s/mahsaamoon1",
        "https://t.me/s/V2RAY_NEW",
        "https://t.me/s/v2RayChannel",
        "https://t.me/s/configV2rayNG",
        "https://t.me/s/config_v2ray",
        "https://t.me/s/vpn_proxy_custom",
        "https://t.me/s/vpnmasi",
        "https://t.me/s/v2ray_custom",
        "https://t.me/s/VPNCUSTOMIZE",
        "https://t.me/s/HTTPCustomLand",
        "https://t.me/s/vpn_proxy_custom",
        "https://t.me/s/ViPVpn_v2ray",
        "https://t.me/s/FreeNet1500",
        "https://t.me/s/v2ray_ar",
        "https://t.me/s/beta_v2ray",
        "https://t.me/s/vip_vpn_2022",
        "https://t.me/s/FOX_VPN66",
        "https://t.me/s/VorTexIRN",
        "https://t.me/s/YtTe3la",
        "https://t.me/s/V2RayOxygen",
        "https://t.me/s/Network_442",
        "https://t.me/s/VPN_443",
        "https://t.me/s/v2rayng_v",
        "https://t.me/s/ultrasurf_12",
        "https://t.me/s/iSeqaro",
        "https://t.me/s/frev2rayng",
        "https://t.me/s/frev2ray",
        "https://t.me/s/FreakConfig",
        "https://t.me/s/Awlix_ir",
        "https://t.me/s/v2rayngvpn",
        "https://t.me/s/God_CONFIG",
        "https://t.me/s/Configforvpn01",
    ]

    all_v2ray_configs = []
    for url in telegram_urls:
        if configs := get_v2ray_links(url):
            all_v2ray_configs.extend(configs)

    if all_v2ray_configs:
        # 去重处理
        unique_configs = list(set(all_v2ray_configs))
        # 保存到Subs.txt
        save_all_configs(unique_configs)
        print(f"Saved { len(unique_configs) } unique configs to Subs.txt")
    else:
        print("No V2Ray configs found.")
