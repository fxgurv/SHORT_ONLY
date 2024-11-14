"""
This file contains all the constants used in the program.
"""
import g4f

TWITTER_TEXTAREA_CLASS = "public-DraftStyleDefault-block public-DraftStyleDefault-ltr"

TWITTER_POST_BUTTON_XPATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]"

# menu
MAIN_MENU = ["Shorts Generator", "Twitter Poster", "Affiliate Marketing", "Outreach WorkFlows", "Exit"]

SHORTS_MENU = ["Add New Account", "Show all Shorts", "Setup CRON Jobs", "Back To Main Menu", "Exit"]

CRON_MENU = ["Once a day", "Twice a day", "Custom", "Back To Main Menu", "Exit"]


# YouTube Section
YOUTUBE_TEXTBOX_ID = "textbox"
YOUTUBE_MADE_FOR_KIDS_NAME = "VIDEO_MADE_FOR_KIDS_MFK"
YOUTUBE_NOT_MADE_FOR_KIDS_NAME = "VIDEO_MADE_FOR_KIDS_NOT_MFK"
YOUTUBE_NEXT_BUTTON_ID = "next-button"
YOUTUBE_RADIO_BUTTON_XPATH = "//*[@id=\"radioLabel\"]"
YOUTUBE_DONE_BUTTON_ID = "done-button"

# Amazon Section (AFM)$
AMAZON_PRODUCT_TITLE_ID = "productTitle"

AMAZON_FEATURE_BULLETS_ID = "feature-bullets"

XTTS_VOICES = ["Claribel Dervla", "Daisy Studious", "Gracie Wise", "Tammie Ema", "Alison Dietlinde", "Ana Florence", "Annmarie Nele", "Asya Anara", "Brenda Stern", "Gitta Nikolina", "Henriette Usha", "Sofia Hellen", "Tammy Grit", "Tanja Adelina", "Vjollca Johnnie", "Andrew Chipper", "Badr Odhiambo", "Dionisio Schuyler", "Royston Min", "Viktor Eka", "Abrahan Mack", "Adde Michal", "Baldur Sanjin", "Craig Gutsy", "Damien Black", "Gilberto Mathias", "Ilkin Urbano", "Kazuhiko Atallah", "Ludvig Milivoj", "Suad Qasim", "Torcull Diarmuid", "Viktor Menelaos", "Zacharie Aimilios", "Nova Hogarth", "Maja Ruoho", "Uta Obando", "Lidiya Szekeres", "Chandra MacFarland", "Szofi Granger", "Camilla Holmström", "Lilya Stainthorpe", "Zofija Kendrick", "Narelle Moon", "Barbora MacLean", "Alexandra Hisakawa", "Alma María", "Rosemary Okafor", "Ige Behringer", "Filip Traverse", "Damjan Chapman", "Wulf Carlevaro", "Aaron Dreschner", "Kumar Dahl", "Eugenio Mataracı", "Ferran Simen", "Xavier Hayasaka", "Luis Moray", "Marcos Rudaski"]

EDGE=VOICES = ["en-AU-NatashaNeural", "en-AU-WilliamNeural", "en-CA-ClaraNeural", "en-CA-LiamNeural", "en-HK-SamNeural", "en-HK-YanNeural", "en-IN-NeerjaExpressiveNeural", "en-IN-NeerjaNeural", "en-IN-PrabhatNeural", "en-IE-ConnorNeural", "en-IE-EmilyNeural", "en-KE-AsiliaNeural", "en-KE-ChilembaNeural", "en-NZ-MitchellNeural", "en-NZ-MollyNeural", "en-NG-AbeoNeural", "en-NG-EzinneNeural", "en-PH-JamesNeural", "en-PH-RosaNeural", "en-SG-LunaNeural", "en-SG-WayneNeural", "en-ZA-LeahNeural", "en-ZA-LukeNeural", "en-TZ-ElimuNeural", "en-TZ-ImaniNeural", "en-GB-LibbyNeural", "en-GB-MaisieNeural", "en-GB-RyanNeural", "en-GB-SoniaNeural", "en-GB-ThomasNeural", "en-US-AvaMultilingualNeural", "en-US-AndrewMultilingualNeural", "en-US-EmmaMultilingualNeural", "en-US-BrianMultilingualNeural", "en-US-AvaNeural", "en-US-AndrewNeural", "en-US-EmmaNeural", "en-US-BrianNeural", "en-US-AnaNeural", "en-US-AriaNeural", "en-US-ChristopherNeural", "en-US-EricNeural", "en-US-GuyNeural", "en-US-JennyNeural", "en-US-MichelleNeural", "en-US-RogerNeural", "en-US-SteffanNeural", 
 "hi-IN-MadhurNeural", "hi-IN-SwaraNeural",
 "ur-IN-GulNeural", "ur-IN-SalmanNeural", "ur-PK-AsadNeural", "ur-PK-UzmaNeural",
 "af-ZA-AdriNeural", "af-ZA-WillemNeural", "sq-AL-AnilaNeural", "sq-AL-IlirNeural", "am-ET-AmehaNeural", "am-ET-MekdesNeural", "ar-DZ-AminaNeural", "ar-DZ-IsmaelNeural", "ar-BH-AliNeural", "ar-BH-LailaNeural", "ar-EG-SalmaNeural", "ar-EG-ShakirNeural", "ar-IQ-BasselNeural", "ar-IQ-RanaNeural", "ar-JO-SanaNeural", "ar-JO-TaimNeural", "ar-KW-FahedNeural", "ar-KW-NouraNeural", "ar-LB-LaylaNeural", "ar-LB-RamiNeural", "ar-LY-ImanNeural", "ar-LY-OmarNeural", "ar-MA-JamalNeural", "ar-MA-MounaNeural", "ar-OM-AbdullahNeural", "ar-OM-AyshaNeural", "ar-QA-AmalNeural", "ar-QA-MoazNeural", "ar-SA-HamedNeural", "ar-SA-ZariyahNeural", "ar-SY-AmanyNeural", "ar-SY-LaithNeural", "ar-TN-HediNeural", "ar-TN-ReemNeural", "ar-AE-FatimaNeural", "ar-AE-HamdanNeural", "ar-YE-MaryamNeural", "ar-YE-SalehNeural", "az-AZ-BabekNeural", "az-AZ-BanuNeural", "bn-BD-NabanitaNeural", "bn-BD-PradeepNeural", "bn-IN-BashkarNeural", "bn-IN-TanishaaNeural", "bs-BA-GoranNeural", "bs-BA-VesnaNeural", "bg-BG-BorislavNeural", "bg-BG-KalinaNeural", "my-MM-NilarNeural", "my-MM-ThihaNeural", "ca-ES-EnricNeural", "ca-ES-JoanaNeural", "zh-HK-HiuGaaiNeural", "zh-HK-HiuMaanNeural", "zh-HK-WanLungNeural", "zh-CN-XiaoxiaoNeural", "zh-CN-XiaoyiNeural", "zh-CN-YunjianNeural", "zh-CN-YunxiNeural", "zh-CN-YunxiaNeural", "zh-CN-YunyangNeural", "zh-CN-liaoning-XiaobeiNeural", "zh-TW-HsiaoChenNeural", "zh-TW-YunJheNeural", "zh-TW-HsiaoYuNeural", "zh-CN-shaanxi-XiaoniNeural", "hr-HR-GabrijelaNeural", "hr-HR-SreckoNeural", "cs-CZ-AntoninNeural", "cs-CZ-VlastaNeural", "da-DK-ChristelNeural", "da-DK-JeppeNeural", "nl-BE-ArnaudNeural", "nl-BE-DenaNeural", "nl-NL-ColetteNeural", "nl-NL-FennaNeural", "nl-NL-MaartenNeural", "et-EE-AnuNeural", "et-EE-KertNeural", "fil-PH-AngeloNeural", "fil-PH-BlessicaNeural", "fi-FI-HarriNeural", "fi-FI-NooraNeural", "fr-BE-CharlineNeural", "fr-BE-GerardNeural", "fr-CA-ThierryNeural", "fr-CA-AntoineNeural", "fr-CA-JeanNeural", "fr-CA-SylvieNeural", "fr-FR-VivienneMultilingualNeural", "fr-FR-RemyMultilingualNeural", "fr-FR-DeniseNeural", "fr-FR-EloiseNeural", "fr-FR-HenriNeural", "fr-CH-ArianeNeural", "fr-CH-FabriceNeural", "gl-ES-RoiNeural", "gl-ES-SabelaNeural", "ka-GE-EkaNeural", "ka-GE-GiorgiNeural", "de-AT-IngridNeural", "de-AT-JonasNeural", "de-DE-SeraphinaMultilingualNeural", "de-DE-FlorianMultilingualNeural", "de-DE-AmalaNeural", "de-DE-ConradNeural", "de-DE-KatjaNeural", "de-DE-KillianNeural", "de-CH-JanNeural", "de-CH-LeniNeural", "el-GR-AthinaNeural", "el-GR-NestorasNeural", "gu-IN-DhwaniNeural", "gu-IN-NiranjanNeural", "he-IL-AvriNeural", "he-IL-HilaNeural", "hu-HU-NoemiNeural", "hu-HU-TamasNeural", "is-IS-GudrunNeural", "is-IS-GunnarNeural", "id-ID-ArdiNeural", "id-ID-GadisNeural", "ga-IE-ColmNeural", "ga-IE-OrlaNeural", "it-IT-GiuseppeMultilingualNeural", "it-IT-DiegoNeural", "it-IT-ElsaNeural", "it-IT-IsabellaNeural", "ja-JP-KeitaNeural", "ja-JP-NanamiNeural", "jv-ID-DimasNeural", "jv-ID-SitiNeural", "kn-IN-GaganNeural", "kn-IN-SapnaNeural", "kk-KZ-AigulNeural", "kk-KZ-DauletNeural", "km-KH-PisethNeural", "km-KH-SreymomNeural", "ko-KR-HyunsuMultilingualNeural", "ko-KR-InJoonNeural", "ko-KR-SunHiNeural", "lo-LA-ChanthavongNeural", "lo-LA-KeomanyNeural", "lv-LV-EveritaNeural", "lv-LV-NilsNeural", "lt-LT-LeonasNeural", "lt-LT-OnaNeural", "mk-MK-AleksandarNeural", "mk-MK-MarijaNeural", "ms-MY-OsmanNeural", "ms-MY-YasminNeural", "ml-IN-MidhunNeural", "ml-IN-SobhanaNeural", "mt-MT-GraceNeural", "mt-MT-JosephNeural", "mr-IN-AarohiNeural", "mr-IN-ManoharNeural", "mn-MN-BataaNeural", "mn-MN-YesuiNeural", "ne-NP-HemkalaNeural", "ne-NP-SagarNeural", "nb-NO-FinnNeural", "nb-NO-PernilleNeural", "ps-AF-GulNawazNeural", "ps-AF-LatifaNeural", "fa-IR-DilaraNeural", "fa-IR-FaridNeural", "pl-PL-MarekNeural", "pl-PL-ZofiaNeural", "pt-BR-ThalitaMultilingualNeural", "pt-BR-AntonioNeural", "pt-BR-FranciscaNeural", "pt-PT-DuarteNeural", "pt-PT-RaquelNeural", "ro-RO-AlinaNeural", "ro-RO-EmilNeural", "ru-RU-DmitryNeural", "ru-RU-SvetlanaNeural", "sr-RS-NicholasNeural", "sr-RS-SophieNeural", "si-LK-SameeraNeural", "si-LK-ThiliniNeural", "sk-SK-LukasNeural", "sk-SK-ViktoriaNeural", "sl-SI-PetraNeural", "sl-SI-RokNeural", "so-SO-MuuseNeural", "so-SO-UbaxNeural", "es-AR-ElenaNeural", "es-AR-TomasNeural", "es-BO-MarceloNeural", "es-BO-SofiaNeural", "es-CL-CatalinaNeural", "es-CL-LorenzoNeural", "es-ES-XimenaNeural", "es-CO-GonzaloNeural", "es-CO-SalomeNeural", "es-CR-JuanNeural", "es-CR-MariaNeural", "es-CU-BelkysNeural", "es-CU-ManuelNeural", "es-DO-EmilioNeural", "es-DO-RamonaNeural", "es-EC-AndreaNeural", "es-EC-LuisNeural", "es-SV-LorenaNeural", "es-SV-RodrigoNeural", "es-GQ-JavierNeural", "es-GQ-TeresaNeural", "es-GT-AndresNeural", "es-GT-MartaNeural", "es-HN-CarlosNeural", "es-HN-KarlaNeural", "es-MX-DaliaNeural", "es-MX-JorgeNeural", "es-NI-FedericoNeural", "es-NI-YolandaNeural", "es-PA-MargaritaNeural", "es-PA-RobertoNeural", "es-PY-MarioNeural", "es-PY-TaniaNeural", "es-PE-AlexNeural", "es-PE-CamilaNeural", "es-PR-KarinaNeural", "es-PR-VictorNeural", "es-ES-AlvaroNeural", "es-ES-ElviraNeural", "es-US-AlonsoNeural", "es-US-PalomaNeural", "es-UY-MateoNeural", "es-UY-ValentinaNeural", "es-VE-PaolaNeural", "es-VE-SebastianNeural", "su-ID-JajangNeural", "su-ID-TutiNeural", "sw-KE-RafikiNeural", "sw-KE-ZuriNeural", "sw-TZ-DaudiNeural", "sw-TZ-RehemaNeural", "sv-SE-MattiasNeural", "sv-SE-SofieNeural", "ta-IN-PallaviNeural", "ta-IN-ValluvarNeural", "ta-MY-KaniNeural", "ta-MY-SuryaNeural", "ta-SG-AnbuNeural", "ta-SG-VenbaNeural", "ta-LK-KumarNeural", "ta-LK-SaranyaNeural", "te-IN-MohanNeural", "te-IN-ShrutiNeural", "th-TH-NiwatNeural", "th-TH-PremwadeeNeural", "tr-TR-AhmetNeural", "tr-TR-EmelNeural", "uk-UA-OstapNeural", "uk-UA-PolinaNeural", "uz-UZ-MadinaNeural", "uz-UZ-SardorNeural", "vi-VN-HoaiMyNeural", "vi-VN-NamMinhNeural", "cy-GB-AledNeural", "cy-GB-NiaNeural", "zu-ZA-ThandoNeural", "zu-ZA-ThembaNeural"]

XTTS_LANGUAGES = ["en", "es", "fr", "de", "it", "pt", "pl", "tr", "ru", "nl", "cs", "ar", "zh-cn", "ja", "hu", "ko", "hi"]

def parse_model(model_name: str) -> any:
    if model_name == "GPT4":
        return g4f.models.gpt_4
    elif model_name == "GPT3":
        return g4f.models.gpt_35_turbo
    elif model_name == "Llama":
        return g4f.models.llama2_70b
    elif model_name == "Mixtral":
        return g4f.models.mixtral_8x7b
    else:
        return g4f.models.gpt_35_turbo
