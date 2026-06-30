import os
import zipfile
import urllib.request

print("🚀 جاري إنشاء مشروع 'حقي كيمني'...")
print("=" * 60)

# ==================== إعدادات المشروع ====================
project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)
zip_filename = f"{project_name}.zip"

# ==================== إنشاء المجلدات ====================
directories = [
    f"{base_dir}/lib/core/config/theme",
    f"{base_dir}/lib/core/services",
    f"{base_dir}/lib/features/auth/screens",
    f"{base_dir}/lib/features/home/screens",
    f"{base_dir}/lib/features/laws/screens",
    f"{base_dir}/lib/features/consultations/screens",
    f"{base_dir}/lib/features/profile/screens",
    f"{base_dir}/lib/features/lawyer/screens",
    f"{base_dir}/lib/features/about/screens",
    f"{base_dir}/lib/features/faq/screens",
    f"{base_dir}/lib/providers",
    f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app",
    f"{base_dir}/android/gradle/wrapper",
    f"{base_dir}/ios/Runner",
    f"{base_dir}/assets/images",
    f"{base_dir}/assets/icons",
    f"{base_dir}/assets/fonts",
    f"{base_dir}/test",
]

for dir_path in directories:
    os.makedirs(dir_path, exist_ok=True)

# ==================== دالة كتابة الملفات ====================
def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ==================== توليد الشعار ====================
print("\n🎨 جاري توليد صورة الشعار...")
try:
    from PIL import Image, ImageDraw
    
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    yemeni_green = (27, 94, 32, 255)
    yemeni_red = (198, 40, 40, 255)
    yemeni_white = (255, 255, 255, 255)
    yemeni_black = (33, 33, 33, 255)
    gold = (255, 215, 0, 255)
    
    shield_points = [
        (size//2, 80), (size - 120, 150), (size - 120, size//2 + 100),
        (size//2, size - 80), (120, size//2 + 100), (120, 150),
    ]
    draw.polygon(shield_points, fill=yemeni_green, outline=gold, width=15)
    
    stripe_height = (size - 260) // 3
    draw.rectangle([140, 170, size-140, 170+stripe_height], fill=yemeni_red)
    draw.rectangle([140, 170+stripe_height, size-140, 170+stripe_height*2], fill=yemeni_white)
    draw.rectangle([140, 170+stripe_height*2, size-140, 170+stripe_height*3], fill=yemeni_black)
    
    center_x = size // 2
    draw.rectangle([center_x-15, 280, center_x+15, 700], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([center_x-120, 700, center_x+120, 730], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([center_x-150, 730, center_x+150, 760], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([180, 280, size-180, 310], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([center_x-25, 240, center_x+25, 290], fill=gold, outline=yemeni_black, width=3)
    
    draw.line([220, 310, 220, 500], fill=gold, width=8)
    draw.line([180, 500, 260, 500], fill=gold, width=8)
    draw.polygon([(180, 500), (260, 500), (240, 620), (200, 620)], fill=gold, outline=yemeni_black, width=3)
    
    draw.line([size-220, 310, size-220, 500], fill=gold, width=8)
    draw.line([size-260, 500, size-180, 500], fill=gold, width=8)
    draw.polygon([(size-260, 500), (size-180, 500), (size-200, 620), (size-240, 620)], fill=gold, outline=yemeni_black, width=3)
    
    draw.ellipse([170, 270, 230, 330], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([size-230, 270, size-170, 330], fill=gold, outline=yemeni_black, width=3)
    
    icons_dir = f"{base_dir}/assets/icons"
    images_dir = f"{base_dir}/assets/images"
    
    img.save(f"{icons_dir}/app_icon.png", "PNG")
    img.save(f"{images_dir}/logo.png", "PNG")
    
    bg_img = Image.new('RGBA', (size, size), yemeni_green)
    bg_img.paste(img, (0, 0), img)
    bg_img.save(f"{icons_dir}/app_icon_bg.png", "PNG")
    
    print("✅ تم توليد الشعار بنجاح!")
    
except ImportError:
    print("⚠️  مكتبة Pillow غير مثبتة. جاري تثبيتها...")
    os.system("pip install Pillow")
    print("✅ تم تثبيت Pillow. يرجى إعادة تشغيل السكريبت.")
    exit()

# ==================== تحميل الخطوط العربية ====================
print("\n📝 جاري تحميل الخطوط العربية...")
fonts_to_download = {
    "Cairo-Regular.ttf": "https://github.com/googlefonts/CairoFont/raw/main/fonts/ttf/Cairo-Regular.ttf",
    "Cairo-Bold.ttf": "https://github.com/googlefonts/CairoFont/raw/main/fonts/ttf/Cairo-Bold.ttf",
    "Cairo-SemiBold.ttf": "https://github.com/googlefonts/CairoFont/raw/main/fonts/ttf/Cairo-SemiBold.ttf",
    "Tajawal-Regular.ttf": "https://github.com/googlefonts/TajawalFont/raw/main/fonts/ttf/Tajawal-Regular.ttf",
    "Tajawal-Bold.ttf": "https://github.com/googlefonts/TajawalFont/raw/main/fonts/ttf/Tajawal-Bold.ttf",
}

fonts_dir = f"{base_dir}/assets/fonts"
for font_name, font_url in fonts_to_download.items():
    font_path = f"{fonts_dir}/{font_name}"
    try:
        urllib.request.urlretrieve(font_url, font_path)
    except Exception as e:
        print(f"⚠️  فشل تحميل {font_name}: {e}")

# ==================== كتابة جميع الملفات ====================
# (نفس الملفات السابقة - انسخها من السكريبت السابق)

# pubspec.yaml
write_file(f"{base_dir}/pubspec.yaml", '''name: my_yemeni_right
description: حقي كيمني - التطبيق القانوني الشامل للمواطن اليمني
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: ^0.18.1
  provider: ^6.0.5
  flutter_riverpod: ^2.4.0
  go_router: ^12.0.0
  firebase_core: ^2.24.0
  firebase_auth: ^4.15.0
  cloud_firestore: ^4.13.0
  firebase_storage: ^11.5.0
  firebase_messaging: ^14.7.0
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  path_provider: ^2.1.1
  cupertino_icons: ^1.0.6
  flutter_svg: ^2.0.9
  cached_network_image: ^3.3.0
  shimmer: ^3.0.0
  flutter_form_builder: ^9.1.1
  form_builder_validators: ^9.1.0
  url_launcher: ^6.2.1
  share_plus: ^7.2.1
  image_picker: ^1.0.5
  file_picker: ^6.1.1
  permission_handler: ^11.0.1
  dio: ^5.4.0
  connectivity_plus: ^5.0.2
  pin_code_fields: ^8.0.1
  font_awesome_flutter: ^10.6.0
  lottie: ^2.7.0
  animate_do: ^3.1.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1
  hive_generator: ^2.0.1
  build_runner: ^2.4.7
  flutter_launcher_icons: ^0.13.1

flutter:
  uses-material-design: true
  assets:
    - assets/images/
    - assets/icons/
    - assets/laws/
  fonts:
    - family: Cairo
      fonts:
        - asset: assets/fonts/Cairo-Regular.ttf
        - asset: assets/fonts/Cairo-Bold.ttf
          weight: 700
        - asset: assets/fonts/Cairo-SemiBold.ttf
          weight: 600
    - family: Tajawal
      fonts:
        - asset: assets/fonts/Tajawal-Regular.ttf
        - asset: assets/fonts/Tajawal-Bold.ttf
          weight: 700

flutter_icons:
  android: true
  ios: true
  image_path: "assets/icons/app_icon.png"
  adaptive_icon_background: "#1B5E20"
''')

# main.dart
write_file(f"{base_dir}/lib/main.dart", '''import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:provider/provider.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'core/config/routes.dart';
import 'core/config/theme/app_theme.dart';
import 'core/services/local_storage_service.dart';
import 'providers/auth_provider.dart';
import 'providers/law_provider.dart';
import 'providers/consultation_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await Hive.initFlutter();
  await LocalStorageService.init();
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  runApp(const ProviderScope(child: MyApp()));
}

class MyApp extends ConsumerWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
        ChangeNotifierProvider(create: (_) => LawProvider()),
        ChangeNotifierProvider(create: (_) => ConsultationProvider()),
      ],
      child: MaterialApp.router(
        title: 'حقي كيمني',
        debugShowCheckedModeBanner: false,
        locale: const Locale('ar', 'YE'),
        localizationsDelegates: const [
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          GlobalCupertinoLocalizations.delegate,
        ],
        supportedLocales: const [Locale('ar', 'YE'), Locale('ar', 'SA')],
        theme: AppTheme.lightTheme,
        darkTheme: AppTheme.darkTheme,
        themeMode: ThemeMode.system,
        routerConfig: AppRouter.router,
        builder: (context, child) {
          return Directionality(
            textDirection: TextDirection.rtl,
            child: child!,
          );
        },
      ),
    );
  }
}
''')

# باقي الملفات... (انسخها من السكريبت السابق)

# ==================== ضغط المشروع في ZIP ====================
print("\n📦 جاري ضغط المشروع...")

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(base_dir))
            zipf.write(file_path, arcname)

print(f"✅ تم ضغط المشروع في: {zip_filename}")
print(f"📊 حجم الملف: {os.path.getsize(zip_filename) / 1024 / 1024:.2f} MB")

print("\n" + "="*60)
print("✅ تم إنشاء المشروع بنجاح!")
print("="*60)
print(f"\n📁 المجلد: {base_dir}")
print(f"📦 ملف ZIP: {zip_filename}")
print("\n📋 الخطوات التالية:")
print("1. ارفع ملف ZIP إلى GitHub")
print("2. حمّله وفك الضغط")
print("3. افتحه في Android Studio")
print("4. flutter pub get")
print("5. flutter build apk --release")
print("="*60)