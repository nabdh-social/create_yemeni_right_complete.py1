import os
import zipfile

print("🚀 بناء مشروع 'حقي كيمني' - نسخة نظيفة")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

# إنشاء المجلدات
directories = [
    f"{base_dir}/lib/core/theme",
    f"{base_dir}/lib/features/auth",
    f"{base_dir}/lib/features/home",
    f"{base_dir}/lib/features/laws",
    f"{base_dir}/lib/features/consultations",
    f"{base_dir}/lib/features/profile",
    f"{base_dir}/lib/features/about",
    f"{base_dir}/lib/features/faq",
    f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app",
    f"{base_dir}/android/app/src/main/res/values",
    f"{base_dir}/assets/images",
    f"{base_dir}/assets/icons",
]

for d in directories:
    os.makedirs(d, exist_ok=True)
    print(f"✓ {d.replace(base_dir + os.sep, '')}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {path.replace(base_dir + os.sep, '')}")

# ==================== 1. pubspec.yaml ====================
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
  cupertino_icons: ^1.0.6
  go_router: ^12.0.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1

flutter:
  uses-material-design: true
  assets:
    - assets/images/
    - assets/icons/
""")

# ==================== 2. main.dart ====================
write_file(f"{base_dir}/lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'core/theme/app_theme.dart';
import 'features/auth/login_screen.dart';
import 'features/home/home_screen.dart';
import 'features/laws/laws_screen.dart';
import 'features/consultations/consultations_screen.dart';
import 'features/profile/profile_screen.dart';
import 'features/about/about_screen.dart';
import 'features/about/privacy_screen.dart';
import 'features/about/terms_screen.dart';
import 'features/faq/faq_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
  ]);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
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
      initialRoute: '/login',
      routes: {
        '/login': (context) => const LoginScreen(),
        '/home': (context) => const HomeScreen(),
        '/laws': (context) => const LawsScreen(),
        '/consultations': (context) => const ConsultationsScreen(),
        '/profile': (context) => const ProfileScreen(),
        '/about': (context) => const AboutScreen(),
        '/privacy': (context) => const PrivacyScreen(),
        '/terms': (context) => const TermsScreen(),
        '/faq': (context) => const FaqScreen(),
      },
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

# ==================== 3. app_theme.dart ====================
write_file(f"{base_dir}/lib/core/theme/app_theme.dart", """import 'package:flutter/material.dart';

class AppTheme {
  static const Color yemeniGreen = Color(0xFF1B5E20);
  static const Color yemeniRed = Color(0xFFC62828);
  static const Color goldAccent = Color(0xFFFFD700);
  static const Color lightGreen = Color(0xFF4CAF50);

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      primaryColor: yemeniGreen,
      scaffoldBackgroundColor: const Color(0xFFF5F5F5),
      colorScheme: const ColorScheme.light(
        primary: yemeniGreen,
        secondary: goldAccent,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: yemeniGreen,
        foregroundColor: Colors.white,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: TextStyle(
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: Colors.white,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: yemeniGreen,
          foregroundColor: Colors.white,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      primaryColor: yemeniGreen,
      colorScheme: const ColorScheme.dark(
        primary: lightGreen,
        secondary: goldAccent,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: yemeniGreen,
        foregroundColor: Colors.white,
      ),
    );
  }
}
""")

# ==================== 4. login_screen.dart ====================
write_file(f"{base_dir}/lib/features/auth/login_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

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
              const Icon(Icons.balance, size: 100, color: AppTheme.yemeniGreen),
              const SizedBox(height: 24),
              const Text(
                'حقي كيمني',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.yemeniGreen,
                ),
              ),
              const SizedBox(height: 8),
              const Text(
                'الموسوعة القانونية الشاملة',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 16, color: Colors.grey),
              ),
              const SizedBox(height: 48),
              TextField(
                controller: _emailController,
                decoration: const InputDecoration(
                  labelText: 'البريد الإلكتروني',
                  prefixIcon: Icon(Icons.email),
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: const InputDecoration(
                  labelText: 'كلمة المرور',
                  prefixIcon: Icon(Icons.lock),
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () {
                  Navigator.pushReplacementNamed(context, '/home');
                },
                child: const Text('تسجيل الدخول'),
              ),
              const SizedBox(height: 16),
              OutlinedButton.icon(
                onPressed: () {
                  Navigator.pushReplacementNamed(context, '/home');
                },
                icon: const Icon(Icons.phone),
                label: const Text('الدخول برقم الهاتف'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# ==================== 5. home_screen.dart ====================
write_file(f"{base_dir}/lib/features/home/home_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';
import 'home_tab.dart';
import '../laws/laws_screen.dart';
import '../consultations/consultations_screen.dart';
import '../profile/profile_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = const [
    HomeTab(),
    LawsScreen(),
    ConsultationsScreen(),
    ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _currentIndex,
        onDestinationSelected: (index) {
          setState(() => _currentIndex = index);
        },
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.home_outlined),
            selectedIcon: Icon(Icons.home),
            label: 'الرئيسية',
          ),
          NavigationDestination(
            icon: Icon(Icons.library_books_outlined),
            selectedIcon: Icon(Icons.library_books),
            label: 'القوانين',
          ),
          NavigationDestination(
            icon: Icon(Icons.chat_outlined),
            selectedIcon: Icon(Icons.chat),
            label: 'الاستشارات',
          ),
          NavigationDestination(
            icon: Icon(Icons.person_outline),
            selectedIcon: Icon(Icons.person),
            label: 'حسابي',
          ),
        ],
      ),
    );
  }
}
""")

# ==================== 6. home_tab.dart ====================
write_file(f"{base_dir}/lib/features/home/home_tab.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('حقي كيمني'),
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {},
          ),
          IconButton(
            icon: const Icon(Icons.notifications),
            onPressed: () {},
          ),
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(24),
              decoration: const BoxDecoration(
                gradient: LinearGradient(
                  colors: [AppTheme.yemeniGreen, AppTheme.lightGreen],
                  begin: Alignment.topRight,
                  end: Alignment.bottomLeft,
                ),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'مرحباً بك'
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'موسوعتك القانونية الشاملة',
                    style: TextStyle(color: Colors.white70, fontSize: 16),
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: GridView.count(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                crossAxisCount: 2,
                childAspectRatio: 1.2,
                crossAxisSpacing: 12,
                mainAxisSpacing: 12,
                children: [
                  _buildCategoryCard(context, Icons.gavel, 'الدستور'),
                  _buildCategoryCard(context, Icons.work, 'قانون العمل'),
                  _buildCategoryCard(context, Icons.family_restroom, 'الأحوال الشخصية'),
                  _buildCategoryCard(context, Icons.school, 'قانون التعليم'),
                  _buildCategoryCard(context, Icons.security, 'الجرائم والعقوبات'),
                  _buildCategoryCard(context, Icons.accessible, 'حقوق ذوي الإعاقة'),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCategoryCard(BuildContext context, IconData icon, String title) {
    return Card(
      child: InkWell(
        onTap: () => Navigator.pushNamed(context, '/laws'),
        borderRadius: BorderRadius.circular(12),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 40, color: AppTheme.yemeniGreen),
            const SizedBox(height: 8),
            Text(
              title,
              style: const TextStyle(fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }
}
""")

# ==================== 7. laws_screen.dart ====================
write_file(f"{base_dir}/lib/features/laws/laws_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class LawsScreen extends StatelessWidget {
  const LawsScreen({super.key});

  final List<Map<String, String>> laws = const [
    {'title': 'الدستور اليمني', 'count': '150 مادة'},
    {'title': 'قانون العمل اليمني', 'count': '200 مادة'},
    {'title': 'قانون الأحوال الشخصية', 'count': '180 مادة'},
    {'title': 'قانون التعليم', 'count': '120 مادة'},
    {'title': 'قانون الجرائم والعقوبات', 'count': '250 مادة'},
    {'title': 'قانون الإجراءات الجزائية', 'count': '170 مادة'},
    {'title': 'حقوق ذوي الإعاقة', 'count': '90 مادة'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('الموسوعة القانونية')),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: laws.length,
        itemBuilder: (context, index) {
          final law = laws[index];
          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
                child: const Icon(Icons.article, color: AppTheme.yemeniGreen),
              ),
              title: Text(
                law['title']!,
                style: const TextStyle(fontWeight: FontWeight.bold),
              ),
              subtitle: Text(law['count']!),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
              onTap: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('فتح: \${law['title']}')),
                );
              },
            ),
          );
        },
      ),
    );
  }
}
""")

# ==================== 8. consultations_screen.dart ====================
write_file(f"{base_dir}/lib/features/consultations/consultations_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class ConsultationsScreen extends StatelessWidget {
  const ConsultationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('الاستشارات القانونية')),
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.chat_bubble_outline, size: 80, color: Colors.grey),
            SizedBox(height: 16),
            Text(
              'لا توجد استشارات حالياً',
              style: TextStyle(fontSize: 18, color: Colors.grey),
            ),
            SizedBox(height: 8),
            Text(
              'اضغط الزر أدناه لبدء استشارة جديدة',
              style: TextStyle(color: Colors.grey),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('إنشاء استشارة جديدة')),
          );
        },
        icon: const Icon(Icons.add),
        label: const Text('استشارة جديدة'),
      ),
    );
  }
}
""")

# ==================== 9. profile_screen.dart ====================
write_file(f"{base_dir}/lib/features/profile/profile_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('ملفي الشخصي')),
      body: ListView(
        children: [
          const SizedBox(height: 24),
          const CircleAvatar(
            radius: 60,
            backgroundColor: AppTheme.yemeniGreen,
            child: Icon(Icons.person, size: 60, color: Colors.white),
          ),
          const SizedBox(height: 16),
          const Text(
            'المستخدم',
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          const Text(
            'مواطن',
            textAlign: TextAlign.center,
            style: TextStyle(color: Colors.grey),
          ),
          const SizedBox(height: 32),
          _buildMenuItem(context, Icons.bookmark, 'المحفوظات', () {}),
          _buildMenuItem(context, Icons.help_outline, 'الأسئلة الشائعة', () {
            Navigator.pushNamed(context, '/faq');
          }),
          _buildMenuItem(context, Icons.info_outline, 'من نحن', () {
            Navigator.pushNamed(context, '/about');
          }),
          _buildMenuItem(context, Icons.privacy_tip, 'سياسة الخصوصية', () {
            Navigator.pushNamed(context, '/privacy');
          }),
          _buildMenuItem(context, Icons.description, 'شروط الاستخدام', () {
            Navigator.pushNamed(context, '/terms');
          }),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.logout, color: AppTheme.yemeniRed),
            title: const Text(
              'تسجيل الخروج',
              style: TextStyle(color: AppTheme.yemeniRed),
            ),
            onTap: () {
              showDialog(
                context: context,
                builder: (ctx) => AlertDialog(
                  title: const Text('تسجيل الخروج'),
                  content: const Text('هل أنت متأكد؟'),
                  actions: [
                    TextButton(
                      onPressed: () => Navigator.pop(ctx),
                      child: const Text('إلغاء'),
                    ),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.pop(ctx);
                        Navigator.pushNamedAndRemoveUntil(
                          context, '/login', (route) => false,
                        );
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppTheme.yemeniRed,
                      ),
                      child: const Text('خروج'),
                    ),
                  ],
                ),
              );
            },
          ),
        ],
      ),
    );
  }

  Widget _buildMenuItem(BuildContext context, IconData icon, String title, VoidCallback onTap) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      child: ListTile(
        leading: Icon(icon, color: AppTheme.yemeniGreen),
        title: Text(title),
        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
        onTap: onTap,
      ),
    );
  }
}
""")

# ==================== 10. about_screen.dart ====================
write_file(f"{base_dir}/lib/features/about/about_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('من نحن')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            const Icon(Icons.balance, size: 80, color: AppTheme.yemeniGreen),
            const SizedBox(height: 24),
            const Text(
              'حقي كيمني',
              style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            const Text(
              'الإصدار 1.0.0',
              style: TextStyle(color: Colors.grey),
            ),
            const SizedBox(height: 32),
            _buildSection('رؤيتنا', 'أن نكون المرجع القانوني الأول لكل مواطن يمني.'),
            const SizedBox(height: 16),
            _buildSection('رسالتنا', 'توفير المعلومات القانونية الموثوقة والمبسطة.'),
            const SizedBox(height: 32),
            const Text(
              'جميع الحقوق محفوظة © 2026',
              style: TextStyle(color: Colors.grey),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSection(String title, String content) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title,
          style: const TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: AppTheme.yemeniGreen,
          ),
        ),
        const SizedBox(height: 8),
        Text(
          content,
          style: const TextStyle(fontSize: 16, height: 1.6),
        ),
      ],
    );
  }
}
""")

# ==================== 11. privacy_screen.dart ====================
write_file(f"{base_dir}/lib/features/about/privacy_screen.dart", """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('سياسة الخصوصية')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'سياسة الخصوصية',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 24),
            const Text(
              'نحن نلتزم بحماية خصوصيتك وبياناتك الشخصية.',
              style: TextStyle(fontSize: 16, height: 1.6),
            ),
            const SizedBox(height: 16),
            const Text(
              'المعلومات التي نجمعها',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            const Text(
              'نقوم بجمع المعلومات التي تقدمها عند التسجيل فقط.',
              style: TextStyle(fontSize: 16, height: 1.6),
            ),
          ],
        ),
      ),
    );
  }
}
""")

# ==================== 12. terms_screen.dart ====================
write_file(f"{base_dir}/lib/features/about/terms_screen.dart", """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('شروط الاستخدام')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text(
              'شروط وأحكام الاستخدام',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 24),
            Text(
              '1. قبول الشروط',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              'باستخدامك للتطبيق، فإنك توافق على الالتزام بهذه الشروط.',
              style: TextStyle(fontSize: 16, height: 1.6),
            ),
            SizedBox(height: 16),
            Text(
              '2. طبيعة الخدمة',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              'يوفر التطبيق معلومات قانونية عامة واستشارات عبر محامين مرخصين.',
              style: TextStyle(fontSize: 16, height: 1.6),
            ),
          ],
        ),
      ),
    );
  }
}
""")

# ==================== 13. faq_screen.dart ====================
write_file(f"{base_dir}/lib/features/faq/faq_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});

  final List<Map<String, String>> faqs = const [
    {
      'q': 'كم مدة إجازة الوضع للمرأة العاملة؟',
      'a': '60 يوماً مدفوعة الأجر وفقاً لقانون العمل اليمني.',
    },
    {
      'q': 'ما هي حقوق المرأة في الميراث؟',
      'a': 'كفل القانون اليمني والشريعة الإسلامية للمرأة حقها الكامل في الميراث.',
    },
    {
      'q': 'هل يحق فصل العامل دون سبب؟',
      'a': 'لا، يحق للعامل المطالبة بتعويض في حالة الفصل التعسفي.',
    },
    {
      'q': 'ما هي سن الحضانة للأم؟',
      'a': 'حتى سن السابعة للذكر والتاسعة للأنثى.',
    },
    {
      'q': 'ما هي حقوق ذوي الإعاقة في التعليم؟',
      'a': 'التعليم المجاني والإلزامي مع توفير البيئة المناسبة.',
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('الأسئلة الشائعة')),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: faqs.length,
        itemBuilder: (context, index) {
          final faq = faqs[index];
          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child: ExpansionTile(
              leading: CircleAvatar(
                backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
                child: const Icon(Icons.help_outline, color: AppTheme.yemeniGreen),
              ),
              title: Text(
                faq['q']!,
                style: const TextStyle(fontWeight: FontWeight.bold),
              ),
              children: [
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: Text(faq['a']!),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
""")

# ==================== 14. AndroidManifest.xml ====================
write_file(f"{base_dir}/android/app/src/main/AndroidManifest.xml", """<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET"/>
    <application
        android:label="حقي كيمني"
        android:name="\${applicationName}"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"/>
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <meta-data android:name="flutterEmbedding" android:value="2"/>
    </application>
</manifest>
""")

# ==================== 15. MainActivity.kt ====================
write_file(f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity()
""")

# ==================== 16. styles.xml ====================
write_file(f"{base_dir}/android/app/src/main/res/values/styles.xml", """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="LaunchTheme" parent="@android:style/Theme.Light.NoTitleBar">
        <item name="android:windowBackground">@android:color/white</item>
    </style>
    <style name="NormalTheme" parent="@android:style/Theme.Light.NoTitleBar">
        <item name="android:windowBackground">@android:color/white</item>
    </style>
</resources>
""")

# ==================== 17. README.md ====================
write_file(f"{base_dir}/README.md", """# حقي كيمني - My Yemeni Right

التطبيق القانوني الشامل للمواطن اليمني

## الخطوات

```bash
flutter pub get
flutter build apk --release
