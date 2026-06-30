import os
import zipfile

print("🚀 جاري إنشاء مشروع 'حقي كيمني'...")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

# إنشاء المجلدات
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
    print(f"✓ {dir_path.replace(base_dir + os.sep, '')}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {path.replace(base_dir + os.sep, '')}")

# 1. pubspec.yaml
write_file(f"{base_dir}/pubspec.yaml", """name: my_yemeni_right
description: حقي كيمني - التطبيق القانوني الشامل
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
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  path_provider: ^2.1.1
  cupertino_icons: ^1.0.6
  pin_code_fields: ^8.0.1
  image_picker: ^1.0.5
  permission_handler: ^11.0.1

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1

flutter:
  uses-material-design: true
  assets:
    - assets/images/
    - assets/icons/
  fonts:
    - family: Cairo
      fonts:
        - asset: assets/fonts/Cairo-Regular.ttf
""")

# 2. main.dart
write_file(f"{base_dir}/lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';
import 'core/config/routes.dart';
import 'core/config/theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'حقي كيمني',
      debugShowCheckedModeBanner: false,
      locale: const Locale('ar', 'YE'),
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [Locale('ar', 'YE')],
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
    );
  }
}
""")

# 3. app_theme.dart
write_file(f"{base_dir}/lib/core/config/theme/app_theme.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class AppTheme {
  static const Color yemeniGreen = Color(0xFF1B5E20);
  static const Color yemeniRed = Color(0xFFC62828);
  static const Color yemeniWhite = Color(0xFFFFFFFF);
  static const Color goldAccent = Color(0xFFFFD700);
  static const Color lightGreen = Color(0xFF4CAF50);
  static const Color darkGreen = Color(0xFF1B5E20);
  static const Color backgroundLight = Color(0xFFF5F5F5);
  static const Color backgroundDark = Color(0xFF121212);
  static const Color textSecondaryLight = Color(0xFF757575);
  static const Color textPrimaryDark = Color(0xFFFFFFFF);
  static const Color textSecondaryDark = Color(0xFFB0B0B0);

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      primaryColor: yemeniGreen,
      scaffoldBackgroundColor: backgroundLight,
      colorScheme: const ColorScheme.light(
        primary: yemeniGreen,
        secondary: goldAccent,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: yemeniGreen,
        foregroundColor: yemeniWhite,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: TextStyle(
          fontFamily: 'Cairo',
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: yemeniWhite,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: yemeniGreen,
          foregroundColor: yemeniWhite,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          textStyle: const TextStyle(fontFamily: 'Cairo', fontSize: 16, fontWeight: FontWeight.bold),
        ),
      ),
      textTheme: const TextTheme(
        headlineLarge: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold),
        titleLarge: TextStyle(fontFamily: 'Cairo', fontSize: 20, fontWeight: FontWeight.bold),
        bodyLarge: TextStyle(fontFamily: 'Cairo', fontSize: 16),
        bodyMedium: TextStyle(fontFamily: 'Cairo', fontSize: 14, color: textSecondaryLight),
      ),
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      primaryColor: yemeniGreen,
      scaffoldBackgroundColor: backgroundDark,
      colorScheme: const ColorScheme.dark(
        primary: lightGreen,
        secondary: goldAccent,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: darkGreen,
        foregroundColor: yemeniWhite,
        elevation: 0,
        centerTitle: true,
      ),
      textTheme: const TextTheme(
        headlineLarge: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold, color: textPrimaryDark),
        bodyLarge: TextStyle(fontFamily: 'Cairo', fontSize: 16, color: textPrimaryDark),
        bodyMedium: TextStyle(fontFamily: 'Cairo', fontSize: 14, color: textSecondaryDark),
      ),
    );
  }
}
""")

# 4. routes.dart
write_file(f"{base_dir}/lib/core/config/routes.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../features/auth/screens/login_screen.dart';
import '../../features/auth/screens/register_screen.dart';
import '../../features/home/screens/home_screen.dart';
import '../../features/laws/screens/laws_list_screen.dart';
import '../../features/consultations/screens/consultations_list_screen.dart';
import '../../features/profile/screens/profile_screen.dart';
import '../../features/about/screens/about_screen.dart';
import '../../features/about/screens/privacy_screen.dart';
import '../../features/about/screens/terms_screen.dart';
import '../../features/faq/screens/faq_screen.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/login',
    routes: [
      GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
      GoRoute(path: '/register', builder: (context, state) => const RegisterScreen()),
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(path: '/laws', builder: (context, state) => const LawsListScreen()),
      GoRoute(path: '/consultations', builder: (context, state) => const ConsultationsListScreen()),
      GoRoute(path: '/profile', builder: (context, state) => const ProfileScreen()),
      GoRoute(path: '/about', builder: (context, state) => const AboutScreen()),
      GoRoute(path: '/privacy', builder: (context, state) => const PrivacyScreen()),
      GoRoute(path: '/terms', builder: (context, state) => const TermsScreen()),
      GoRoute(path: '/faq', builder: (context, state) => const FaqScreen()),
    ],
    errorBuilder: (context, state) => Scaffold(
      appBar: AppBar(title: const Text('خطأ')),
      body: const Center(child: Text('الصفحة غير موجودة')),
    ),
  );
}
""")

# 5. login_screen.dart
write_file(f"{base_dir}/lib/features/auth/screens/login_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  
  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 60),
              Icon(Icons.balance, size: 100, color: AppTheme.yemeniGreen),
              const SizedBox(height: 24),
              const Text('حقي كيمني', textAlign: TextAlign.center, 
                style: TextStyle(fontFamily: 'Cairo', fontSize: 32, 
                fontWeight: FontWeight.bold, color: AppTheme.yemeniGreen)),
              const SizedBox(height: 8),
              const Text('تسجيل الدخول', textAlign: TextAlign.center, 
                style: TextStyle(fontFamily: 'Cairo', fontSize: 18)),
              const SizedBox(height: 48),
              TextField(controller: _emailController, 
                decoration: const InputDecoration(labelText: 'البريد الإلكتروني', 
                prefixIcon: Icon(Icons.email_outlined))),
              const SizedBox(height: 16),
              TextField(controller: _passwordController, obscureText: true, 
                decoration: const InputDecoration(labelText: 'كلمة المرور', 
                prefixIcon: Icon(Icons.lock_outlined))),
              const SizedBox(height: 24),
              ElevatedButton(onPressed: () => context.go('/'), 
                child: const Text('تسجيل الدخول')),
              const SizedBox(height: 24),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                const Text('ليس لديك حساب؟'),
                TextButton(onPressed: () => context.push('/register'), 
                  child: const Text('إنشاء حساب جديد')),
              ]),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# 6. register_screen.dart
write_file(f"{base_dir}/lib/features/auth/screens/register_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  
  @override
  void dispose() {
    _nameController.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('إنشاء حساب جديد')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Icon(Icons.person_add, size: 80, color: AppTheme.yemeniGreen),
            const SizedBox(height: 24),
            TextField(controller: _nameController, 
              decoration: const InputDecoration(labelText: 'الاسم الكامل')),
            const SizedBox(height: 16),
            TextField(controller: _emailController, 
              decoration: const InputDecoration(labelText: 'البريد الإلكتروني')),
            const SizedBox(height: 16),
            TextField(controller: _passwordController, obscureText: true, 
              decoration: const InputDecoration(labelText: 'كلمة المرور')),
            const SizedBox(height: 24),
            ElevatedButton(onPressed: () => context.go('/'), 
              child: const Text('إنشاء الحساب')),
          ],
        ),
      ),
    );
  }
}
""")

# 7. home_screen.dart
write_file(f"{base_dir}/lib/features/home/screens/home_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;
  final List<Widget> _screens = const [HomeTab(), LawsTab(), ConsultationsTab(), ProfileTab()];
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selectedIndex,
        onDestinationSelected: (index) => setState(() => _selectedIndex = index),
        destinations: const [
          NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'الرئيسية'),
          NavigationDestination(icon: Icon(Icons.library_books_outlined), selectedIcon: Icon(Icons.library_books), label: 'القوانين'),
          NavigationDestination(icon: Icon(Icons.chat_outlined), selectedIcon: Icon(Icons.chat), label: 'الاستشارات'),
          NavigationDestination(icon: Icon(Icons.person_outline), selectedIcon: Icon(Icons.person), label: 'حسابي'),
        ],
      ),
    );
  }
}

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});
  @override
  Widget build(BuildContext context) {
    return CustomScrollView(slivers: [
      SliverAppBar(floating: true, title: const Text('حقي كيمني')),
      SliverToBoxAdapter(child: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(colors: [AppTheme.yemeniGreen, AppTheme.lightGreen]),
        ),
        padding: const EdgeInsets.all(24),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('مرحباً بك', style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('موسوعتك القانونية الشاملة', style: TextStyle(color: Colors.white70, fontSize: 16)),
          const SizedBox(height: 16),
          ElevatedButton.icon(
            onPressed: () => context.push('/laws'),
            icon: const Icon(Icons.search),
            label: const Text('ابحث في القوانين'),
          ),
        ]),
      )),
      SliverPadding(
        padding: const EdgeInsets.all(16),
        sliver: SliverGrid(
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2, childAspectRatio: 1.2, crossAxisSpacing: 12, mainAxisSpacing: 12),
          delegate: SliverChildBuilderDelegate((context, index) {
            final items = [
              {'icon': Icons.gavel, 'title': 'الدستور'},
              {'icon': Icons.work, 'title': 'قانون العمل'},
              {'icon': Icons.family_restroom, 'title': 'الأحوال الشخصية'},
              {'icon': Icons.school, 'title': 'قانون التعليم'},
            ];
            final item = items[index];
            return Card(child: InkWell(
              onTap: () => context.push('/laws'),
              borderRadius: BorderRadius.circular(12),
              child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
                Icon(item['icon'] as IconData, size: 40, color: AppTheme.yemeniGreen),
                const SizedBox(height: 8),
                Text(item['title'] as String, style: const TextStyle(fontWeight: FontWeight.bold)),
              ]),
            ));
          }, childCount: 4),
        ),
      ),
    ]);
  }
}

class LawsTab extends StatelessWidget {
  const LawsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('القوانين'));
}

class ConsultationsTab extends StatelessWidget {
  const ConsultationsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('الاستشارات'));
}

class ProfileTab extends StatelessWidget {
  const ProfileTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('الملف الشخصي'));
}
""")

# 8. laws_list_screen.dart
write_file(f"{base_dir}/lib/features/laws/screens/laws_list_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class LawsListScreen extends StatelessWidget {
  const LawsListScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('الموسوعة القانونية')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _buildLawCard('الدستور اليمني', '150 مادة'),
          _buildLawCard('قانون العمل اليمني', '200 مادة'),
          _buildLawCard('قانون الأحوال الشخصية', '180 مادة'),
          _buildLawCard('قانون التعليم', '120 مادة'),
          _buildLawCard('قانون الجرائم والعقوبات', '250 مادة'),
        ],
      ),
    );
  }
  
  Widget _buildLawCard(String title, String subtitle) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
          child: const Icon(Icons.article, color: AppTheme.yemeniGreen)),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text(subtitle),
        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
      ),
    );
  }
}
""")

# 9. consultations_list_screen.dart
write_file(f"{base_dir}/lib/features/consultations/screens/consultations_list_screen.dart", """import 'package:flutter/material.dart';

class ConsultationsListScreen extends StatelessWidget {
  const ConsultationsListScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('استشاراتي')),
      body: const Center(child: Text('لا توجد استشارات بعد')),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.add),
      ),
    );
  }
}
""")

# 10. profile_screen.dart
write_file(f"{base_dir}/lib/features/profile/screens/profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('ملفي الشخصي')),
      body: ListView(
        children: [
          const SizedBox(height: 24),
          CircleAvatar(radius: 60, backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
            child: const Icon(Icons.person, size: 60, color: AppTheme.yemeniGreen)),
          const SizedBox(height: 16),
          const Text('مستخدم', textAlign: TextAlign.center, 
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 24),
          ListTile(leading: const Icon(Icons.info_outline), 
            title: const Text('من نحن'), 
            onTap: () => context.push('/about')),
          ListTile(leading: const Icon(Icons.privacy_tip_outlined), 
            title: const Text('الخصوصية'), 
            onTap: () => context.push('/privacy')),
          ListTile(leading: const Icon(Icons.description), 
            title: const Text('الشروط'), 
            onTap: () => context.push('/terms')),
          ListTile(leading: const Icon(Icons.help_outline), 
            title: const Text('الأسئلة الشائعة'), 
            onTap: () => context.push('/faq')),
        ],
      ),
    );
  }
}
""")

# 11. about_screen.dart
write_file(f"{base_dir}/lib/features/about/screens/about_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('من نحن')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(children: [
          Icon(Icons.balance, size: 80, color: AppTheme.yemeniGreen),
          const SizedBox(height: 24),
          const Text('حقي كيمني', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
          const SizedBox(height: 16),
          const Text('موسوعتك القانونية الشاملة', style: TextStyle(fontSize: 16)),
          const SizedBox(height: 32),
          const Text('رؤيتنا: أن نكون المرجع القانوني الأول لكل مواطن يمني', 
            style: TextStyle(fontSize: 16, height: 1.6)),
          const SizedBox(height: 16),
          const Text('رسالتنا: توفير المعلومات القانونية الموثوقة والمبسطة', 
            style: TextStyle(fontSize: 16, height: 1.6)),
          const SizedBox(height: 32),
          const Text('الإصدار 1.0.0\\nجميع الحقوق محفوظة © 2024', 
            textAlign: TextAlign.center, style: TextStyle(color: Colors.grey)),
        ]),
      ),
    );
  }
}
""")

# 12. privacy_screen.dart
write_file(f"{base_dir}/lib/features/about/screens/privacy_screen.dart", """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('سياسة الخصوصية')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('مقدمة', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('نرحب بك في تطبيق "حقي كيمني". نحن نلتزم بحماية خصوصيتك.', 
            style: TextStyle(fontSize: 16, height: 1.6)),
          const SizedBox(height: 24),
          const Text('المعلومات التي نجمعها', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('نقوم بجمع المعلومات التي تقدمها لنا عند التسجيل.', 
            style: TextStyle(fontSize: 16, height: 1.6)),
        ]),
      ),
    );
  }
}
""")

# 13. terms_screen.dart
write_file(f"{base_dir}/lib/features/about/screens/terms_screen.dart", """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('شروط الاستخدام')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('شروط وأحكام الاستخدام', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 24),
          const Text('1. قبول الشروط', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('باستخدامك للتطبيق، فإنك توافق على الالتزام بهذه الشروط.', 
            style: TextStyle(fontSize: 16, height: 1.6)),
        ]),
      ),
    );
  }
}
""")

# 14. faq_screen.dart
write_file(f"{base_dir}/lib/features/faq/screens/faq_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('الأسئلة الشائعة')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _buildFaq('كم مدة إجازة الوضع؟', '60 يوماً وفقاً لقانون العمل اليمني'),
          _buildFaq('ما هي حقوق المرأة في الميراث؟', 'كفل القانون والشريعة للمرأة حقها في الميراث'),
          _buildFaq('هل يحق فصل العامل دون سبب؟', 'لا، يحق للعامل المطالبة بتعويض'),
        ],
      ),
    );
  }
  
  Widget _buildFaq(String question, String answer) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ExpansionTile(
        leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
          child: const Icon(Icons.help_outline, color: AppTheme.yemeniGreen)),
        title: Text(question, style: const TextStyle(fontWeight: FontWeight.bold)),
        children: [Padding(padding: const EdgeInsets.all(16), child: Text(answer))],
      ),
    );
  }
}
""")

# 15. AndroidManifest.xml
write_file(f"{base_dir}/android/app/src/main/AndroidManifest.xml", """<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET"/>
    <application
        android:label="حقي كيمني"
        android:name="${'$'}{applicationName}"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <meta-data android:name="io.flutter.embedding.android.NormalTheme" android:resource="@style/NormalTheme"/>
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <meta-data android:name="flutterEmbedding" android:value="2"/>
    </application>
</manifest>
""")

# 16. MainActivity.kt
write_file(f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity()
""")

# 17. README.md
write_file(f"{base_dir}/README.md", """# حقي كيمني - My Yemeni Right
التطبيق القانوني الشامل للمواطن اليمني

## خطوات البناء
1. flutter pub get
2. flutter build apk --release
""")

# 18. .gitignore
write_file(f"{base_dir}/.gitignore", """.dart_tool/
.packages
.pub/
build/
.flutter-plugins
.flutter-plugins-dependencies
.idea/
.vscode/
*.iml
.DS_Store
Thumbs.db
""")

# 19. إنشاء صورة شعار بسيطة
try:
    from PIL import Image, ImageDraw
    size = 512
    img = Image.new('RGBA', (size, size), (27, 94, 32, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse([156, 156, 356, 356], fill=(255, 215, 0, 255))
    draw.text((200, 220), "⚖", fill=(27, 94, 32, 255))
    img.save(f"{base_dir}/assets/icons/app_icon.png", "PNG")
    print("✓ تم إنشاء الشعار")
except:
    print("⚠ تم تخطي إنشاء الشعار (Pillow غير متوفرة)")

# ضغط المشروع في ZIP
print("\n📦 جاري ضغط المشروع...")
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(base_dir))
            zipf.write(file_path, arcname)

print(f"✅ تم ضغط المشروع في: {zip_filename}")
print(f" الحجم: {os.path.getsize(zip_filename) / 1024 / 1024:.2f} MB")
print("\n" + "=" * 60)
print("✅ تم إنشاء المشروع بنجاح!")
print("=" * 60)
