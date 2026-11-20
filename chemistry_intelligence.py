#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🧪 HSC CHEMISTRY A+ SUPER-INTELLIGENCE SYSTEM (রসায়ন সুপার ইন্টেলিজেন্স)
=============================================================================
Designed for HSC Bangladesh Board Candidates targeting A+ (GPA 5.00) in 7 Days
Author: Antigravity Super Intelligence Engine
Repository: https://github.com/ZubairZerok/HscChemistry
=============================================================================
"""

import sys
import os
import math
import json

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

# --- COLOR CODES FOR BEAUTIFUL TERMINAL DISPLAY ---
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def banner():
    print(Color.CYAN + Color.BOLD + "=" * 75)
    print("      🧪 HSC CHEMISTRY A+ SUPER-INTELLIGENCE ENGINE (রসায়ন সুপার ইন্টেলিজেন্স)")
    print("            7-Day Strategic Mastery for 80%+ Guaranteed Marks")
    print("=" * 75 + Color.END)

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {"Day 1": False, "Day 2": False, "Day 3": False, "Day 4": False, "Day 5": False, "Day 6": False, "Day 7": False}

def save_progress(data):
    try:
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving progress: {e}")

# --- MODULE 1: 7-DAY BATTLE PLAN NAVIGATOR ---
def battle_plan_navigator():
    progress = load_progress()
    while True:
        print("\n" + Color.YELLOW + Color.BOLD + "📅 7-DAY ULTRA BATTLEPLAN NAVIGATOR" + Color.END)
        print("-" * 50)
        days = [
            ("Day 1", "রাসায়নিক পরিবর্তন (Kp, Kc, pH, বাফার দ্রবণ)", "1st Ch.4", 25),
            ("Day 2", "জৈব রসায়ন পর্ব-১ (অ্যালিফেটিক, সমাণুতা, অ্যালকেন/অ্যালকিন)", "2nd Ch.2", 15),
            ("Day 3", "জৈব রসায়ন পর্ব-২ (অ্যারোমেটিক, বেনজিন, লুকাস, টলেন, রূপান্তর)", "2nd Ch.2", 20),
            ("Day 4", "মৌলের পর্যায়বৃত্ত ধর্ম ও বন্ধন (সংকরণ, VSEPR, ফাজান)", "1st Ch.3", 22),
            ("Day 5", "তড়িৎ রসায়ন ও গুণগত রসায়ন (নার্নস্ট, ফ্যারাডে, বোর মডেল, Ksp)", "2nd Ch.4 & 1st Ch.2", 35),
            ("Day 6", "পরিমাণগত ও পরিবেশ রসায়ন (টাইট্রেশন, গ্যাস সূত্র, শিল্প রসায়ন)", "2nd Ch.3 & 1st Ch.1,5", 25),
            ("Day 7", "পূর্ণাঙ্গ রিভিশন + সূত্রাবলী মেমোরাইজেশন + পূর্ণাঙ্গ মক টেস্ট", "উভয় পত্র", 100),
        ]
        for key, title, paper, marks in days:
            status = Color.GREEN + "[COMPLETED ✅]" + Color.END if progress.get(key) else Color.RED + "[PENDING ⏳]" + Color.END
            print(f"  {Color.BOLD}{key}{Color.END}: {title:<55} {status}")

        print("\nকমান্ড:")
        print("  [1-7] নির্দিষ্ট দিনের বিস্তারিত গাইডলাইন ও হাজারে-নাগ পেজ দেখতে")
        print("  [c]   কোনো দিনের স্ট্যাটাস টগল (Completed / Pending) করতে")
        print("  [b]   প্রধান মেন্যুতে ফিরে যেতে")
        choice = input(Color.CYAN + "পছন্দ লিখুন > " + Color.END).strip().lower()

        if choice == 'b':
            break
        elif choice == 'c':
            day_num = input("কোন দিনের স্ট্যাটাস পরিবর্তন করবেন? (১-৭) > ").strip()
            key = f"Day {day_num}"
            if key in progress:
                progress[key] = not progress[key]
                save_progress(progress)
                print(Color.GREEN + f"✅ {key} এর স্ট্যাটাস আপডেট করা হয়েছে!" + Color.END)
        elif choice in [str(i) for i in range(1, 8)]:
            show_day_detail(int(choice))

def show_day_detail(day_num):
    details = {
        1: {
            "title": "Day 1: রাসায়নিক পরিবর্তন (1st Paper Ch.4)",
            "pages": "হাজারী ১ম পত্র: পৃষ্ঠা ৩৮১ – ৪৫৬ (পিডিএফ পৃষ্ঠা ৩৯২ – ৪৬৭)",
            "topics": [
                "১. ভরক্রিয়া সূত্র ও সাম্যধ্রুবক Kp ও Kc এর গাণিতিক হিসাব (পৃষ্ঠা ৩৮৭ – ৩৯৩)",
                "২. Kp ও Kc এর সম্পর্ক: Kp = Kc(RT)^Δn এর সমাধান (পৃষ্ঠা ৩৮৯ – ৩৯১)",
                "৩. লা-শাতেলিয়ার নীতি: তাপমাত্রা, চাপ ও ঘনমাত্রার প্রভাব (পৃষ্ঠা ৪০২ – ৪০৭)",
                "৪. pH ও pOH গণনা, পানির আয়নিক গুণফল Kw (পৃষ্ঠা ৪২৮ – ৪৩২)",
                "৫. বাফার দ্রবণ প্রস্তুতি, ক্রিয়াকৌশল ও হেন্ডারসন সমীকরণ (পৃষ্ঠা ৪৪০ – ৪৪৭)"
            ],
            "target": "২৫ – ৩০ নম্বর নিশ্চিত করণ (বোর্ডে ২টি পূর্ণ CQ)"
        },
        2: {
            "title": "Day 2: জৈব রসায়ন পর্ব-১ (2nd Paper Ch.2)",
            "pages": "হাজারী ২য় পত্র: পৃষ্ঠা ১৯৭ – ৩৩৪ (পিডিএফ পৃষ্ঠা ২০৮ – ৩৪৫)",
            "topics": [
                "১. কার্বনের সংকরণ ও IUPAC নামকরণ পদ্ধতি (পৃষ্ঠা ২০১ – ২১৮)",
                "২. জ্যামিতিক (cis-trans) ও আলোক সমাণুতা, কাইরাল কার্বন (পৃষ্ঠা ২২৭ – ২৩৭)",
                "৩. কার্বোক্যাটায়ন, কার্বঅ্যানায়ন ও মুক্তমূলক স্থায়িত্ব (পৃষ্ঠা ২২৩ – ২২৪)",
                "৪. অ্যালকেন প্রস্তুতি (উর্টজ, ডিকার্বক্সিলেশন) (পৃষ্ঠা ২৫৭ – ২৬০)",
                "৫. অ্যালকিনে মার্কভনিকভ ও বিপরীত মার্কভনিকভ নীতি (পৃষ্ঠা ২৬৮ – ২৭০)",
                "৬. অ্যালকিনের ওজোনোলিসিস ও Zn চূর্ণের ভূমিকা (পৃষ্ঠা ২৭১ – ২৭৩)"
            ],
            "target": "১৫ – ২০ নম্বর নিশ্চিত করণ"
        },
        3: {
            "title": "Day 3: জৈব রসায়ন পর্ব-২: অ্যারোমেটিক ও ফাংশনাল গ্রুপ (2nd Paper Ch.2)",
            "pages": "হাজারী ২য় পত্র: পৃষ্ঠা ২৯০ – ৫৭০ (পিডিএফ পৃষ্ঠা ৩০১ – ৫৮১)",
            "topics": [
                "১. হাকেল নিয়ম (4n+2 π ইলেকট্রন) ও অ্যারোমেটিসিটি (পৃষ্ঠা ৩০৬ – ৩০৭)",
                "২. বেনজিনের ইলেকট্রনাকর্ষী প্রতিস্থাপন: নাইট্রেশন, সালফোনেশন, ফ্রিডেল-ক্রাফটস (পৃষ্ঠা ২৯৯ – ৩০৫)",
                "৩. অর্থো-প্যারা নির্দেশক বনাম মেটা নির্দেশক গ্রুপ (পৃষ্ঠা ৩১০ – ৩১২)",
                "৪. ১°, ২° ও ৩° অ্যালকোহল পৃথকীকরণ: লুকাস বিকারক পরীক্ষা (পৃষ্ঠা ৩৯৪ – ৩৯৬)",
                "৫. ফেনলের অম্লত্ব, ব্রোমিন পানি ও FeCl3 পরীক্ষা (পৃষ্ঠা ৪০০ – ৪০৮)",
                "৬. টলেন বিকারক, ফেলিং দ্রবণ, আয়োডোফর্ম পরীক্ষা (পৃষ্ঠা ৪৪৮ – ৪৬৭)",
                "৭. অ্যালডল ঘনীভবন ও ক্যানিজারো বিক্রিয়া (পৃষ্ঠা ৪৫৪ – ৪৫৬)",
                "৮. কার্বিল অ্যামিন ও ডায়াজোটাইজেশন বিক্রিয়া (পৃষ্ঠা ৫৬৩ – ৫৭০)"
            ],
            "target": "২০ – ২৫ নম্বর নিশ্চিত করণ"
        },
        4: {
            "title": "Day 4: পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (1st Paper Ch.3)",
            "pages": "হাজারী ১ম পত্র: পৃষ্ঠা ২৫৭ – ৩২৩ (পিডিএফ পৃষ্ঠা ২৬৮ – ৩৩৪)",
            "topics": [
                "১. পর্যায়বৃত্ত প্রবণতা: আয়নীকরণ শক্তি, ইলেকট্রন আসক্তি ও ব্যতিক্রমসমূহ (N>O, Cl>F)",
                "২. হাইব্রিডাইজেশন সংকরণ: sp, sp2, sp3, sp3d, sp3d2 নির্ণয় ও আকৃতি (পৃষ্ঠা ২৯৮ – ৩০৬)",
                "৩. VSEPR নীতি: লোন পেয়ারের কারণে বন্ধন কোণের পরিবর্তন (H2O 104.5°, NH3 107°)",
                "৪. ফাজানের নিয়ম: পোলারায়ন ও সমযোজী বৈশিষ্ট্য বৃদ্ধির শর্তাবলি (পৃষ্ঠা ২৮৪ – ২৮৮)",
                "৫. হাইড্রোজেন বন্ধন (আন্তঃআণবিক বনাম অন্তঃআণবিক) ও স্ফুটনাংক (পৃষ্ঠা ২৯৩ – ২৯৭)",
                "৬. আণবিক অরবিটাল তত্ত্ব (MOT) ও বন্ড অর্ডার নির্ণয় (পৃষ্ঠা ৩০৭ – ৩১০)"
            ],
            "target": "২০ – ২৫ নম্বর নিশ্চিত করণ"
        },
        5: {
            "title": "Day 5: তড়িৎ রসায়ন ও গুণগত রসায়ন (2nd Ch.4 & 1st Ch.2)",
            "pages": "হাজারী ১ম পত্র: পৃষ্ঠা ৯১ – ১৮৫ | ২য় পত্র: পৃষ্ঠা ৪৫৭ – ৫১৪",
            "topics": [
                "১. ডেনিয়েল কোষ ও লবণ সেতুর কার্যপ্রণালী (পৃষ্ঠা ৪৮১ – ৪৮৬)",
                "২. নার্নস্ট সমীকরণ প্রয়োগ করে কোষের EMF গণনা (পৃষ্ঠা ৪৯৩ – ৫০০)",
                "৩. ফ্যারাডের ১ম ও ২য় সূত্র প্রয়োগ করে সঞ্চিত ভর ও গ্যাসের আয়তন গণনা (পৃষ্ঠা ৪৬২ – ৪৭২)",
                "৪. বোর পরমাণু মডেল, হাইড্রোজেন বর্ণালী ও রিডবার্গ ধ্রুবক ম্যাথ (পৃষ্ঠা ১০৬ – ১০৮)",
                "৫. ৪টি কোয়ান্টাম সংখ্যা (n, l, m, s) ও ইলেক্ট্রন বিন্যাস নীতি (পৃষ্ঠা ১১০ – ১২৪)",
                "৬. দ্রাব্যতা গুণফল (Ksp) ও আয়নিক গুণফল (Kip) দ্বারা অধঃক্ষেপের শর্ত"
            ],
            "target": "৩৫ – ৪০ নম্বর নিশ্চিত করণ"
        },
        6: {
            "title": "Day 6: পরিমাণগত ও পরিবেশ রসায়ন (2nd Ch.3 & 1st Ch.1,5)",
            "pages": "হাজারী ১ম পত্র: পৃষ্ঠা ১ – ৯০, ১৯৫ – ২৫৬ | ২য় পত্র: পৃষ্ঠা ১ – ৯০",
            "topics": [
                "১. বয়েল, চার্লস, আদর্শ গ্যাস সমীকরণ (PV = nRT) ও ডাল্টনের আংশিক চাপ (পৃষ্ঠা ১৯ – ৩২)",
                "২. গ্রাহামের ব্যাপন সূত্র ও আণবিক ভর নির্ণয় (পৃষ্ঠা ৩৩ – ৩৬)",
                "৩. পরিবেশ দূষণ, গ্রিনহাউস গ্যাস, ওজোন স্তর ক্ষয়, BOD, COD, DO, TDS",
                "৪. এসিড-ক্ষার টাইট্রেশন ও মোলারিটি, নরমালিটি, ppm ঘনমাত্রা রূপান্তর",
                "৫. জারক-বিজারক সমতাকরণ ও আয়োডিমিতি/আয়োডোমিতি",
                "৬. শিল্প রসায়ন: ভিনেগার, খাদ্য সংরক্ষক, গ্লাস, সিমেন্ট ও ইউরিয়া উৎপাদন"
            ],
            "target": "২৫ – ৩০ নম্বর নিশ্চিত করণ"
        },
        7: {
            "title": "Day 7: পূর্ণাঙ্গ রিভিশন + সূত্রাবলী মেমোরাইজেশন + পূর্ণাঙ্গ মক টেস্ট",
            "pages": "INTELLIGENCE/04-FORMULA-SHEET.md ও 05-ORGANIC-CONVERSION-MAP.md",
            "topics": [
                "১. সকালের সেশন: পূর্ণাঙ্গ সূত্রাবলী লিখে প্র্যাকটিস করা (১ ঘণ্টা)",
                "২. রূপান্তর মাস্টার ম্যাপ দেখে মুখস্থ ২০টি রূপান্তর খাতায় লিখা (১ ঘণ্টা)",
                "৩. ৫০টি বহুনির্বাচনি প্রশ্ন টাইমার ধরে সমাধান করা (২৫ মিনিট + ২৫ মিনিট)",
                "৪. ১ম পত্রের ৫টি পূর্ণাঙ্গ CQ খাতায় লিখা (৫০ মিনিট)",
                "৫. ২য় পত্রের ৫টি পূর্ণাঙ্গ CQ খাতায় লিখা (৫০ মিনিট)",
                "৬. সন্ধ্যার সেশন: ভুল হওয়া প্রশ্ন বিশ্লেষণ ও দুর্বল টপিক রিভিশন (২ ঘণ্টা)"
            ],
            "target": "বোর্ডে ৮০ – ৯৫ নম্বর ও A+ সম্পূর্ণ প্রস্তুত!"
        }
    }
    
    info = details.get(day_num, {})
    print("\n" + Color.GREEN + Color.BOLD + f"=== {info.get('title')} ===" + Color.END)
    print(Color.CYAN + f"📖 বইয়ের পৃষ্ঠা: {info.get('pages')}" + Color.END)
    print(Color.YELLOW + f"🎯 প্রত্যাশিত নম্বর: {info.get('target')}" + Color.END)
    print("\nমূল টপিকসমূহ:")
    for t in info.get("topics", []):
        print(f"  • {t}")
    input("\n[Enter চাপুন মেন্যুতে ফিরে যেতে] ")

# --- MODULE 2: HAJARI SIR EXACT PAGE FINDER ---
def page_finder():
    database = [
        {"keyword": "kp", "topic": "Kp ও Kc সাম্যধ্রুবক, সম্পর্ক ও গাণিতিক সমস্যা", "paper": "১ম পত্র", "page": "৩৮৭ – ৩৯৩"},
        {"keyword": "kc", "topic": "Kp ও Kc সাম্যধ্রুবক, সম্পর্ক ও গাণিতিক সমস্যা", "paper": "১ম পত্র", "page": "৩৮৭ – ৩৯৩"},
        {"keyword": "ph", "topic": "pH স্কেল, তীব্র ও মৃদু অম্ল/ক্ষারের pH গণনা", "paper": "১ম পত্র", "page": "৪২৯ – ৪৩২"},
        {"keyword": "buffer", "topic": "বাফার দ্রবণ, ক্রিয়াকৌশল ও হেন্ডারসন সমীকরণ", "paper": "১ম পত্র", "page": "৪৪০ – ৪৪৭"},
        {"keyword": "সংকরণ", "topic": "অরবিটাল সংকরণ (sp, sp2, sp3, sp3d) ও আকৃতি", "paper": "১ম পত্র", "page": "২৯৮ – ৩০৬"},
        {"keyword": "hybridization", "topic": "অরবিটাল সংকরণ (sp, sp2, sp3, sp3d) ও আকৃতি", "paper": "১ম পত্র", "page": "২৯৮ – ৩০৬"},
        {"keyword": "fajan", "topic": "ফাজানের নিয়ম ও সমযোজী বৈশিষ্ট্য", "paper": "১ম পত্র", "page": "২৮৪ – ২৮৮"},
        {"keyword": "ফাজান", "topic": "ফাজানের নিয়ম ও সমযোজী বৈশিষ্ট্য", "paper": "১ম পত্র", "page": "২৮৪ – ২৮৮"},
        {"keyword": "bohr", "topic": "বোর পরমাণু মডেল ও হাইড্রোজেন বর্ণালী", "paper": "১ম পত্র", "page": "১০৬ – ১০৮"},
        {"keyword": "কোয়ান্টাম", "topic": "কোয়ান্টাম সংখ্যাসমূহ (n, l, m, s) ও ইলেকট্রন বিন্যাস", "paper": "১ম পত্র", "page": "১১০ – ১২১"},
        {"keyword": "quantum", "topic": "কোয়ান্টাম সংখ্যাসমূহ (n, l, m, s) ও ইলেকট্রন বিন্যাস", "paper": "১ম পত্র", "page": "১১০ – ১২১"},
        {"keyword": "বয়েল", "topic": "বয়েল ও চার্লসের সূত্র, আদর্শ গ্যাস সমীকরণ (PV=nRT)", "paper": "১ম পত্র", "page": "৮ – ২৬"},
        {"keyword": "gas", "topic": "বয়েল ও চার্লসের সূত্র, আদর্শ গ্যাস সমীকরণ (PV=nRT)", "paper": "১ম পত্র", "page": "৮ – ২৬"},
        {"keyword": "ডাল্টন", "topic": "ডাল্টনের আংশিক চাপ সূত্র ও গাণিতিক সমস্যা", "paper": "১ম পত্র", "page": "২৭ – ৩২"},
        {"keyword": "markovnikov", "topic": "মার্কভনিকভ ও বিপরীত মার্কভনিকভ নীতি (পারঅক্সাইড)", "paper": "২য় পত্র", "page": "২৬৮ – ২৭০"},
        {"keyword": "মার্কভনিকভ", "topic": "মার্কভনিকভ ও বিপরীত মার্কভনিকভ নীতি (পারঅক্সাইড)", "paper": "২য় পত্র", "page": "২৬৮ – ২৭০"},
        {"keyword": "ওজোনোলিসিস", "topic": "অ্যালকিনের ওজোনোলিসিস ও কার্বনাইল যৌগ প্রস্তুতি", "paper": "২য় পত্র", "page": "২৭১ – ২৭৩"},
        {"keyword": "ozonolysis", "topic": "অ্যালকিনের ওজোনোলিসিস ও কার্বনাইল যৌগ প্রস্তুতি", "paper": "২য় পত্র", "page": "২৭১ – ২৭৩"},
        {"keyword": "lucas", "topic": "লুকাস বিকারক পরীক্ষা (১°, ২°, ৩° অ্যালকোহল পৃথকীকরণ)", "paper": "২য় পত্র", "page": "৩৯৪ – ৩৯৬"},
        {"keyword": "লুকাস", "topic": "লুকাস বিকারক পরীক্ষা (১°, ২°, ৩° অ্যালকোহল পৃথকীকরণ)", "paper": "২য় পত্র", "page": "৩৯৪ – ৩৯৬"},
        {"keyword": "tollen", "topic": "টলেন বিকারক ও ফেলিং দ্রবণ দ্বারা অ্যালডিহাইড শনাক্তকরণ", "paper": "২য় পত্র", "page": "৪৬৫ – ৪৬৭"},
        {"keyword": "টলেন", "topic": "টলেন বিকারক ও ফেলিং দ্রবণ দ্বারা অ্যালডিহাইড শনাক্তকরণ", "paper": "২য় পত্র", "page": "৪৬৫ – ৪৬৭"},
        {"keyword": "aldol", "topic": "অ্যালডল ঘনীভবন ও ক্যানিজারো বিক্রিয়া", "paper": "২য় পত্র", "page": "৪৫৪ – ৪৫৬"},
        {"keyword": "cannizzaro", "topic": "অ্যালডল ঘনীভবন ও ক্যানিজারো বিক্রিয়া", "paper": "২য় পত্র", "page": "৪৫৪ – ৪৫৬"},
        {"keyword": "ক্যানিজারো", "topic": "অ্যালডল ঘনীভবন ও ক্যানিজারো বিক্রিয়া", "paper": "২য় পত্র", "page": "৪৫৪ – ৪৫৬"},
        {"keyword": "বেনজিন", "topic": "বেনজিন বলয়ে ইলেকট্রনাকর্ষী প্রতিস্থাপন ও হাকেল নীতি", "paper": "২য় পত্র", "page": "২৯৯ – ৩০৭"},
        {"keyword": "benzene", "topic": "বেনজিন বলয়ে ইলেকট্রনাকর্ষী প্রতিস্থাপন ও হাকেল নীতি", "paper": "২য় পত্র", "page": "২৯৯ – ৩০৭"},
        {"keyword": "nernst", "topic": "নার্নস্ট সমীকরণ ও কোষের EMF নির্ণয়", "paper": "২য় পত্র (বা ১ম)", "page": "৪৯৩ – ৫০০"},
        {"keyword": "নার্নস্ট", "topic": "নার্নস্ট সমীকরণ ও কোষের EMF নির্ণয়", "paper": "২য় পত্র (বা ১ম)", "page": "৪৯৩ – ৫০০"},
        {"keyword": "faraday", "topic": "ফ্যারাডের তড়িৎ বিশ্লেষণের সূত্রাবলি ও ভর গণনা", "paper": "২য় পত্র (বা ১ম)", "page": "৪৬২ – ৪৭২"},
        {"keyword": "ফ্যারাডে", "topic": "ফ্যারাডের তড়িৎ বিশ্লেষণের সূত্রাবলি ও ভর গণনা", "paper": "২য় পত্র (বা ১ম)", "page": "৪৬২ – ৪৭২"},
        {"keyword": "রূপান্তর", "topic": "পরিশিষ্ট ৩, ৪, ৫: কার্বন শিকল বৃদ্ধি/হ্রাস ও রূপান্তর ম্যাপ", "paper": "২য় পত্র", "page": "৬৬৪ – ৬৬৭"},
        {"keyword": "conversion", "topic": "পরিশিষ্ট ৩, ৪, ৫: কার্বন শিকল বৃদ্ধি/হ্রাস ও রূপান্তর ম্যাপ", "paper": "২য় পত্র", "page": "৬৬৪ – ৬৬৭"},
    ]
    
    print("\n" + Color.CYAN + Color.BOLD + "🔍 হাজারী-নাগ পাঠ্যবই ইনস্ট্যান্ট পেজ ফাইন্ডার" + Color.END)
    print("টপিকের নাম বা কিওয়ার্ড লিখুন (যেমন: Kp, pH, buffer, ফাজান, markovnikov, lucas, tollen, nernst, faraday):")
    query = input(Color.YELLOW + "খুঁজুন > " + Color.END).strip().lower()
    if not query:
        return

    matches = [item for item in database if query in item["keyword"] or query in item["topic"].lower()]
    if matches:
        print("\n" + Color.GREEN + f"✅ {len(matches)}টি ফলাফল পাওয়া গেছে:" + Color.END)
        print("-" * 70)
        for m in matches:
            print(f"  📌 {Color.BOLD}{m['topic']}{Color.END}")
            print(f"     বই: {m['paper']} | {Color.YELLOW}বইয়ের পৃষ্ঠা: {m['page']}{Color.END}")
            print("-" * 70)
    else:
        print(Color.RED + f"❌ '{query}' সম্পর্কিত নির্দিষ্ট পৃষ্ঠা পাওয়া যায়নি। অনুগ্রহ করে HAJARI-1-EXACT-PAGE-INDEX.md বা HAJARI-2-EXACT-PAGE-INDEX.md দেখুন।" + Color.END)
    input("\n[Enter চাপুন মেন্যুতে ফিরে যেতে] ")

# --- MODULE 3: SUPER CHEMISTRY FORMULA CALCULATOR ---
def formula_calculator():
    while True:
        print("\n" + Color.PURPLE + Color.BOLD + "🧮 SUPER CHEMISTRY FORMULA CALCULATOR" + Color.END)
        print("  [1] Kp ও Kc রূপান্তর ক্যালকুলেটর (Kp = Kc * (RT)^Δn)")
        print("  [2] দ্রবণ pH ও pOH ক্যালকুলেটর")
        print("  [3] বাফার দ্রবণ pH ক্যালকুলেটর (হেন্ডারসন-হ্যাসেলবালখ সমীকরণ)")
        print("  [4] নার্নস্ট সমীকরণ সেল বিভব (Ecell) ক্যালকুলেটর")
        print("  [5] ফ্যারাডের ১ম সূত্র ভর ক্যালকুলেটর (W = MIt / nF)")
        print("  [6] আদর্শ গ্যাস সূত্র ক্যালকুলেটর (PV = nRT)")
        print("  [b] প্রধান মেন্যুতে ফিরে যেতে")
        choice = input(Color.CYAN + "পছন্দ লিখুন > " + Color.END).strip()

        if choice == 'b':
            break
        elif choice == '1':
            try:
                kc = float(input("Kc এর মান লিখুন: "))
                temp_c = float(input("তাপমাত্রা (°C এ) লিখুন: "))
                delta_n = float(input("Δn এর মান লিখুন (গ্যাসীয় উৎপাদ মোল - গ্যাসীয় বিক্রিয়ক মোল): "))
                temp_k = temp_c + 273.15
                r = 0.0821
                kp = kc * math.pow(r * temp_k, delta_n)
                print(Color.GREEN + f"\n✅ ফলাফল: T = {temp_k} K, Kp = {kp:.6f}" + Color.END)
                if delta_n == 0:
                    print("নোট: যেহেতু Δn = 0, তাই Kp = Kc এবং এটি এককবিহীন।")
            except Exception as e:
                print(Color.RED + f"গণনায় ত্রুটি: {e}" + Color.END)
        elif choice == '2':
            try:
                conc = float(input("দ্রবণের হাইড্রোজেন আয়ন ঘনমাত্রা [H+] (mol/L) লিখুন (যেমন: 0.01): "))
                if conc <= 0:
                    print(Color.RED + "ঘনমাত্রা ধনাত্মক হতে হবে!" + Color.END)
                    continue
                ph = -math.log10(conc)
                poh = 14.0 - ph
                print(Color.GREEN + f"\n✅ ফলাফল: pH = {ph:.3f}, pOH = {poh:.3f}" + Color.END)
                nature = "অম্লীয় (Acidic)" if ph < 7 else ("ক্ষারীয় (Basic)" if ph > 7 else "নিরপেক্ষ (Neutral)")
                print(f"দ্রবণের প্রকৃতি: {nature}")
            except Exception as e:
                print(Color.RED + f"গণনায় ত্রুটি: {e}" + Color.END)
        elif choice == '3':
            try:
                pka = float(input("এসিডের pKa লিখুন (যেমন: CH3COOH এর জন্য 4.745): "))
                salt_mol = float(input("লবণের মোল বা মিলিমোল লিখুন: "))
                acid_mol = float(input("মৃদু এসিডের মোল বা মিলিমোল লিখুন: "))
                if salt_mol <= 0 or acid_mol <= 0:
                    print(Color.RED + "মোল সংখ্যা শূন্য অপেক্ষা বড় হতে হবে!" + Color.END)
                    continue
                ph = pka + math.log10(salt_mol / acid_mol)
                print(Color.GREEN + f"\n✅ হেন্ডারসন সমীকরণ মতে বাফারের pH = {ph:.3f}" + Color.END)
            except Exception as e:
                print(Color.RED + f"গণনায় ত্রুটি: {e}" + Color.END)
        elif choice == '4':
            try:
                e_standard = float(input("প্রমাণ সেল বিভব E°cell (V এ) লিখুন (যেমন: ডেনিয়েল সেলে 1.10): "))
                n = int(input("স্থানান্তরিত ইলেকট্রন সংখ্যা n লিখুন (যেমন: 2): "))
                anode_conc = float(input("অ্যানোড আয়নের ঘনমাত্রা [Anode^n+] লিখুন (যেমন: 0.05): "))
                cathode_conc = float(input("ক্যাথোড আয়নের ঘনমাত্রা [Cathode^n+] লিখুন (যেমন: 0.01): "))
                q = anode_conc / cathode_conc
                ecell = e_standard - (0.0591 / n) * math.log10(q)
                print(Color.GREEN + f"\n✅ 25°C এ নার্নস্ট সেল বিভব Ecell = {ecell:.4f} V" + Color.END)
            except Exception as e:
                print(Color.RED + f"গণনায় ত্রুটি: {e}" + Color.END)
        elif choice == '5':
            try:
                molar_mass = float(input("সঞ্চিত ধাতুর মোলার ভর M (g/mol) লিখুন (Cu=63.5, Ag=108, Al=27): "))
                current = float(input("তড়িৎ প্রবাহ I (Amperes এ) লিখুন: "))
                time_sec = float(input("সময় t (সেকেন্ড এ) লিখুন (যেমন: 40 min = 2400 s): "))
                n = int(input("যোজ্যতা বা স্থানান্তরিত ইলেকট্রন n লিখুন (Cu=2, Ag=1, Al=3): "))
                f = 96500.0
                mass = (molar_mass * current * time_sec) / (n * f)
                print(Color.GREEN + f"\n✅ ক্যাথোডে সঞ্চিত ধাতুর ভর W = {mass:.4f} গ্রাম" + Color.END)
            except Exception as e:
                print(Color.RED + f"গণনায় ত্রুটি: {e}" + Color.END)
        elif choice == '6':
            try:
                p = float(input("চাপ P (atm এ) লিখুন: "))
                v = float(input("আয়তন V (L এ) লিখুন: "))
                temp_c = float(input("তাপমাত্রা T (°C এ) লিখুন: "))
                temp_k = temp_c + 273.15
                r = 0.0821
                n = (p * v) / (r * temp_k)
                print(Color.GREEN + f"\n✅ গ্যাসের মোল সংখ্যা n = {n:.4f} mol" + Color.END)
            except Exception as e:
                print(Color.RED + f"গণনায় ত্রুটি: {e}" + Color.END)

# --- MODULE 4: ORGANIC REACTION & CONVERSION HIGHWAY ---
def organic_conversion_highway():
    conversions = [
        {
            "name": "ইথানল হতে অ্যাসিটিক এসিড (Ethanol to Acetic Acid)",
            "steps": [
                "ধাপ ১: ইথানল + [O] --(K2Cr2O7 + গাঢ় H2SO4)--> অ্যাসিটালডিহাইড (CH3CHO) + H2O",
                "ধাপ ২: অ্যাসিটালডিহাইড + [O] --(K2Cr2O7 + গাঢ় H2SO4)--> অ্যাসিটিক এসিড (CH3COOH)"
            ],
            "conditions": "তীব্র জারক K2Cr2O7 + গাঢ় H2SO4"
        },
        {
            "name": "ইথাইন হতে অ্যাসিটালডিহাইড (Ethyne to Acetaldehyde)",
            "steps": [
                "CH≡CH + H2O --(20% H2SO4, 2% HgSO4, 60°C)--> [CH2=CH-OH] (অস্থায়ী ইনল) --> CH3CHO (অ্যাসিটালডিহাইড)"
            ],
            "conditions": "২০% H2SO4, ২% HgSO4, ৬০°C তাপমাত্রা"
        },
        {
            "name": "মিথেন হতে ইথেন (কার্বন শিকল বৃদ্ধি - Wurtz বিক্রিয়া)",
            "steps": [
                "ধাপ ১: CH4 + Cl2 --(UV আলো)--> CH3Cl + HCl",
                "ধাপ ২: 2CH3Cl + 2Na --(শুষ্ক ইথার)--> CH3-CH3 (ইথেন) + 2NaCl"
            ],
            "conditions": "শুষ্ক ইথার দ্রাবক এবং ধাতব সোডিয়াম (Na)"
        },
        {
            "name": "বেনজিন হতে অ্যানিলিন (Benzene to Aniline)",
            "steps": [
                "ধাপ ১ (নাইট্রেশন): C6H6 + HNO3 --(গাঢ় H2SO4, 55°C)--> C6H5NO2 (নাইট্রোবেনজিন) + H2O",
                "ধাপ ২ (বিজারণ): C6H5NO2 + 6[H] --(Sn + গাঢ় HCl)--> C6H5NH2 (অ্যানিলিন) + 2H2O"
            ],
            "conditions": "গাঢ় HNO3/H2SO4 অতঃপর Sn + HCl বিজারণ"
        },
        {
            "name": "অ্যানিলিন হতে ফেনল (ডায়াজোটাইজেশন ও আর্দ্রবিশ্লেষণ)",
            "steps": [
                "ধাপ ১: C6H5NH2 + NaNO2 + 2HCl --(0° - 5°C)--> C6H5N2+Cl- (বেনজিন ডায়াজোনিয়াম ক্লোরাইড) + NaCl + 2H2O",
                "ধাপ ২: C6H5N2+Cl- + H2O --(হালকা গরম, 40°C)--> C6H5OH (ফেনল) + N2↑ + HCl"
            ],
            "conditions": "০° - ৫°C বরফ-শীতল তাপমাত্রা নিশ্চিত রাখতে হবে"
        },
        {
            "name": "টলুইন হতে বেনজোয়িক এসিড (পার্শ্ব-শিকল জারণ)",
            "steps": [
                "C6H5-CH3 + 3[O] --(ক্ষারীয় KMnO4, উত্তাপ / অতঃপর লঘু HCl)--> C6H5-COOH (বেনজোয়িক এসিড) + H2O"
            ],
            "conditions": "ক্ষারীয় KMnO4 দ্রবণ সহযোগে রিফ্লাক্স"
        },
        {
            "name": "ফেনল হতে পিকরিক এসিড (২,৪,৬-ট্রাইনাইট্রোফেনল)",
            "steps": [
                "C6H5OH + 3HNO3 (গাঢ়) --(গাঢ় H2SO4, উত্তাপ)--> C6H2(NO2)3OH (পিকরিক এসিড) + 3H2O"
            ],
            "conditions": "গাঢ় নাইট্রিক ও সালফিউরিক এসিড মিশ্রণ"
        }
    ]

    print("\n" + Color.GREEN + Color.BOLD + "🛣️ মাস্টার অর্গানিক কনভার্শন হাইওয়ে (বোর্ড পরীক্ষার শীর্ষ রূপান্তরসমূহ)" + Color.END)
    for idx, conv in enumerate(conversions, 1):
        print(f"  [{idx}] {conv['name']}")
    print("  [b] ফিরে যেতে")

    choice = input(Color.CYAN + "রূপান্তর নং লিখুন > " + Color.END).strip()
    if choice.isdigit() and 1 <= int(choice) <= len(conversions):
        c = conversions[int(choice) - 1]
        print("\n" + Color.YELLOW + Color.BOLD + f"=== {c['name']} ===" + Color.END)
        print("প্রয়োজনীয় শর্তাবলী: " + Color.CYAN + c['conditions'] + Color.END)
        print("বিক্রিয়া ধাপসমূহ:")
        for s in c['steps']:
            print(f"  ➡️ {s}")
        input("\n[Enter চাপুন মেন্যুতে ফিরে যেতে] ")

# --- MODULE 5: INSTANT MCQ PRACTICE QUIZ ---
def mcq_quiz():
    questions = [
        {
            "q": "কোন মৌলের ১ম আয়নীকরণ শক্তি সবচেয়ে বেশি?",
            "options": ["(ক) বোরন (B)", "(খ) কার্বন (C)", "(গ) নাইট্রোজেন (N)", "(ঘ) অক্সিজেন (O)"],
            "ans": 3,
            "exp": "নাইট্রোজেনের 2p অরবিটাল অর্ধপূর্ণ (2p3) হওয়ায় তা অতিরিক্ত সুস্থিত। ফলে অক্সিজেনের চেয়েও নাইট্রোজেনের ১ম আয়নীকরণ শক্তি বেশি।"
        },
        {
            "q": "PCl5 অণুতে ফসফরাসের অরবিটাল সংকরণ কোনটি?",
            "options": ["(ক) sp2", "(খ) sp3", "(গ) sp3d", "(ঘ) sp3d2"],
            "ans": 3,
            "exp": "স্টেরিক নম্বর = ৫টি বন্ধন + ০ মুক্তজোড় = ৫, যা sp3d সংকরণ (আকৃতি: ত্রিকোণাকার দ্বিপিরামিডীয়)।"
        },
        {
            "q": "টলেন বিকারকের সাথে সিলভার দর্পণ পরীক্ষা দেয় কোনটি?",
            "options": ["(ক) প্রোপানোন", "(খ) অ্যাসিটালডিহাইড", "(গ) ইথাইল এসিটেট", "(ঘ) ডাইমিথাইল ইথার"],
            "ans": 2,
            "exp": "অ্যালডিহাইডে মুক্ত -CHO গ্রুপ থাকায় এটি টলেন বিকারককে বিজারিত করে সিলভারের রূপালি দর্পণ তৈরি করে।"
        },
        {
            "q": "১ ফ্যারাডে (1 F) বিদ্যুৎ চালনায় ক্যাথোডে কত গ্রাম কপার জমা হবে? (Cu = 63.5)",
            "options": ["(ক) 63.5 g", "(খ) 31.75 g", "(গ) 127.0 g", "(ঘ) 21.17 g"],
            "ans": 2,
            "exp": "Cu2+ + 2e- -> Cu। ১ মোল কপার জমার জন্য ২ ফ্যারাডে বিদ্যুৎ লাগে। অতএব ১ ফ্যারাডে জমা হবে 63.5 / 2 = 31.75 গ্রাম।"
        },
        {
            "q": "নিচের কোনটি অর্থো-প্যারা নির্দেশক এবং বলয় সক্রিয়কারী মূলক?",
            "options": ["(ক) -NO2", "(খ) -COOH", "(গ) -OH", "(ঘ) -CHO"],
            "ans": 3,
            "exp": "-OH মূলকের অক্সিজেনে মুক্তজোড় ইলেকট্রন থাকায় তা রেজোন্যান্সের মাধ্যমে বেনজিন বলয়ে ইলেকট্রন ঘনত্ব বৃদ্ধি করে এবং বলয় সক্রিয় করে।"
        }
    ]

    print("\n" + Color.PURPLE + Color.BOLD + "📝 দ্রুত বহুনির্বাচনি কুইজ (MCQ Rapid Fire)" + Color.END)
    score = 0
    for idx, item in enumerate(questions, 1):
        print(f"\nপ্রশ্ন {idx}: {Color.BOLD}{item['q']}{Color.END}")
        for opt in item['options']:
            print(f"  {opt}")
        user_ans = input(Color.CYAN + "সঠিক উত্তর নির্বাচন করুন (1, 2, 3 বা 4) > " + Color.END).strip()
        if user_ans.isdigit() and int(user_ans) == item["ans"]:
            print(Color.GREEN + "অভিনন্দন! সঠিক উত্তর! 🎉" + Color.END)
            score += 1
        else:
            print(Color.RED + f"ভুল উত্তর! সঠিক উত্তর ছিল: বিকল্প ({item['ans']})" + Color.END)
        print(Color.YELLOW + f"ব্যাখ্যা: {item['exp']}" + Color.END)

    print("\n" + Color.BOLD + f"আপনার মোট স্কোর: {score} / {len(questions)}" + Color.END)
    if score == len(questions):
        print(Color.GREEN + "দুর্দান্ত! আপনি রসায়নে নিশ্চিত A+ পাওয়ার যোগ্য! 🏆" + Color.END)
    else:
        print(Color.YELLOW + "আরো একটু অনুশীলন করুন। INTELLIGENCE ফোল্ডারের ফাইলগুলো রিভিশন দিন।" + Color.END)
    input("\n[Enter চাপুন মেন্যুতে ফিরে যেতে] ")

# --- MAIN CONTROLLER ---
def main():
    while True:
        banner()
        print("  [1] 📅 ৭ দিনের আল্ট্রা স্টাডি নেভিগেটর ও চেকলিস্ট ট্র্যাকার")
        print("  [2] 🔍 হাজারী-নাগ পাঠ্যবই ইনস্ট্যান্ট পেজ ফাইন্ডার (Hajari Page Finder)")
        print("  [3] 🧮 সুপার কেমিস্ট্রি ফর্মুলা ক্যালকুলেটর (Kp, Kc, pH, Nernst, Faraday)")
        print("  [4] 🛣️ অর্গানিক কনভার্শন হাইওয়ে (Master Reaction Roadmaps)")
        print("  [5] 📝 ইনস্ট্যান্ট MCQ কুইজ ও স্পিড টেস্ট")
        print("  [6] 🔮 ২০২৫-২০২৬ বোর্ড পরীক্ষার নিশ্চিত প্রেডিকশন ও সাজেশন")
        print("  [0] প্রস্থান (Exit)")
        print("-" * 75)
        choice = input(Color.CYAN + "আপনার কমান্ড নম্বর লিখুন > " + Color.END).strip()

        if choice == '1':
            battle_plan_navigator()
        elif choice == '2':
            page_finder()
        elif choice == '3':
            formula_calculator()
        elif choice == '4':
            organic_conversion_highway()
        elif choice == '5':
            mcq_quiz()
        elif choice == '6':
            pred_file = os.path.join(os.path.dirname(__file__), "INTELLIGENCE", "10-HSC-A-PLUS-PREDICTION-SUGGESTION-2025-2026.md")
            if os.path.exists(pred_file):
                print("\n" + Color.GREEN + "=== বোর্ড পরীক্ষার নিশ্চিত প্রেডিকশন ও সাজেশন ===" + Color.END)
                with open(pred_file, 'r', encoding='utf-8') as f:
                    print(f.read()[:2000] + "\n\n...সম্পূর্ণ পড়তে INTELLIGENCE/10-HSC-A-PLUS-PREDICTION-SUGGESTION-2025-2026.md ফাইলটি খুলুন।")
                input("\n[Enter চাপুন মেন্যুতে ফিরে যেতে] ")
        elif choice == '0':
            print(Color.GREEN + "\nধন্যবাদ! তোমার HSC Chemistry A+ নিশ্চিত হোক! শুভকামনা! 🌟\n" + Color.END)
            break
        else:
            print(Color.RED + "ভুল ইনপুট! দয়া করে সঠিক বিকল্প বেছে নিন।" + Color.END)

if __name__ == "__main__":
    main()
