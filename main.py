import datetime 
import locale

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

NOTIFICATIONS = """
--------------------------------------------------

内容がお間違いないかご確認お願いいたします。

⚠️必ずご確認お願いいたします⚠️
✔️ヘアラインの場合、施術範囲が広い場合追加金額が発生する可能性がございます。（当日確認後金額が確定します。）
✔️眉毛アートメイクの施術技法は当日カウンセリングの後に決定いたします🤲
✔️お客様の眉毛の状態によって自然眉毛(エンボ技法/20万ウォン)ができない場合がございますのでご了承ください。🙇‍♀️♥️(自然眉毛ができない場合、コンボ眉毛/25万ウォンの技法に施術変更されます)

⚠️全てのsnsイベント値段は現金のみの場合に適用されます。クレジットカード(WOWPASSワオパス)などでお支払いする場合、定価の値段に10%が課税されますので現金(ウォン)の持参をお願いいたします。
"""

CATEGORIES = [
    {
      "slug": "eyebrow",
      "name": "眉毛",
      "menus": [
        { "slug": "naturalEyebrow", "name": "自然眉毛（エンボ）", "price": 200000 },
        { "slug": "powderEyebrow", "name": "パウダー眉毛", "price": 250000 },
        { "slug": "comboEyebrow", "name": "コンボ眉毛", "price": 250000 },
      ],
    },
    {
      "slug": "lip",
      "name": "リップ",
      "menus": [
        { "slug": "fullLip", "name": "フルリップ", "price": 320000 },
        { "slug": "gradientLip", "name": "グラデーションリップ", "price": 320000 },
      ],
    },
    {
      "slug": "face",
      "name": "顔",
      "menus": [
        { "slug": "skinplanning", "name": "スキンプランニング", "price": 150000 },
        { "slug": "mole", "name": "美人ホクロ", "price": 40000 },
      ],
    },
    {
      "slug": "hairline",
      "name": "ヘアライン",
      "menus": [
        { "slug": "naturalHairLine", "name": "自然ヘアライン", "price": 320000 },
        {
          "slug": "gradationHairLine",
          "name": "グラデーションヘアライン",
          "price": 450000,
        },
        { "slug": "comboHairLine", "name": "コンボヘアライン", "price": 500000 },
      ],
    },
    {
      "slug": "eyeline",
      "name": "アイライン",
      "menus": [
        { "slug": "eyeCorner", "name": "目尻のみ", "price": 180000 },
        { "slug": "underline", "name": "アンダーライン", "price": 200000 },
        { "slug": "membrane", "name": "粘膜", "price": 200000 },
        { "slug": "eyeCornerMembrane", "name": "目尻 + 粘膜", "price": 250000 },
        { "slug": "designUnderline", "name": "デザインアイライン", "price": 250000 },
      ],
    },
    {
      "slug": "eyelashes",
      "name": "まつげ",
      "menus": [
        { "slug": "basicEyelashes", "name": "基本まつ毛パーマ", "price": 50000 },
        {
          "slug": "clinicEyelashes",
          "name": "クリニックまつ毛パーマ",
          "price": 60000,
        },
        {
          "slug": "tintEyelashes",
          "name": "ティントパーマ（クリニック＋ティントパーマ含む）",
          "price": 70000,
        },
        {
          "slug": "howToReproLift", 
          "name": "ハウツリプロリフト",
          "price": 40000,
        },
      ],
    },
    {
      "slug": "smp",
      "name": "頭皮",
      "menus": [
        { "slug": "smpCounseling", "name": "金額策定（写真確認後）", "price": 0 },
      ],
    },
    {
      "slug": "nipple",
      "name": "ニップル",
      "menus": [{ "slug": "nippleArt", "name": "ニップル", "price": 800000 }],
    },
]

COUPONS = [
  { "slug": 'double', "name": "セット割引", "discount": 10000 },
  { "slug": "influencer", "name": "インフルエンサー割引", "discount": 20000 },
]

def customer_information(name: str, name_kana: str, operated_at: datetime, menuSlugs: str, couponSlugs: str, phone_number: str):
  parsed_menus = [menu for category in CATEGORIES for menu in category["menus"]]
  my_menus = list(filter(lambda x: x["slug"] in menuSlugs, parsed_menus))
  my_coupons = list(filter(lambda x: x["slug"] in couponSlugs, COUPONS))

  price = sum([menu["price"] for menu in my_menus]) - sum([coupon['discount'] for coupon in my_coupons])

  return f"""
★ソウル★
●お名前 : {name}({name_kana})
●施術日時: {operated_at.strftime("%Y年%m月%d日(%a) %H:%M")}
●施術内容: {', '.join([menu["name"] for menu in my_menus])}
●現地払い: {format(price, ',')}ウォン（⚠️現金金額)
●ご連絡先: {phone_number}
"""

def main():
  customer_data = {
    "name": "",
    "name_kana": '',
    "operated_at": datetime.datetime(2024, 1, 1, 0, 0),
    "menuSlugs": [],
    "couponSlugs": [],
    "phone_number": ""
  }

  print("\n".join([customer_information(**customer_data), NOTIFICATIONS]))

main()